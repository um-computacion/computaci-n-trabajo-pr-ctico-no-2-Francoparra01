def is_palindrome(text):
    """Verifica si el texto es un palíndromo, ignorando mayúsculas, espacios y signos de puntuación."""
    # La función ahora depende de una implementación de limpieza de texto externa
    # Limpieza de texto se implementará en el siguiente Issue
    pass



import string

def clean_text(text):
    """Elimina espacios, puntuación y convierte a minúsculas."""
    return ''.join(
        char.lower() for char in text if char.isalnum()
    )

