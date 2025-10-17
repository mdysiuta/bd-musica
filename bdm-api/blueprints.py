from flask import Blueprint, request

from models import db, Artist

artists = Blueprint("artists", __name__)

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