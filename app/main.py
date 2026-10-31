from flask import Flask, jsonify, render_template, request
from pathlib import Path
import json, secrets, time

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

app = Flask(__name__, template_folder=str(ROOT / "templates"),
            static_folder=str(ROOT / "static"))
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

@app.after_request
def security_headers(resp):
    resp.headers["X-Content-Type-Options"] = "nosniff"
    resp.headers["X-Frame-Options"] = "DENY"
    resp.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    resp.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    return resp

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "AICTE FDR Management Portal"})

@app.get("/api/config")
def config():
    return jsonify({
        "name": "AICTE Security Deposit / FDR Management Portal",
        "version": "1.0.0",
        "environment": "prototype"
    })

@app.post("/api/audit")
def audit():
    payload = request.get_json(silent=True) or {}
    event = {
        "id": secrets.token_hex(8),
        "timestamp": int(time.time()),
        "event": payload.get("event", "unknown"),
        "user": payload.get("user", "unknown")
    }
    audit_file = DATA / "audit.jsonl"
    with audit_file.open("a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")
    return jsonify({"saved": True, "id": event["id"]}), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
