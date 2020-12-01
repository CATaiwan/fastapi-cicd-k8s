FROM python:3.7.7-stretch

COPY . /fastapi_cicd_demo

WORKDIR /fastapi_cicd_demo

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "fastapi_cicd_demo.main:app", "--proxy-headers", "--reload", "--host", "0.0.0.0" ]