from flask import Flask, request, jsonify
from problem_1 import Functional_Des

app = Flask(__name__)
chall = Functional_Des()

@app.route("/challenge", methods=["GET"])
def challenge():
    try:
        challenge_hex = chall.get_challenge().hex()
        return jsonify({"challenge": challenge_hex})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.get_json()
    if not data or "ct" not in data:
        return jsonify({"error": "Missing ciphertext (ct) in payload."}), 400
    try:
        ct = bytes.fromhex(data["ct"])
        decrypted = chall.decrypt(ct)
        return jsonify({"decrypted": decrypted.hex()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/reveal", methods=["POST"])
def reveal():
    data = request.get_json()
    if not data or "pt" not in data:
        return jsonify({"error": "Missing plaintext (pt) in payload."}), 400
    try:
        pt = bytes.fromhex(data["pt"])
        result = chall.get_random_string(pt)
        # Attempt to decode flag; if not possible, return hex
        try:
            flag_str = result.decode("utf-8")
        except UnicodeDecodeError:
            flag_str = result.hex()
        return jsonify({"flag": flag_str})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
