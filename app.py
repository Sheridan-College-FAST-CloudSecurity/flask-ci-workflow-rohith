from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, DevSecOps! modified after failure verified in settings actions as well"

if __name__ == "__main__":
    app.run()
