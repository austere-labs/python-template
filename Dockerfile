FROM python:3.11-slim-bookworm
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r /app/requirements.txt
EXPOSE 8080
COPY . .
CMD uvicorn app:app --port 8080 --host 0.0.0.0