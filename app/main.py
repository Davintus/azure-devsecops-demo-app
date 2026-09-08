from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify(
        {
            "application": "azure-devsecops-demo-app",
            "status": "running",
            "version": "1.0.0",
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.get("/ready")
def readiness():
    return jsonify({"status": "ready"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # nosec B104 - intentional container binding
