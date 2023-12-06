from unittest import TestCase
from unittest.mock import patch

from battle import pokemon_catch


class TestPokemonCatch(TestCase):
    @patch('random.randint', return_value=1)
    def test_hp_ratio_of_foe_is_smallest_and_catch_success(self, _):
        foe = {'HP': 1, 'Max HP': 10}
        actual = pokemon_catch(foe)
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=20)
    def test_hp_ratio_of_foe_is_middle_and_catch_success(self, _):
        foe = {'HP': 5, 'Max HP': 10}
        actual = pokemon_catch(foe)
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=10)
    def test_hp_ratio_of_foe_is_largest_and_catch_success(self, _):
        foe = {'HP': 10, 'Max HP': 10}
        actual = pokemon_catch(foe)
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=81)
    def test_hp_ratio_of_foe_is_smallest_and_catch_fail(self, _):
        foe = {'HP': 1, 'Max HP': 8}
        actual = pokemon_catch(foe)
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=51)
    def test_hp_ratio_of_foe_is_middle_and_catch_fail(self, _):
        foe = {'HP': 5, 'Max HP': 10}
        actual = pokemon_catch(foe)
        expected = False
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=11)
    def test_hp_ratio_of_foe_is_largest_and_catch_fail(self, _):
        foe = {'HP': 10, 'Max HP': 10}
        actual = pokemon_catch(foe)
        expected = False
        self.assertEqual(actual, expected)
