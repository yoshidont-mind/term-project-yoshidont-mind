from unittest import TestCase
from unittest.mock import mock_open, patch
import json

from game import save_data_as_json


class TestSaveDataAsJson(TestCase):
    def test_save_data(self):
        mock_character = {'Name': 'Ash', 'Pokemon': [{'Name': 'Pikachu'}, {'Name': 'Charmander'}]}
        mock_file = mock_open()

        with patch('builtins.open', mock_file):
            save_data_as_json(mock_character)

        written_data = ''.join(args[0] for args, _ in mock_file().write.call_args_list)
        self.assertEqual(written_data, json.dumps(mock_character))
