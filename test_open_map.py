import io
from unittest import TestCase
from unittest.mock import patch

from game import open_map


class TestOpenMap(TestCase):
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_open_map(self, mock_output, _):
        map_dic = {(0, 0): '.', (0, 1): '.', (1, 0): '.', (1, 1): '.'}
        character = {'Location': (0, 0)}
        open_map(map_dic, character)
        actual_output = mock_output.getvalue()
        expected_output = '★ \n..\nNow, you are at "★".\n\n'
        self.assertEqual(expected_output, actual_output)
