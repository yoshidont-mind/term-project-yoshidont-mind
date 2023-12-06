import io
from unittest import TestCase
from unittest.mock import patch

from event import gather_user_choice_for_fist_pokemon


class TestGatherUserChoiceForFistPokemon(TestCase):
    @patch('builtins.input', side_effect=['3', '1'])
    def test_user_choice_is_valid_and_confirmed(self, _):
        expected = '3'
        actual = gather_user_choice_for_fist_pokemon()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3', 'hello world', '2', '1'])
    def test_user_choice_is_valid_and_not_confirmed_at_first(self, _):
        expected = '2'
        actual = gather_user_choice_for_fist_pokemon()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['hello world', '1', '1'])
    def test_user_choice_is_invalid_at_first(self, _):
        expected = '1'
        actual = gather_user_choice_for_fist_pokemon()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['3', 'hello world', '2', '1'])
    def test_print(self, _, mock_output):
        gather_user_choice_for_fist_pokemon()
        expected = "Are you sure to choose Charmander?"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
