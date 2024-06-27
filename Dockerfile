# Dockerfile

# Базовий образ
FROM python:3.10

# Встановлюємо необхідні системні пакети
RUN apt-get update \
    && apt-get install -y \
    libpq-dev \
    gcc \
    && apt-get clean

# Встановлюємо необхідні Python пакети
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Копіюємо проект
COPY . /app
WORKDIR /app

# Збирання статичних файлів
RUN python manage.py collectstatic --noinput

# Команда для запуску проекту
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "shop_project.wsgi:application"]
