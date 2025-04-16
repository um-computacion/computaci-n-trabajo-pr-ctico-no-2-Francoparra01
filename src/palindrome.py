import string

def clean_text(text):
    """Elimina espacios, puntuación y convierte a minúsculas."""
    return ''.join(
        char.lower() for char in text if char.isalnum()
    )

def is_palindrome(text):
    """Verifica si el texto es un palíndromo, ignorando mayúsculas, espacios y signos de puntuación."""
    cleaned = clean_text(text)
    return cleaned == cleaned[::-1]
