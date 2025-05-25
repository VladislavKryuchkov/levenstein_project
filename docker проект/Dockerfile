# Используем официальный образ Python
FROM python:3.9-slim

# Рабочая директория
WORKDIR /app

# Копируем файлы проекта
COPY requirements.txt setup.py .
COPY levenshtein_cli.py ./

# Устанавливаем зависимости и пакет
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir .

# По умолчанию переменные окружения (пример для базы данных)
ENV DB_HOST=db.example.com \
    DB_PORT=5432 \
    DB_NAME=lev_db

# По желанию задайте точку входа
ENTRYPOINT ["levenshtein"]