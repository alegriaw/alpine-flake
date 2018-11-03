# home.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:red'>This is Home!</h1>"

if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=5000)
