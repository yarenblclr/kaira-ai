from flask import Flask
from flask_cors import CORS

from config import DevelopmentConfig
from app.database import close_db, init_db
from app.routes import api, pages


def create_app():
    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    CORS(app)

    app.register_blueprint(pages)
    app.register_blueprint(api, url_prefix="/api")

    app.teardown_appcontext(close_db)

    with app.app_context():
        init_db()

    @app.route("/health")
    def health():
        return {
            "basari": True,
            "durum": "aktif",
            "uygulama": "Kaira AI"
        }

    return app