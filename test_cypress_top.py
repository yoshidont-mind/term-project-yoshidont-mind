import io
from unittest import TestCase
from unittest.mock import patch

from event import cypress_top


class TestBcitPokemonGym(TestCase):
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
        cypress_top(character)
        expected = 4
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
        cypress_top(character)
        expected = "You've completed the game! Congratulations! Thank you so much for playing!"
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
        cypress_top(character)
        expected = "The world of Pokémon is still full of mysteries. Continue enjoying your adventure!"
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
        cypress_top(character)
        expected = (15, 1)
        actual = character['Location']
        self.assertEqual(expected, actual)
