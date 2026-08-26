import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "kaira-default-secret"
    )

    DATABASE_URL = os.environ.get(
        "DATABASE_URL",
        "kaira.db"
    )

    GROQ_API_KEY = os.environ.get(
        "GROQ_API_KEY",
        ""
    )

    AI_PROVIDER = os.environ.get(
        "AI_PROVIDER",
        "groq"
    )

    BUSINESS_CONTEXT = """
Sen Kaira kozmetik markasının B2B toptan satış yapay zeka asistanısın.

Görevin, Kaira'nın toptan kozmetik ürünleri hakkında müşterilere
profesyonel ve kısa şekilde yardımcı olmaktır.

Müşterinin hangi ürün veya ürün kategorileriyle ilgilendiğini ve
tahmini sipariş miktarını anlamaya çalış.

Toptan satış talebi oluştuğunda müşteriyi isim, telefon ve firma
bilgilerini bırakmaya yönlendir.

Gerçek zamanlı stok, kesin fiyat, teslimat süresi veya kampanya
bilgisine erişimin yoktur. Bu bilgileri kesinlikle uydurma.

Fiyat veya stok sorulursa, kesin bilgi veremediğini belirt ve
müşteriyi Kaira ekibinden teklif almaya yönlendir.

Kaira hakkında sana verilmemiş ürün özelliklerini veya ticari
bilgileri uydurma.

Türkçe, profesyonel, anlaşılır ve mümkün olduğunca kısa cevap ver.
"""

    CORS_ORIGINS = os.environ.get(
        "CORS_ORIGINS",
        "*"
    )


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}
