from flask import Blueprint, request

from models import db, Artist, Genre
from util import create_slug, generate_slug, create_genre_dict

artists = Blueprint("artists", __name__)
genres = Blueprint("genres", __name__)

@artists.route("/artists")
def artist_list():
    query = db.select(Artist)

    # Filtros
    if request.values.get("name") != None:
        query = query.filter_by(name=request.values.get("name"))

    artists = db.session.execute(query).scalars()

    return [{
        "id": artist.id,
        "name": artist.name
    } for artist in artists]

@artists.get("/artist/<int:id>")
def artist_detail(id):
    query = db.select(Artist).filter_by(id=id)
    artist = db.session.execute(query).scalar()

    return {
        "id": artist.id,
        "name": artist.name
    }

@artists.post("/artist")
def add_artist():
    data = request.json

    artist = Artist(
        name = data["name"]
    )

    artist.slug = generate_slug(str(data["name"]), Artist)

    db.session.add(artist)
    db.session.commit()

    return {
        "name": artist.name,
        "slug": artist.slug
    }

@genres.get("/genres")
def genre_list():
    query = db.select(Genre)

    # Filtros
    if request.values.get("name") != None:
        query = query.filter_by(name=request.values.get("name"))
    
    if request.values.get("top") != None:
        if request.values.get("top") == 1:
            query = query.filter_by(top=True)

    genres = db.session.execute(query).scalars()

    return [{
        "id": genre.id,
        "name": genre.name
    } for genre in genres]

@genres.get("/genre/<int:id>")
def genre_detail_id(id):
    query = db.select(Genre).filter_by(id=id)
    genre = db.session.execute(query).scalar()

    return create_genre_dict(genre)

@genres.get("/genre/<string:slug>")
def genre_detail_slug(slug):
    query = db.select(Genre).filter_by(slug=slug)
    genre = db.session.execute(query).scalar()

    return create_genre_dict(genre)

@genres.post("/genre")
def add_genre():
    data = request.json

    parentNameList = data["parents"]
    parents = []

    for parentName in parentNameList:
        query = db.select(Genre).filter_by(name=parentName)
        parentObj = db.session.execute(query).scalar()
        parents.append(parentObj)

    genre = Genre(
        name    = data["name"],
        top     = data["top"],
        parents = parents
    )

    genre.slug = generate_slug(str(data["name"]), Genre)

    db.session.add(genre)
    db.session.commit()

    return {
        "name":    genre.name,
        "top":     genre.top,
        "slug":    genre.slug,
        "parents": [parent.name for parent in genre.parents],
    }