from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Render!</h1><p>My First PaaS Web Application</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

