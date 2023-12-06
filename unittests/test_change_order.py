from unittest import TestCase

from game import change_order


class TestChangeOrder(TestCase):
    def test_smallest_number_of_pokemon(self):
        character = {'Pokemon': [{'Name': 'Bulbasaur'}, {'Name': 'Charmander'}]}
        change_order(character, 1)
        expect = {'Pokemon': [{'Name': 'Charmander'}, {'Name': 'Bulbasaur'}]}
        self.assertEqual(expect, character)

    def test_not_smallest_number_of_pokemon_with_smallest_index(self):
        character = {'Pokemon': [{'Name': 'Bulbasaur'}, {'Name': 'Charmander'}, {'Name': 'Squirtle'}]}
        change_order(character, 1)
        expect = {'Pokemon': [{'Name': 'Charmander'}, {'Name': 'Bulbasaur'}, {'Name': 'Squirtle'}]}
        self.assertEqual(expect, character)

    def test_not_smallest_number_of_pokemon_with_middle_index(self):
        character = {'Pokemon': [{'Name': 'Bulbasaur'}, {'Name': 'Charmander'}, {'Name': 'Squirtle'}, {'Name': 'Mew'}]}
        change_order(character, 2)
        expect = {'Pokemon': [{'Name': 'Squirtle'}, {'Name': 'Charmander'}, {'Name': 'Bulbasaur'}, {'Name': 'Mew'}]}
        self.assertEqual(expect, character)

    def test_not_smallest_number_of_pokemon_with_largest_index(self):
        character = {'Pokemon': [{'Name': 'Bulbasaur'}, {'Name': 'Charmander'}, {'Name': 'Squirtle'}, {'Name': 'Mew'}]}
        change_order(character, 3)
        expect = {'Pokemon': [{'Name': 'Mew'}, {'Name': 'Charmander'}, {'Name': 'Squirtle'}, {'Name': 'Bulbasaur'}]}
        self.assertEqual(expect, character)
