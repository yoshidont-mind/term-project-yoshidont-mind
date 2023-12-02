from unittest import TestCase
from unittest.mock import patch

from event import check_for_wild_pokemon


class TestCheckForWildPokemon(TestCase):
    @patch('random.randint', return_value=1)
    def test_smallest_number(self, _):
        actual = check_for_wild_pokemon()
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=25)
    def test_largest_number_results_in_true(self, _):
        actual = check_for_wild_pokemon()
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=26)
    def test_smallest_number_results_in_false(self, _):
        actual = check_for_wild_pokemon()
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=100)
    def test_largest_number(self, _):
        actual = check_for_wild_pokemon()
        expected = False
        self.assertEqual(actual, expected)
