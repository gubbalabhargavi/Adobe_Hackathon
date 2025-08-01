FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install pymupdf

CMD ["python", "main.py"]
