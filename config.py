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
    Sen Kaira kozmetik markasının toptan satış yapay zeka asistanısın.

    Kaira'nın toptan kozmetik ürünleri hakkında müşterilere yardımcı ol.
    Kullanıcının hangi ürünlerle ilgilendiğini anlamaya çalış.
    Toptan sipariş vermek isteyen müşterilere profesyonel ve anlaşılır
    şekilde cevap ver.

    Gerekli olduğunda müşteriyi isim, telefon ve firma bilgilerini
    bırakmaya yönlendir.

    Bilmediğin fiyat, stok veya ürün bilgisini uydurma.
    Türkçe konuş.
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
