FROM python:3.7.7-stretch

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "app.api:app", "--proxy-headers", "--host", "0.0.0.0" ]