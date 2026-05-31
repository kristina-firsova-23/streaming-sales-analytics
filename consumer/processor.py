import json
import time
import psycopg2
import redis
from collections import defaultdict
from datetime import datetime

# Подключение к Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Подключение к PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="analytics",
    user="admin",
    password="admin"
)
cur = conn.cursor()

# Создаём таблицу
cur.execute("""
    CREATE TABLE IF NOT EXISTS sales_aggregates (
        id SERIAL PRIMARY KEY,
        product VARCHAR(50),
        total_quantity INTEGER,
        total_revenue FLOAT,
        transaction_count INTEGER,
        processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

print("🔥 Обработчик запущен, ожидаем сообщения...")

def process_batch(messages):
    aggregates = defaultdict(lambda: {'quantity': 0, 'revenue': 0, 'count': 0})
    
    for msg in messages:
        sale = json.loads(msg)
        product = sale['product']
        qty = sale['quantity']
        revenue = qty * sale['price']
        
        aggregates[product]['quantity'] += qty
        aggregates[product]['revenue'] += revenue
        aggregates[product]['count'] += 1
    
    for product, data in aggregates.items():
        cur.execute("""
            INSERT INTO sales_aggregates (product, total_quantity, total_revenue, transaction_count)
            VALUES (%s, %s, %s, %s)
        """, (product, data['quantity'], data['revenue'], data['count']))
    
    conn.commit()
    print(f"✅ Обработано {len(messages)} транзакций, {len(aggregates)} уникальных товаров")

while True:
    messages = []
    # Забираем все сообщения из очереди
    while True:
        msg = r.lpop('sales_stream')
        if not msg:
            break
        messages.append(msg)
    
    if messages:
        process_batch(messages)
    else:
        time.sleep(1)