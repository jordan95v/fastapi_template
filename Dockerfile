FROM python:3.13.2-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install . 

CMD alembic upgrade head && fastapi run core/main.py