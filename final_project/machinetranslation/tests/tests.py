import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Thank'), 'Merci')
        self.assertEqual(english_to_french('My name is Leo'), 'Mon nom est Leo')
        self.assertEqual(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Au revoir')

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Merci'), 'Thank you')
        self.assertEqual(french_to_english('Mon nom est Leo'), 'My name is Leo')
        self.assertEqual(french_to_english(''), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Au revoir'), 'Hello')

unittest.main()