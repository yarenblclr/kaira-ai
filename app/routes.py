from flask import Blueprint, jsonify, render_template, request

from app.database import lead_ekle, tum_leadler
from app.services.ai_service import AIService


pages = Blueprint("pages", __name__)
api = Blueprint("api", __name__)


@pages.route("/")
def ana_sayfa():
    return render_template("index.html")


@pages.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@api.route("/sohbet", methods=["POST"])
def sohbet():
    data = request.get_json() or {}
    mesaj = data.get("mesaj", "").strip()

    if not mesaj:
        return jsonify({
            "basari": False,
            "hata": "Mesaj boş olamaz."
        }), 400

    cevap = AIService.cevapla(mesaj)

    return jsonify({
        "basari": True,
        "cevap": cevap
    })


@api.route("/leads", methods=["POST"])
def yeni_lead():
    data = request.get_json() or {}

    isim = data.get("isim", "").strip()
    telefon = data.get("telefon", "").strip()

    if not isim or not telefon:
        return jsonify({
            "basari": False,
            "hata": "İsim ve telefon zorunludur."
        }), 400

    lead_ekle(
        isim=isim,
        telefon=telefon,
        firma=data.get("firma"),
        urun_ilgisi=data.get("urun_ilgisi"),
        mesaj=data.get("mesaj")
    )

    return jsonify({
        "basari": True,
        "mesaj": "Talebiniz başarıyla kaydedildi."
    }), 201


@api.route("/leads", methods=["GET"])
def leadleri_getir():
    return jsonify({
        "basari": True,
        "leads": tum_leadler()
    })