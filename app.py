from flask import Flask, render_template, url_for, request

app = Flask(__name__)

data = [
    {"Date": "2024-11-07", "Temperature": 5, "Hour": "12","Weather Description": "clear sky"},
    {"Date": "2024-11-07", "Temperature": 6, "Hour": "13","Weather Description": "few clouds"},
    {"Date": "2024-11-07", "Temperature": 4, "Hour": "14","Weather Description": "scattered clouds"},
]

@app.route('/')
def index():
    return render_template('index.html',data=data)


if __name__ == "__main__":
    app.run(debug=True)