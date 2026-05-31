import json
import time
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import redis

# Подключение к Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

spark = SparkSession.builder \
    .appName("SalesStreamProcessor") \
    .config("spark.jars.packages", "org.postgresql:postgresql:42.7.3") \
    .getOrCreate()

schema = StructType([
    StructField("transaction_id", StringType()),
    StructField("timestamp", StringType()),
    StructField("product", StringType()),
    StructField("quantity", IntegerType()),
    StructField("price", FloatType()),
    StructField("customer_city", StringType())
])

print("🔥 Ожидание сообщений из Redis...")

def process_batch():
    while True:
        # Берём все сообщения из Redis
        batch = []
        while True:
            msg = r.lpop('sales_stream')
            if not msg:
                break
            batch.append(json.loads(msg))
        
        if batch:
            # Преобразуем в Spark DataFrame
            df = spark.createDataFrame(batch, schema) \
                .withColumn("timestamp", to_timestamp(col("timestamp")))
            
            # Агрегация
            aggregated = df.groupBy("product").agg(
                sum("quantity").alias("total_quantity"),
                sum(col("quantity") * col("price")).alias("total_revenue"),
                count("*").alias("transaction_count")
            )
            
            aggregated.show()
            
            # Запись в PostgreSQL
            aggregated.write \
                .format("jdbc") \
                .option("url", "jdbc:postgresql://localhost:5432/analytics") \
                .option("dbtable", "sales_aggregates") \
                .option("user", "admin") \
                .option("password", "admin") \
                .mode("append") \
                .save()
            
            print(f"✅ Обработано {len(batch)} записей")
        
        time.sleep(5)

if __name__ == "__main__":
    process_batch()