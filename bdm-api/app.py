from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

from models import db

# Crear las tablas de la base de datos
with app.app_context():
    db.create_all()

from blueprints import artists, genres

app.register_blueprint(artists)
app.register_blueprint(genres)