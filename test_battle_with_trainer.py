import io
from unittest import TestCase
from unittest.mock import patch

from battle import battle_with_trainer


class TestBattleWithTrainer(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.pokemon_battle', return_value=True)
    @patch('battle.check_alive_pokemon_remains', side_effect=[True, False])
    def test_print_remaining_foe_pokemon(self, _, __, mock_output):
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0},
                                 {'Number': 2, 'Name': 'Charmander', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        trainer = {'Name': 'Gary',
                   'Pokemon': [{'Number': 3, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                'Defense': 11, 'Exp to next level': 5, 'Exp': 0},
                               {'Number': 4, 'Name': 'Pikachu', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        battle_with_trainer(character, trainer)
        expected = "Remaining foe Pokémon: 2"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('battle.pokemon_battle', return_value=True)
    @patch('battle.check_alive_pokemon_remains', side_effect=[True, False])
    def test_print_lets_go_call(self, _, __, mock_output):
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0},
                                 {'Number': 2, 'Name': 'Charmander', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        trainer = {'Name': 'Gary',
                   'Pokemon': [{'Number': 3, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                'Defense': 11, 'Exp to next level': 5, 'Exp': 0},
                               {'Number': 4, 'Name': 'Pikachu', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        battle_with_trainer(character, trainer)
        expected = "Let's go, Bulbasaur!"
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)

    @patch('battle.pokemon_battle', return_value=True)
    @patch('battle.check_alive_pokemon_remains', side_effect=[True, False])
    def win_battle(self, _, __):
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0},
                                 {'Number': 2, 'Name': 'Charmander', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        trainer = {'Name': 'Gary',
                   'Pokemon': [{'Number': 3, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                'Defense': 11, 'Exp to next level': 5, 'Exp': 0},
                               {'Number': 4, 'Name': 'Pikachu', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        actual = battle_with_trainer(character, trainer)
        expected = True
        self.assertEqual(expected, actual)

    @patch('battle.pokemon_battle', return_value=False)
    @patch('battle.check_alive_pokemon_remains', side_effect=[True, False])
    def lose_battle(self, _, __):
        character = {'Name': 'Ash',
                     'Pokemon': [{'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0},
                                 {'Number': 2, 'Name': 'Charmander', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                  'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        trainer = {'Name': 'Gary',
                   'Pokemon': [{'Number': 3, 'Name': 'Squirtle', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                'Defense': 11, 'Exp to next level': 5, 'Exp': 0},
                               {'Number': 4, 'Name': 'Pikachu', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                                'Defense': 11, 'Exp to next level': 5, 'Exp': 0}]}
        actual = battle_with_trainer(character, trainer)
        expected = False
        self.assertEqual(expected, actual)
