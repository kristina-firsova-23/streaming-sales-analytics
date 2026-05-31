# 🚀 Streaming Sales Analytics Pipeline

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Redis](https://img.shields.io/badge/Redis-7.0-red.svg)](https://redis.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![Grafana](https://img.shields.io/badge/Grafana-10.0-orange.svg)](https://grafana.com/)
[![Docker](https://img.shields.io/badge/Docker-24.0-blue.svg)](https://www.docker.com/)

**Потоковая обработка данных о продажах в реальном времени.**
![Dashboard](dashboard-screensho.jpg)
![Dashboard](graph.jpg)
## 📊 Архитектура
Producer (Python) → Redis Queue → Consumer (Python) → PostgreSQL → Grafana

## Технологии

- Python + Faker (генератор данных)
- Redis (очередь сообщений)
- PostgreSQL (хранилище)
- Grafana (дашборд)
- Docker Compose (оркестрация)

## Быстрый старт

```bash
git clone https://github.com/kristina-firsova-23/streaming-sales-analytics.git
cd streaming-sales-analytics
docker-compose up -d
pip install -r requirements.txt
python producer/sales_producer.py
python consumer/processor.py
