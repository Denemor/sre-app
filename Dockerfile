FROM python:3.8-slim

WORKDIR /app

RUN groupadd -r sre-app && \
    useradd --no-log-init -r -g sre-app sre-app

COPY requirements.txt ./

RUN pip install -r requirements.txt

USER sre-app

EXPOSE 5000

COPY . ./

CMD ["python", "app.py"]