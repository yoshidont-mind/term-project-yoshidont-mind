import io
from unittest import TestCase
from unittest.mock import patch

from event import adventure_preparation


class TestAdventurePreparation(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_trainer_rank_is_one_or_greater(self, mock_output):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}], 'Trainer rank': 1}
        adventure_preparation(character)
        expected = "\nDr.Nabil \"Hi Ash!\"\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('event.gather_user_choice_for_fist_pokemon', return_value='4')
    @patch('builtins.input', return_value='')
    def test_pokemon_is_appended(self, _, __):
        character = {'Name': 'Ash', 'Pokemon': [], 'Item': {'Potion': 0, 'Poke Ball': 0}, 'Trainer rank': 0}
        adventure_preparation(character)
        expected = 'Pikachu'
        actual = character['Pokemon'][0]['Name']
        self.assertEqual(expected, actual)

    @patch('event.gather_user_choice_for_fist_pokemon', return_value='4')
    @patch('builtins.input', return_value='')
    def test_potions_are_added(self, _, __):
        character = {'Name': 'Ash', 'Pokemon': [], 'Item': {'Potion': 0, 'Poke Ball': 0}, 'Trainer rank': 0}
        adventure_preparation(character)
        expected = 3
        actual = character['Item']['Potion']
        self.assertEqual(expected, actual)

    @patch('event.gather_user_choice_for_fist_pokemon', return_value='4')
    @patch('builtins.input', return_value='')
    def test_poke_balls_are_added(self, _, __):
        character = {'Name': 'Ash', 'Pokemon': [], 'Item': {'Potion': 0, 'Poke Ball': 0}, 'Trainer rank': 0}
        adventure_preparation(character)
        expected = 5
        actual = character['Item']['Poke Ball']
        self.assertEqual(expected, actual)

    @patch('event.gather_user_choice_for_fist_pokemon', return_value='4')
    @patch('builtins.input', return_value='')
    def test_trainer_rank_is_increased(self, _, __):
        character = {'Name': 'Ash', 'Pokemon': [], 'Item': {'Potion': 0, 'Poke Ball': 0}, 'Trainer rank': 0}
        adventure_preparation(character)
        expected = 1
        actual = character['Trainer rank']
        self.assertEqual(expected, actual)

    @patch('event.gather_user_choice_for_fist_pokemon', return_value='4')
    @patch('builtins.input', return_value='')
    def test_next_goal_is_updated(self, _, __):
        character = {'Name': 'Ash', 'Pokemon': [], 'Item': {'Potion': 0, 'Poke Ball': 0}, 'Trainer rank': 0}
        adventure_preparation(character)
        expected = "Let's catch two more Pokémon and go to Lion Gate Bridge!"
        actual = character['Next goal']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('event.gather_user_choice_for_fist_pokemon', return_value='4')
    @patch('builtins.input', return_value='')
    def test_message_is_printed(self, _, __, mock_output):
        character = {'Name': 'Ash', 'Pokemon': [], 'Item': {'Potion': 0, 'Poke Ball': 0}, 'Trainer rank': 0}
        adventure_preparation(character)
        expected = "Dr.Nabil \"Now, you're ready to go on an adventure!\"\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
