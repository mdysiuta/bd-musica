def create_slug(string : str) -> str :
    newString = string

    newString = newString.replace(" ", "-")
    newString = newString.replace(".", "_")
    newString = newString.replace("/", "_")
    newString = newString.replace("'", "")
    newString = newString.replace("\"", "")
    newString = newString.replace("[", "")
    newString = newString.replace("]", "")
    newString = newString.lower()

    return newString

# Verificar si existe artista con el slug creado.
# Si existe, incrementar el contador por uno.
# Pegar el valor del contador al slug original para crear un nuevo slug.
# Verificar si existe un artista con ese nuevo slug y si lo hay, repetir
# el proceso hasta que la consulta no devuelva una fila.
def generate_slug(string : str, model) -> str :
    slug = create_slug(string)

    from models import db

    query = db.select(model).filter_by(slug=slug)
    result = db.session.execute(query).scalar()

    count = 0

    if (result == None):
        return slug
    else:
        while (result != None):
            count += 1
            newSlug = slug + "-" + str(count)
            query = db.select(model).filter_by(slug=newSlug)
            result = db.session.execute(query).scalar()
            if (result == None):
                return newSlug

def create_genre_dict(genre):
    return {
        "id": genre.id,
        "name": genre.name,
        "top":  genre.top,
        "slug": genre.slug
    }