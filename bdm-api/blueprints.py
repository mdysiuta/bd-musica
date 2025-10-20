from flask import Blueprint, request

from models import db, Artist, Genre
from util import create_slug, generate_slug, filter_artist_query, filter_genre_query, get_genres_from_name_list

artists = Blueprint("artists", __name__)
genres = Blueprint("genres", __name__)

# ARTISTAS ====================================================================

@artists.route("/artists")
def artist_list():
    query = db.select(Artist)
    query = filter_artist_query(query, request)
    artists = db.session.execute(query).scalars()
    return [artist.create_dict() for artist in artists]

@artists.get("/artist/<int:id>")
def artist_detail(id):
    query = db.select(Artist).filter_by(id=id)
    artist = db.session.execute(query).scalar()
    return artist.create_dict()

@artists.post("/artist")
def add_artist():
    data = request.json
    artist = Artist(name = data["name"])
    artist.slug = generate_slug(str(data["name"]), Artist)

    db.session.add(artist)
    db.session.commit()
    
    return artist.create_dict(), 201

# GÉNEROS =====================================================================

@genres.get("/genres")
def genre_list():
    query = db.select(Genre)
    query = filter_genre_query(query, request)
    genres = db.session.execute(query).scalars()
    return [genre.create_dict() for genre in genres]

@genres.get("/genre/<int:id>")
def genre_detail_id(id):
    query = db.select(Genre).filter_by(id=id)
    genre = db.session.execute(query).scalar()
    return genre.create_dict()

@genres.get("/genre/<string:slug>")
def genre_detail_slug(slug):
    query = db.select(Genre).filter_by(slug=slug)
    genre = db.session.execute(query).scalar()
    return genre.create_dict()

@genres.post("/genre")
def add_genre():
    data = request.json

    genre = Genre(
        name      = data["name"],
        top       = data["top"],
        parents   = Genre.get_genres_from_name_list(data["parents"]),
        subgenres = Genre.get_genres_from_name_list(data["subgenres"]),
        slug      = generate_slug(str(data["name"]), Genre)
    )

    db.session.add(genre)
    db.session.commit()

    return genre.create_dict(), 201