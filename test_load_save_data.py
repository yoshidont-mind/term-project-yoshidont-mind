import unittest
from unittest.mock import mock_open, patch
from game import load_save_data


class TestLoadSaveData(unittest.TestCase):
    def test_load_valid_save_data(self):
        mock_data = '{"Name": "Ash", "Location": [15, 1], "Pokemon": []}'
        with patch('builtins.open', mock_open(read_data=mock_data)):
            result = load_save_data()
            self.assertEqual(result, {"Name": "Ash", "Location": (15, 1), "Pokemon": []})

    def test_file_not_found(self):
        with patch('builtins.open', side_effect=FileNotFoundError()):
            result = load_save_data()
            self.assertIsNone(result)

    def test_json_decode_error(self):
        with patch('builtins.open', mock_open(read_data='invalid json')):
            result = load_save_data()
            self.assertIsNone(result)
