from unittest import TestCase
from unittest.mock import patch
from io import StringIO

from game import describe_current_location, generate_map_dictionary


class TestDescribeCurrentLocation(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_corner(self, mock_output):
        character = {'Location': (1, 1)}
        map_dic = generate_map_dictionary()
        describe_current_location(map_dic, character)
        actual = mock_output.getvalue().strip()
        expected = '▓▓▓▓▓▓▓▓\n▓★  #...\n▓## #...\n▓   #...\n▓!######\nNow, you are at "★".'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_edge(self, mock_output):
        character = {'Location': (1, 3)}
        map_dic = generate_map_dictionary()
        describe_current_location(map_dic, character)
        actual = mock_output.getvalue().strip()
        expected = '▓▓▓▓▓▓▓▓\n▓!  #...\n▓## #...\n▓★  #...\n▓!######\n▓       \n▓.... ..\nNow, you are at "★".'
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=StringIO)
    def test_middle(self, mock_output):
        character = {'Location': (8, 3)}
        map_dic = generate_map_dictionary()
        describe_current_location(map_dic, character)
        actual = mock_output.getvalue().strip()
        expected = ('▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n!  #.........#\n## #.........#\n   #...★.....#\n!##########i##\n              '
                    '\n.... ........!\nNow, you are at "★".')
        self.assertEqual(expected, actual)
