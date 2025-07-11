# Use a lightweight Python base image
FROM python:3.11-alpine

# Set working directory inside the container
WORKDIR /app

ARG DJANGO_ALLOWED_HOSTS
ENV DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}

# Install necessary dependencies
RUN apk add --no-cache \
    build-base \
    libffi-dev \
    postgresql-dev \
    && pip install --no-cache-dir --upgrade pip

# Copy application requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy project files into the container
COPY . .

# Set the environment variables
ENV PYTHONUNBUFFERED=1
# RUN python manage.py collectstatic --noinput

# Expose the application port
EXPOSE 8000

# Command to run the Django server
COPY start.sh .
RUN chmod +x start.sh

CMD ["sh", "start.sh"]

