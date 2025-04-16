def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")  # versión temporal
    return cleaned == cleaned[::-1]
