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




    cleaned = clean_text(text)  # Limpiamos el texto

    # Comparación de caracteres: comparamos el primer carácter con el último, el segundo con el penúltimo, etc.
    for i in range(len(cleaned) // 2):  # Solo necesitamos iterar hasta la mitad del texto
        if cleaned[i] != cleaned[-(i + 1)]:  # Comparar desde los extremos hacia el centro
            return False  # Si alguna comparación falla, no es un palíndromo

    return True  # Si todas las comparaciones son correctas, es un palíndromo
