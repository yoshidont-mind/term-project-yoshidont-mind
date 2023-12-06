from unittest import TestCase
from unittest.mock import patch

from battle import run_success


class TestRunSuccess(TestCase):
    @patch('random.randint', return_value=18)
    def test_run_success(self, _):
        foe = {'Level': 10}
        my_pokemon = {'Level': 15}
        actual = run_success(foe, my_pokemon)
        expected = True
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=25)
    def test_run_fail(self, _):
        foe = {'Level': 10}
        my_pokemon = {'Level': 4}
        actual = run_success(foe, my_pokemon)
        expected = False
        self.assertEqual(actual, expected)
