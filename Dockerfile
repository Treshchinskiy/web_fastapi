# Используем базовый образ с Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл requirements.txt в контейнер
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

# Копируем все файлы проекта в контейнер
COPY ./app /app

# Устанавливаем зависимости

# Команда запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
