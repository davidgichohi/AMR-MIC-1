from flask import Flask, jsonify, send_from_directory
import json
import os

app = Flask(__name__, static_folder='static')

# API endpoints
@app.route('/api/mic_rules')
def get_mic_rules():
    with open('mic_rules_final.json') as f:
        return jsonify(json.load(f))

@app.route('/api/organism_sampletype')
def get_sampletype():
    with open('organism_sampletype_full.json') as f:
        return jsonify(json.load(f))

@app.route('/api/antibiotic_classes')
def get_antibiotic_classes():
    with open('antibiotic_classes_full.json') as f:
        return jsonify(json.load(f))

# Serve frontend
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # use Render's PORT or fallback to 5000 locally
    app.run(host="0.0.0.0", port=port)
