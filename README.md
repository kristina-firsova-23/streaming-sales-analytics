# 🚀 Streaming Sales Analytics Pipeline

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Redis](https://img.shields.io/badge/Redis-7.0-red.svg)](https://redis.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://www.postgresql.org/)
[![Grafana](https://img.shields.io/badge/Grafana-10.0-orange.svg)](https://grafana.com/)
[![Docker](https://img.shields.io/badge/Docker-24.0-blue.svg)](https://www.docker.com/)

**Потоковая обработка данных о продажах в реальном времени.**

## 📊 Архитектура

## 🛠 Технологии

| Компонент | Технология | Назначение |
|-----------|------------|------------|
| Генератор данных | Python + Faker | Создаёт случайные транзакции |
| Очередь сообщений | Redis | Буферизация потока |
| Обработчик | Python (чистый код) | Агрегация в реальном времени |
| Хранилище | PostgreSQL | Сохранение агрегатов |
| Визуализация | Grafana | Дашборд с графиками |
| Оркестрация | Docker Compose | Запуск всех сервисов |

## 🚀 Быстрый старт

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/kristina-firsova-23/streaming-sales-analytics.git
cd streaming-sales-analytics