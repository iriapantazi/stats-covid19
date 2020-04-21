FROM python:3.7

WORKDIR /usr/src/covid_http_api

EXPOSE 5000

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "app.py"]
