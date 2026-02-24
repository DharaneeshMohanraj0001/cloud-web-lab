from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! My Cloud Web Application is Running Successfully 🚀"

@app.route('/about')
def about():
    return "This app is deployed in Public Cloud using Render."

if __name__ == '__main__':
    app.run()