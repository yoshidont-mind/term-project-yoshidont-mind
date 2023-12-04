import io
from unittest import TestCase
from unittest.mock import patch

from event import bcit_pokemon_gym


class TestBcitPokemonGym(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_when_trainer_already_has_the_badge(self, mock_output):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}], 'Trainer rank': 3, 'Item': {'BCIT Gym Badge': 1}}
        bcit_pokemon_gym(character)
        expected = "\nGym Leader Rahul \"Hey Ash, how are you doing?\"\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='')
    def test_message_when_number_of_pokemon_is_less_than_five(self, _, mock_output):
        character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}], 'Trainer rank': 2, 'Location': (5, 9), 'Item': {}}
        bcit_pokemon_gym(character)
        expected = "\nReceptionist \"You need to bring at least five Pokémon with you to challenge the Gym Leader.\"\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('battle.battle_with_trainer', return_value=True)
    @patch('builtins.input', return_value='')
    def test_bcit_gym_badge_when_win_the_battle(self, _, __):
        character = {'Name': 'Ash', 'Trainer rank': 2, 'Item': {},
                     'Pokemon': [{'Name': 'Pikachu'},
                                 {'Name': 'Charmander'},
                                 {'Name': 'Squirtle'},
                                 {'Name': 'Bulbasaur'},
                                 {'Name': 'Eevee'}
                                 ]}
        bcit_pokemon_gym(character)
        expected = 1
        actual = character['Item']['BCIT Gym Badge']
        self.assertEqual(expected, actual)

    @patch('battle.battle_with_trainer', return_value=True)
    @patch('builtins.input', return_value='')
    def test_trainer_rank_when_win_the_battle(self, _, __):
        character = {'Name': 'Ash', 'Trainer rank': 2, 'Item': {},
                     'Pokemon': [{'Name': 'Pikachu'},
                                 {'Name': 'Charmander'},
                                 {'Name': 'Squirtle'},
                                 {'Name': 'Bulbasaur'},
                                 {'Name': 'Eevee'}
                                 ]}
        bcit_pokemon_gym(character)
        expected = 3
        actual = character['Trainer rank']
        self.assertEqual(expected, actual)

    @patch('battle.battle_with_trainer', return_value=True)
    @patch('builtins.input', return_value='')
    def test_next_goal_when_win_the_battle(self, _, __):
        character = {'Name': 'Ash', 'Trainer rank': 2, 'Item': {},
                     'Pokemon': [{'Name': 'Pikachu'},
                                 {'Name': 'Charmander'},
                                 {'Name': 'Squirtle'},
                                 {'Name': 'Bulbasaur'},
                                 {'Name': 'Eevee'}
                                 ]}
        bcit_pokemon_gym(character)
        expected = "Let's explore this world, and eventually go to Cypress Mountain!"
        actual = character['Next goal']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.battle_with_trainer', return_value=True)
    @patch('builtins.input', return_value='')
    def test_message_when_win_the_battle(self, _, __, mock_output):
        character = {'Name': 'Ash', 'Trainer rank': 2, 'Item': {},
                     'Pokemon': [{'Name': 'Pikachu', 'HP': 10, 'Max HP': 15},
                                 {'Name': 'Charmander', 'HP': 10, 'Max HP': 15},
                                 {'Name': 'Squirtle', 'HP': 10, 'Max HP': 15},
                                 {'Name': 'Bulbasaur', 'HP': 10, 'Max HP': 15},
                                 {'Name': 'Eevee', 'HP': 10, 'Max HP': 15}
                                 ]}
        bcit_pokemon_gym(character)
        expected = "Gym Leader Rahul \"I'm totally defeated. Please take this Gym Badge.\"\n"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('battle.battle_with_trainer', return_value=False)
    @patch('builtins.input', return_value='')
    def test_when_lose_the_battle(self, _, __):
        character = {'Name': 'Ash', 'Trainer rank': 2, 'Item': {}, 'Location': (5, 9),
                     'Pokemon': [{'Name': 'Pikachu', 'HP': 10, 'Max HP': 15},
                                 {'Name': 'Charmander', 'HP': 10, 'Max HP': 15},
                                 {'Name': 'Squirtle', 'HP': 10, 'Max HP': 15},
                                 {'Name': 'Bulbasaur', 'HP': 10, 'Max HP': 15},
                                 {'Name': 'Eevee', 'HP': 10, 'Max HP': 15}
                                 ]}
        bcit_pokemon_gym(character)
        expected = (15, 1)
        actual = character['Location']
        self.assertEqual(expected, actual)
