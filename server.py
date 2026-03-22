from flask import Flask
import os

app = Flask(__name__)


@app.get("/")
def hello_world():
    name = os.environ.get("NAME", "world").strip() or "world"
    return f"Hello, {name}!\n"


@app.get("/health")
def health():
    return "ok\n", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", "8080"))
    app.run(host="0.0.0.0", port=port)