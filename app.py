"""Aplikasi Flask sederhana untuk demo pipeline."""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    """Endpoint utama."""
    return jsonify(message="Hello, pipeline!")


@app.route("/health")
def health():
    """Endpoint health check."""
    return jsonify(status="ok")
