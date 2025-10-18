from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from app import app
from util import create_slug

import sqlalchemy as sa

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

class Genre(db.Model):
    __tablename__ = "genres"
    id:   Mapped[int]  = mapped_column(primary_key=True)
    name: Mapped[str]  = mapped_column(unique=True)
    top:  Mapped[bool] = mapped_column(default=False)
    slug: Mapped[str]  = mapped_column(unique=True)

subgenre_m2m = db.Table(
    "subgenres",
    sa.Column("parent_id", sa.ForeignKey(Genre.id), primary_key=True),
    sa.Column("child_id",  sa.ForeignKey(Genre.id), primary_key=True),
)

'''
class ReleaseType(db.Model):
    __tablename__ = "release_types"
    id:       Mapped[int]             = mapped_column(primary_key=True)
    name:     Mapped[str]             = mapped_column(unique=True)
    releases: Mapped[List["Release"]] = relationship(back_populates="release_type")

class Release(db.Model):
    __tablename__ = "releases"
    id:              Mapped[int]           = mapped_column(primary_key=True)
    release_type_id: Mapped[int]           = mapped_column(ForeignKey("release_types.id"))
    release_type:    Mapped["ReleaseType"] = relationship(back_populates="releases")
    title:           Mapped[str]           = mapped_column(unique=True)

class Song(db.Model):
    __tablename__ = "songs"
    id:    Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)

class ReleaseGenre(db.Model):
    __tablename__ = "release_genres"
    release_id: Mapped[int] = mapped_column()
    genre_id:   Mapped[int] = mapped_column()
    priority:   Mapped[int] = mapped_column(nullable=True)

class ReleaseInfluence(db.Model):
    __tablename__ = "release_influences"
    release_id: Mapped[int] = mapped_column()
    genre_id:   Mapped[int] = mapped_column()
    priority:   Mapped[int] = mapped_column(nullable=True)
'''