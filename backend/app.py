from flask import Flask, request, jsonify
import device_manager

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add_device():
    data = request.json
    device_manager.add_device(data["id"], data["type"], data["firmware"])
    return jsonify({"status": "added"}), 200

@app.route("/remove", methods=["POST"])
def remove_device():
    data = request.json
    device_manager.remove_device(data["id"])
    return jsonify({"status": "removed"}), 200

@app.route("/update_firmware", methods=["POST"])
def update_firmware():
    data = request.json
    device_manager.update_firmware(data["id"], data["firmware"])
    return jsonify({"status": "updated"}), 200
