FROM python:3.10.12-slim

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN chmod +x /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]