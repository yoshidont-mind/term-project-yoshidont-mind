import io
from unittest import TestCase
from unittest.mock import patch

from game import check_status


class TestCheckStatus(TestCase):
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_pokemon(self, mock_output, _):
        character = {"Name": "Tats",
                     "Location": [7, 6],
                     "Pokemon": [],
                     "Item": {"Potion": 4, "Poke Ball": 3, "SeaBus Ticket": 1, "BCIT Gym Badge": 1},
                     "Trainer rank": 3,
                     "Next goal": "Let's explore this world, and eventually go to Cypress Mountain!",
                     "End roll": True}
        expected = ("\n--------------------\nName        : Tats\nTrainer rank: 3\nNext goal   : Let's explore this "
                    "world, and eventually go to Cypress Mountain!\n\nItem:\n - Potion: 4\n - Poke Ball: 3\n - SeaBus "
                    "Ticket: 1\n - BCIT Gym Badge: 1\n\n--------------------\nPokemon:\n--------------------\n\n")
        check_status(character)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_with_pokemon(self, mock_output, _):
        character = {"Name": "Tats",
                     "Location": [7, 6],
                     "Pokemon": [{"Number": 1,
                                  "Name": "Bulbasaur",
                                  "Level": 9,
                                  "Max HP": 31,
                                  "HP": 0,
                                  "Attack": 18,
                                  "Defense": 18,
                                  "Exp to next level": 218,
                                  "Exp": 365},
                                 {"Number": 2,
                                  "Name": "Charmander",
                                  "Level": 10,
                                  "Max HP": 32,
                                  "HP": 25,
                                  "Attack": 20,
                                  "Defense": 18,
                                  "Exp to next level": 13,
                                  "Exp": 787}],
                     "Item": {"Potion": 4, "Poke Ball": 3, "SeaBus Ticket": 1, "BCIT Gym Badge": 1},
                     "Trainer rank": 3,
                     "Next goal": "Let's explore this world, and eventually go to Cypress Mountain!",
                     "End roll": True}
        expected = ("\n--------------------\nName        : Tats\nTrainer rank: 3\nNext goal   : Let's explore this "
                    "world, and eventually go to Cypress Mountain!\n\nItem:\n - Potion: 4\n - Poke Ball: 3\n - SeaBus "
                    "Ticket: 1\n - BCIT Gym Badge: 1\n\n--------------------\nPokemon:\n1) Bulbasaur\n - Level  "
                    ": 9\n - Exp    : 365 / 583\n - HP     : 0 / 31\n - Attack : 18\n - Defense: 18\n\n2) Charmander"
                    "\n - Level  : 10\n - Exp    : 787 / 800\n - HP     : 25 / 32\n - Attack : 20\n - Defense: 18"
                    "\n\n--------------------\n\n")
        check_status(character)
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)