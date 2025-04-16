import unittest
from src.palindrome import is_palindrome  # Importas la función que vas a probar

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))

    def test_phrase_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))

    def test_non_palindromes(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))

    def test_edge_cases(self):
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))


def test_phrase_palindromes(self):
    self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
    self.assertTrue(is_palindrome("Anita lava la tina"))
    self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))


def test_edge_cases(self):
    self.assertTrue(is_palindrome(""))  # Cadena vacía
    self.assertTrue(is_palindrome("a"))  # Un solo carácter
    self.assertTrue(is_palindrome(" "))  # Espacio solo
    self.assertTrue(is_palindrome("!@#@!"))  # Caracteres especiales
    self.assertFalse(is_palindrome("ab"))  # No palíndromo de dos letras
