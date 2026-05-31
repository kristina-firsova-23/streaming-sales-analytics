import json
import time
import random
from faker import Faker
import redis

fake = Faker()

# Подключение к Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse']

print("🚀 Начинаем генерацию продаж и отправку в Redis...")

try:
    while True:
        sale = {
            'transaction_id': fake.uuid4(),
            'timestamp': fake.iso8601(),
            'product': random.choice(products),
            'quantity': random.randint(1, 5),
            'price': round(random.uniform(10, 1500), 2),
            'customer_city': fake.city()
        }
        
        # Отправляем в Redis список (лист)
        r.rpush('sales_stream', json.dumps(sale))
        print(f"📤 Отправлено: {sale['product']} x{sale['quantity']} - ${sale['price']}")
        
        time.sleep(random.uniform(0.5, 2))
        
except KeyboardInterrupt:
    print("\n👋 Остановка producer'а")