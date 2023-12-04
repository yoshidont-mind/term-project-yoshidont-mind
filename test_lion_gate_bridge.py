import io
from unittest import TestCase
from unittest.mock import patch

from event import lion_gate_bridge


class TestLionGateBridge(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_trainer_rank_is_two_or_greater(self, mock_output):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}], 'Trainer rank': 2}
        lion_gate_bridge(character)
        expected = "\nConstruction Worker Sam \"Hi Ash!\"\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('builtins.input', return_value='')
    def test_location_when_number_of_pokemon_is_less_than_three(self, _):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}], 'Trainer rank': 1, 'Location': (5, 9)}
        lion_gate_bridge(character)
        expected = (5, 8)
        actual = character['Location']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='')
    def test_location_when_number_of_pokemon_is_less_than_three(self, _, mock_output):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}], 'Trainer rank': 1, 'Location': (5, 9)}
        lion_gate_bridge(character)
        expected = "\"Sorry, you cannot proceed unless you have at least three Pokémon with you.\"\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('battle.battle_with_trainer', return_value=True)
    @patch('builtins.input', return_value='')
    def test_seabus_ticket_when_win_the_battle(self, _, __):
        character = {'Name': 'Ash', 'Trainer rank': 1, 'Item': {},
                     'Pokemon': [{'Name': 'Pikachu'}, {'Name': 'Charmander'}, {'Name': 'Squirtle'}]}
        lion_gate_bridge(character)
        expected = 1
        actual = character['Item']['SeaBus Ticket']
        self.assertEqual(expected, actual)

    @patch('battle.battle_with_trainer', return_value=True)
    @patch('builtins.input', return_value='')
    def test_trainer_rank_when_win_the_battle(self, _, __):
        character = {'Name': 'Ash', 'Trainer rank': 1, 'Item': {},
                     'Pokemon': [{'Name': 'Pikachu'}, {'Name': 'Charmander'}, {'Name': 'Squirtle'}]}
        lion_gate_bridge(character)
        expected = 2
        actual = character['Trainer rank']
        self.assertEqual(expected, actual)

    @patch('battle.battle_with_trainer', return_value=True)
    @patch('builtins.input', return_value='')
    def test_next_goal_when_win_the_battle(self, _, __):
        character = {'Name': 'Ash', 'Trainer rank': 1, 'Item': {},
                     'Pokemon': [{'Name': 'Pikachu'}, {'Name': 'Charmander'}, {'Name': 'Squirtle'}]}
        lion_gate_bridge(character)
        expected = "Let's go to BCIT Pokémon Gym!"
        actual = character['Next goal']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.battle_with_trainer', return_value=True)
    @patch('builtins.input', return_value='')
    def test_message_when_win_the_battle(self, _, __, mock_output):
        character = {'Name': 'Ash', 'Trainer rank': 1, 'Item': {},
                     'Pokemon': [{'Name': 'Pikachu'}, {'Name': 'Charmander'}, {'Name': 'Squirtle'}]}
        lion_gate_bridge(character)
        expected = "\"Passable! Now, you can go to BCIT Pokémon Gym!\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('battle.battle_with_trainer', return_value=False)
    @patch('builtins.input', return_value='')
    def test_when_lose_the_battle(self, _, __):
        character = {'Name': 'Ash', 'Trainer rank': 1, 'Item': {}, 'Location': (5, 9),
                     'Pokemon': [{'Name': 'Pikachu', 'HP': 10, 'Max HP': 15},
                                 {'Name': 'Charmander', 'HP': 10, 'Max HP': 15},
                                 {'Name': 'Squirtle', 'HP': 10, 'Max HP': 15}]}
        lion_gate_bridge(character)
        expected = (15, 1)
        actual = character['Location']
        self.assertEqual(expected, actual)
