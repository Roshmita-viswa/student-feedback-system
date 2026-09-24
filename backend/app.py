from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.environ.get("DB_PATH", "/data/feedback.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS feedback "
        "(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, department TEXT, feedback TEXT)"
    )
    conn.commit()
    conn.close()

@app.route("/api/health")
def health():
    return jsonify({"status": "Backend is running"})

@app.route("/api/feedback", methods=["POST"])
def add_feedback():
    data = request.get_json() or {}
    name = data.get("name", "").strip()
    department = data.get("department", "").strip()
    feedback = data.get("feedback", "").strip()

    if not name or not department or not feedback:
        return jsonify({"message": "Please fill all fields."}), 400

    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO feedback (name, department, feedback) VALUES (?, ?, ?)",
        (name, department, feedback)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Feedback submitted successfully! 🎉"}), 201

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
