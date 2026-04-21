from flask import Flask, render_template, request, jsonify, session
from mini_transformer import build_and_train, predict
import os
import logging

# Configuración básica de logs para ver qué pasa en el backend
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = "secret-2026-premium"

# Inicialización del modelo (Singleton pattern)
logger.info("Cargando modelo...")
model, w2i, i2w, v_size, loss = build_and_train()
logger.info("Modelo listo.")

# --- RUTAS DE NAVEGACIÓN ---
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

# --- API ENDPOINTS ---
@app.route("/status", methods=["GET"])
def status():
    return jsonify({"vocab_size": v_size, "loss": round(float(loss), 4)})

@app.route("/predict", methods=["POST"])
def pred():
    try:
        data = request.json
        words = data.get('words', '').split()
        res = predict(model, words, w2i, i2w)
        return jsonify({"results": res})
    except Exception as e:
        logger.error(f"Error en predicción: {e}")
        return jsonify({"results": []}), 500

@app.route("/train", methods=["POST"])
def train():
    global model, w2i, i2w, v_size, loss
    try:
        new_text = request.json.get('text', '')
        if new_text:
            # Guardado persistente
            with open("training_data.txt", "a", encoding="utf-8") as f:
                f.write("\n" + new_text)
            # Reentrenar modelo
            model, w2i, i2w, v_size, loss = build_and_train()
            logger.info("Modelo reentrenado con éxito.")
        return jsonify({"success": True})
    except Exception as e:
        logger.error(f"Error en entrenamiento: {e}")
        return jsonify({"success": False}), 500

# API de autenticación simulada (para tu login.html)
@app.route("/api/login", methods=["POST"])
def api_login():
    # Aquí iría tu lógica de verificación real
    return jsonify({"success": True})

@app.route("/api/register", methods=["POST"])
def api_register():
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(debug=True, port=5000)