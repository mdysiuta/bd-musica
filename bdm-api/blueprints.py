from flask import Blueprint, request

from models import db, Artist
from util import create_slug

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

@artists.post("/artist")
def add_artist():
    data = request.json

    print(data)

    artist = Artist(
        name = data["name"]
    )

    slug = create_slug(str(artist.name))

    # Verificar si existe artista con el slug creado.
    # Si existe, incrementar el contador por uno.
    # Pegar el valor del contador al slug original para crear un nuevo slug.
    # Verificar si existe un artista con ese nuevo slug y si lo hay, repetir
    # el proceso hasta que la consulta no devuelva una fila.
    query = db.select(Artist).filter_by(slug=slug)
    existingArtist = db.session.execute(query).scalar()

    count = 0

    if(existingArtist == None):
        artist.slug = slug
    else:
        while (existingArtist != None):
            count += 1
            newSlug = slug + "-" + str(count)
            query = db.select(Artist).filter_by(slug=newSlug)
            existingArtist = db.session.execute(query).scalar()
            if (existingArtist == None):
                artist.slug = newSlug

    db.session.add(artist)
    db.session.commit()

    return {
        "name": artist.name,
        "slug": artist.slug
    }