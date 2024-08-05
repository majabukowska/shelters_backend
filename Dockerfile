# Etap 1: Budowanie
FROM python:3-slim AS builder

WORKDIR /app

COPY requirements.txt .
# Instalujemy zależności globalnie, żeby były dostępne w ostatecznym obrazie
RUN pip install --no-cache-dir -r requirements.txt

# Etap 2: Uruchamianie
FROM python:3-slim AS runner

WORKDIR /app

# Kopiujemy zależności z builder
COPY --from=builder /usr/local /usr/local

# Kopiujemy aplikację
COPY . .
ENV DJANGO_SETTINGS_MODULE=shelters_backend.settings

ENV PORT=8000

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "shelters_backend.wsgi"]
