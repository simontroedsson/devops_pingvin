FROM python:3.9
COPY requirements.txt /app/
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]