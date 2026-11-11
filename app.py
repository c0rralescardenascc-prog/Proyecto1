from flask import Flask, request, jsonify, render_template

import json

import os

 

app = Flask(__name__)

ARCHIVO = "datos.json"

 

 

@app.route("/")

def inicio():

    return render_template("index.html")

 

 

@app.route("/registrar", methods=["POST"])

def registrar():

    datos = request.get_json()

    nombre = datos.get("nombre", "").strip()

 

    if not nombre:

        return jsonify({"mensaje": "El campo está vacío", "total": 0}), 400

 

    if os.path.exists(ARCHIVO):

        with open(ARCHIVO, "r", encoding="utf-8") as f:

            registros = json.load(f)

    else:

        registros = []

 

    registros.append({"nombre": nombre})

 

    with open(ARCHIVO, "w", encoding="utf-8") as f:

        json.dump(registros, f, ensure_ascii=False, indent=2)

 

    return jsonify({"mensaje": f"Guardado: {nombre}", "total": len(registros)})

 

 

if __name__ == "__main__":

    app.run(debug=True)
