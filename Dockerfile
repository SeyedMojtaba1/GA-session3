FROM python:3.12-slim

COPY requirements.txt .

RUN apt-get update && apt-get install pip
RUN pip install -r requirements.txt

COPY main.py .

EXPOSE 5000

CMD [ "python", "main.py" ]