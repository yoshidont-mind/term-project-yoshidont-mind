from unittest import TestCase
from unittest.mock import patch

from event import event_path


class TestEventPath(TestCase):
    @patch('random.randint', return_value=1)
    def test_found_potion(self, _):
        character = {'Name': 'Tats', 'Item': {'Potion': 0, 'Poke Ball': 0}}
        event_path(character)
        actual = character['Item']['Potion']
        expected = 1
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=12)
    def test_found_poke_ball(self, _):
        character = {'Name': 'Tats', 'Item': {'Potion': 0, 'Poke Ball': 0}}
        event_path(character)
        actual = character['Item']['Poke Ball']
        expected = 1
        self.assertEqual(actual, expected)

    @patch('random.randint', return_value=25)
    def test_nothing_found(self, _):
        character = {'Name': 'Tats', 'Item': {'Potion': 0, 'Poke Ball': 0}}
        event_path(character)
        actual = [character['Item']['Potion'], character['Item']['Poke Ball']]
        expected = [0, 0]
        self.assertEqual(actual, expected)
