from flask import Flask

app = Flask("E-commerce Fraudometer")

@app.route("/hello_world")
def hello_world():
    return "<p>Hello, world</p>"

@app.route("/analyze/<url>")
def analyze(url: str):
    return f"<p>Analyzing url {url}"
