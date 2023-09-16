FROM python:3.9-slim-buster

WORKDIR /usr/src/app

COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

CMD ["python", "docker_app.py"]
