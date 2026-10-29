FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# el código se monta como volumen en compose (desarrollo con --reload)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]
