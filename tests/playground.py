import random
from unittest import TestCase


class Playground(TestCase):

    def test_iter(self):
        moves = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        print(moves)
        while len(moves) > 3:
            index_to_remove = random.randint(0, len(moves) - 1)
            moves.pop(index_to_remove)
            print(moves)
