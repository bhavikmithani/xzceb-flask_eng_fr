from machinetranslation import translator
import unittest


class TestEnglishToFrench(unittest.TestCase):
    def test_e2f_hello(self):
        actual = translator.english_to_french("Hello")
        expected = "Bonjour"
        self.assertEqual(actual, expected)

    def test_e2f_yes(self):
        actual = translator.english_to_french("Yes")
        expected = "Oui"
        self.assertEqual(actual, expected)


class TestFrenchToEnglish(unittest.TestCase):
    def test_f2e_hello(self):
        actual = translator.french_to_english("Bonjour")
        expected = "Hello"
        self.assertEqual(actual, expected)

    def test_f2e_yes(self):
        actual = translator.french_to_english("Oui")
        expected = "Yes"
        self.assertEqual(actual, expected)