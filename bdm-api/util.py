def create_slug(string : str) -> str :
    newString = string

    newString = newString.replace(" ", "-")
    newString = newString.replace(".", "_")
    newString = newString.replace("/", "_")
    newString = newString.replace("'", "")
    newString = newString.replace("\"", "")
    newString = newString.lower()

    return newString