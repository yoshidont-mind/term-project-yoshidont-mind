import io
from unittest import TestCase
from unittest.mock import patch

from battle import determine_level_up


class Test(TestCase):
    def test_no_level_up(self):
        pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                   'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        determine_level_up(pokemon)
        actual = pokemon['Level']
        expected = 5
        self.assertEqual(actual, expected)

    def test_level_up_once(self):
        pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                   'Defense': 11, 'Exp to next level': -5, 'Exp': 0}
        determine_level_up(pokemon)
        actual = pokemon['Level']
        expected = 6
        self.assertEqual(actual, expected)

    def test_level_up_more_than_once(self):
        pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                   'Defense': 11, 'Exp to next level': -300, 'Exp': 0}
        determine_level_up(pokemon)
        actual = pokemon['Level']
        expected = 7
        self.assertEqual(actual, expected)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_prints(self, mock_output):
        pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                   'Defense': 11, 'Exp to next level': -5, 'Exp': 0}
        determine_level_up(pokemon)
        actual = mock_output.getvalue()
        expected = 'Bulbasaur looks stronger!'
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_no_level_up_prints(self, mock_output):
        pokemon = {'Number': 1, 'Name': 'Bulbasaur', 'Level': 5, 'Max HP': 22, 'HP': 22, 'Attack': 11,
                   'Defense': 11, 'Exp to next level': 5, 'Exp': 0}
        determine_level_up(pokemon)
        actual = mock_output.getvalue()
        not_expected = 'Bulbasaur looks stronger!'
        self.assertNotIn(not_expected, actual)
