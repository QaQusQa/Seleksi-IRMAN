
from flask import Flask, request, jsonify
from flask_cors import CORS
from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Literal
import json

app = Flask(__name__)
CORS(app)

DATA_FILE = "data.json"

#Model validasi peserta
class Peserta(BaseModel) :
    nisn: str
    tanggal: str

    @field_validator("tanggal")
    @classmethod
    def validasi_tanggal(cls, v) : 
        try :
            datetime.strptime(v, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Format harus dd-mm-yyyy")
        return v

# Cek data peserta dari file JSON
@app.route("/cek", methods=["POST"])
def cek() :
    try :
        peserta_data = request.json
        print("Menerima request:", request.json)

        peserta = Peserta(**peserta_data)
        print("Data valid", peserta)

        with open(DATA_FILE, "r", encoding="utf-8") as f :
            data = json.load(f)

        
        hasil = next((item for item in data if item["nisn"] == peserta.nisn and item["tanggal"] == peserta.tanggal), None)

        if hasil :
            return jsonify({**hasil, "success": True})
        else :
            return jsonify({"message": "Data tidak ditemukan", "success" : False}), 404
    
    except Exception as e :
        print("Validasi gagal:", e)
        return jsonify({
            "message" : str(e),
            "success" : False
        }), 400
    
if __name__ == "__main__" :
    from os import environ
    port = int(environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)