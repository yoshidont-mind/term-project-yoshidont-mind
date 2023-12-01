from unittest import TestCase

from game import move_character


class TestMoveCharacter(TestCase):
    def test_move_character(self):
        character = {'Location': (15, 1)}
        direction = '4'
        expected = {'Location': (16, 1)}
        move_character(character, direction)
        self.assertEqual(expected, character)
