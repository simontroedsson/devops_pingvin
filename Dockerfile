FROM python:3.9
ARG API_KEY
ENV API_KEY=${API_KEY}
COPY requirements.txt /app/
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]
