from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

from src.main.routes.cnpj_routes import cnpj_route_bp
from src.main.routes.cpf_routes import cpf_route_bp

db_connection_handler.connect_to_db()


app = Flask(__name__)
CORS(app)

app.register_blueprint(cnpj_route_bp)
app.register_blueprint(cpf_route_bp)
