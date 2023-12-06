import io
from unittest import TestCase
from unittest.mock import patch

from event import event


class TestEvent(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_corresponding_event_is_invoked(self, mock_output):
        character = {'Name': 'Tats', 'Location': (5, 9), 'Trainer rank': 2}
        expected = "\nConstruction Worker Sam \"Hi Tats!\"\n"
        event(character)
        actual = mock_output.getvalue()
        self.assertIn(expected, actual)
