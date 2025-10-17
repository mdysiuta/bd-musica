from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import app
from util import create_slug

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)
migrate = Migrate(app, db)

class Artist(db.Model):
    __tablename__ = "artists"
    id:   Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    slug: Mapped[str] = mapped_column(unique=True)