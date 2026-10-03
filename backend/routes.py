from flask import Blueprint, render_template, request, jsonify
from .services.ai_service import ask_ai
from .modules.meta_ai import improve_python_code
from .modules.quantum_ai import quantum_state
from .modules.mirror_ai import mirror_response
from .modules.storyteller_ai import create_story

main = Blueprint("main", __name__)

@main.get("/")
def index():
    return render_template("index.html")

@main.post("/api/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"error": "Nachricht fehlt."}), 400
    return jsonify({"reply": ask_ai(message)})

@main.post("/api/mirror")
def mirror():
    data = request.get_json(silent=True) or {}
    return jsonify({"reply": mirror_response(data.get("message", ""))})

@main.post("/api/story")
def story():
    data = request.get_json(silent=True) or {}
    return jsonify({"story": create_story(data.get("prompt", ""))})

@main.post("/api/quantum")
def quantum():
    data = request.get_json(silent=True) or {}
    return jsonify(quantum_state(data.get("input", "")))

@main.post("/api/meta/improve")
def meta_improve():
    data = request.get_json(silent=True) or {}
    return jsonify(improve_python_code(data.get("code", "")))
