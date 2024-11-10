# Установка Python
FROM python:3.10-slim

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копирование приложения
COPY app/ app/

# Установка переменных окружения для Flask
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

# Открываем порт для Flask
EXPOSE 5000

# Запуск приложения
CMD ["flask", "run"]
