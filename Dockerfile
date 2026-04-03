FROM python:3.11-slim

# Evita arquivos temporários e permite logs imediatos
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia e instala bibliotecas Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Expõe a porta do Render
EXPOSE 10000

# Comando para iniciar (ajuste se o seu arquivo principal for outro)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "10000"]