import io
from unittest import TestCase
from unittest.mock import patch

from event import granville_island


class TestGranvilleIsland(TestCase):
    @patch('builtins.input', return_value='')
    def test_location_when_character_does_not_have_bcit_gym_badge(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}],
                     'Trainer rank': 1, 'Item': {'Potion': 0, 'Poke Ball': 0},
                     'Location': (15, 21)}
        granville_island(character)
        expected = (15, 21)
        actual = character['Location']
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='')
    def test_location_when_character_has_bcit_gym_badge(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}],
                     'Trainer rank': 1, 'Item': {'Potion': 0, 'Poke Ball': 0, 'BCIT Gym Badge': 1},
                     'Location': (15, 21)}
        granville_island(character)
        expected = (15, 20)
        actual = character['Location']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='')
    def test_location_when_character_does_not_have_bcit_gym_badge(self, _, mock_output):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}],
                     'Trainer rank': 1, 'Item': {'Potion': 0, 'Poke Ball': 0},
                     'Location': (15, 21)}
        granville_island(character)
        expected = "Construction Worker \"Sorry, you cannot proceed further unless you have 'BCIT Gym Badge'.\"\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='')
    def test_location_when_character_has_bcit_gym_badge(self, _, mock_output):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}],
                     'Trainer rank': 1, 'Item': {'Potion': 0, 'Poke Ball': 0, 'BCIT Gym Badge': 1},
                     'Location': (15, 21)}
        granville_island(character)
        expected = "Construction Worker \"Sorry, you cannot proceed further unless you have 'BCIT Gym Badge'.\"\n"
        actual = mock_output.getvalue()
        self.assertNotIn(expected, actual)