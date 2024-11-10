import os
from flask import Blueprint, request, send_from_directory, jsonify
from .file_generator import generate_file

main_bp = Blueprint('main', __name__)

@main_bp.route('/generate', methods=['POST'])
def generate():
    data = request.json
    text = data.get("text")
    title = data.get("title")
    file_format = data.get("format", "txt").lower()
    
    if not text or not title or file_format not in ["docx", "pdf", "txt"]:
        return jsonify({"error": "Invalid input data"}), 400

    file_path = generate_file(text, title, file_format)
    file_name = os.path.basename(file_path)

    return jsonify({"download_url": f"/download/{file_name}"}), 200

@main_bp.route('/download/<filename>', methods=['GET'])
def download(filename):
    return send_from_directory('static/files', filename)
