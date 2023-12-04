import io
from unittest import TestCase
from unittest.mock import patch

from event import waterfront


class TestWaterfront(TestCase):
    @patch('builtins.input', return_value='')
    def test_location_when_character_does_not_have_seabus_ticket(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}],
                     'Trainer rank': 1, 'Item': {'Potion': 0, 'Poke Ball': 0},
                     'Location': (14, 14)}
        waterfront(character)
        expected = (14, 14)
        actual = character['Location']
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='')
    def test_location_when_character_has_seabus_ticket(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}],
                     'Trainer rank': 1, 'Item': {'Potion': 0, 'Poke Ball': 0, 'SeaBus Ticket': 1},
                     'Location': (14, 14)}
        waterfront(character)
        expected = (14, 6)
        actual = character['Location']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='')
    def test_location_when_character_does_not_have_seabus_ticket(self, _, mock_output):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}],
                     'Trainer rank': 1, 'Item': {'Potion': 0, 'Poke Ball': 0},
                     'Location': (14, 14)}
        waterfront(character)
        expected = "Clerk at the gate \"Sorry, the SeaBus is out of service, now.\"\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='')
    def test_location_when_character_has_seabus_ticket(self, _, mock_output):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}],
                     'Trainer rank': 1, 'Item': {'Potion': 0, 'Poke Ball': 0, 'SeaBus Ticket': 1},
                     'Location': (14, 14)}
        waterfront(character)
        expected = "Clerk at the gate \"Welcome to SeaBus!\"\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
