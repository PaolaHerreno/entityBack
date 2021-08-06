FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY essai.py .
COPY fonctions.py .
COPY humains_toMongo.json .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./essai.py" ]