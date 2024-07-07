#Valida si los campos requeridos no se encuentran vacios
def validate_form(form, required_fields):
    for field in required_fields:
        if not form.get(field):
            return False
    return True