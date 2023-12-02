import io
from unittest import TestCase
from unittest.mock import patch

from event import event_information


class TestEventInformation(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='')
    def test_information_displayed(self, _, mock_output):
        character = {'Name': 'Tats', 'Location': (5, 8)}
        user_choice = '1'
        event_information(character, user_choice)
        actual = mock_output.getvalue()
        expected = "\n\"Here is 'Lion Gate Bridge'. The gateway to the world.\"\n"
        self.assertIn(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', return_value='')
    def test_information_not_displayed_because_of_user_input(self, _, mock_output):
        character = {'Name': 'Tats', 'Location': (5, 10)}
        user_choice = '1'
        event_information(character, user_choice)
        actual = mock_output.getvalue()
        expected = "\n\"Here is 'Stanley Park'. Many Pokémon are living here.\"\n"
        self.assertNotIn(expected, actual)
