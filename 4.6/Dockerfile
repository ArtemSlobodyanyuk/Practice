# Базовий образ
FROM python:3.11-slim

# Робоча директорія
WORKDIR /app

# Копіюємо залежності і встановлюємо
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо код
COPY app/ .

# Відкриваємо порт
EXPOSE 5000

# Команда запуску
CMD ["python", "app.py"]