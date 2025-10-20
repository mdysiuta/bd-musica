def create_slug(string : str) -> str :
    """
    Devuelve un slug creado a partir de un string para usar en URLs.
    """
    newString = string

    from data import slugForbiddenSymbols

    # Remover y reemplazar símbolos no permitidos en el slug
    for symbol in slugForbiddenSymbols:
        newString = newString.replace(
            symbol.get("symbol"),
            symbol.get("replace-with"))

    newString = newString.lower()

    return newString

def generate_slug(string : str, model) -> str :
    """
    Generar un slug único para un dato. Un número se agrega a un slug generado
    si se encuentran repeticiones dentro de una tabla.
    """
    slug = create_slug(string)

    from models import db

    # contador para datos encontrados en las consultas
    resultsFound = 0

    query = db.select(model).filter_by(slug=slug)
    result = db.session.execute(query).scalar()

    if (result == None):
        return slug
    else:
        while (result != None):
            resultsFound += 1
            newSlug = slug + "-" + str(resultsFound)

            # verificar existencia de un dato que contiene el slug nuevo
            query = db.select(model).filter_by(slug=newSlug)
            result = db.session.execute(query).scalar()

            if (result == None):
                return newSlug

def filter_artist_query(query, request):
    """
    Devuelve una consulta filtrada a partir de parametros entregados a través
    de una URL.
    """
    if request.values.get("name") != None:
        query = query.filter_by(name=request.values.get("name"))

    return query

def filter_genre_query(query, request):
    """
    Devuelve una consulta filtrada a partir de parametros entregados a través
    de una URL.
    """
    if request.values.get("name") != None:
        query = query.filter_by(name=request.values.get("name"))
    
    if request.values.get("top") != None:
        if request.values.get("top") == 1:
            query = query.filter_by(top=True)
    
    return query