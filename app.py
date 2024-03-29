from flask import Flask, request, Response
import json
from models.usuario import db, Users
from controllers import blue as usuario_controller
from dotenv import load_dotenv
import os
import jwt # lib for create tokens
import datetime
from werkzeug.security import check_password_hash

# Load the enviroment variables
load_dotenv(".env")

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI_MYSQL")
app.config["SECRET_KEY"] = os.getenv("APP_SECRET_KEY")

# Inicia e configura o banco de dados
db.init_app(app=app)
with app.test_request_context():
        db.create_all()

# Register the usuario's blueprint
app.register_blueprint(usuario_controller, url_prefix="/users/")


if __name__ == "__main__":
    app.run(debug=True)
    