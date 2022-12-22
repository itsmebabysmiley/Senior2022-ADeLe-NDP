FROM python:3.7-alpine
FROM tensorflow/tensorflow:2.9.3

WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# RUN apk add --no-cache gcc musl-dev linux-headers
EXPOSE 5000
COPY . .
CMD ["flask", "run"]