import io
from unittest import TestCase
from unittest.mock import patch

from event import go_home


class TestGoHome(TestCase):
    @patch('builtins.input', return_value='')
    def test_potion_are_lost(self, _):
        character = {'Name': 'Tats', 'Location': (5, 8), 'Pokemon': {}, 'Item': {'Potion': 1}}
        go_home(character)
        actual = character['Item']['Potion']
        expected = 0
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='')
    def test_poke_ball_are_lost(self, _):
        character = {'Name': 'Tats', 'Location': (5, 8), 'Pokemon': {}, 'Item': {'Poke Ball': 1}}
        go_home(character)
        actual = character['Item']['Poke Ball']
        expected = 0
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='')
    def test_location_is_changed(self, _):
        character = {'Name': 'Tats', 'Location': (5, 8), 'Pokemon': {}, 'Item': {'Poke Ball': 1}}
        go_home(character)
        actual = character['Location']
        expected = (15, 1)
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='')
    def test_message_is_printed(self, _, mock_output):
        character = {'Name': 'Tats', 'Location': (5, 8), 'Pokemon': {}, 'Item': {'Poke Ball': 1}}
        go_home(character)
        actual = mock_output.getvalue()
        expected = "You rush your home...\n"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='')
    def test_event_home_is_called(self, _, mock_output):
        character = {'Name': 'Tats', 'Location': (5, 8), 'Pokemon': {}, 'Item': {'Poke Ball': 1}}
        go_home(character)
        actual = mock_output.getvalue()
        expected = "Mon \"Take care of yourself, Tats.\"\n"
        self.assertIn(expected, actual)
