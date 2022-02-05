# python randomgametest.py

import unittest
import randomgame


class TestGame(unittest.TestCase):
    def test_input(self):
        result = randomgame.run_guess(5, 5)
        self.assertTrue(result)

    def test_inpu_wrong_guess(self):
        result = randomgame.run_guess(5, 0)
        self.assertFalse(result)

    def test_inpu_wrong_number(self):
        result = randomgame.run_guess(5, 11)
        self.assertFalse(result)

    def test_inpu_wrong_type(self):
        result = randomgame.run_guess(5, '11')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
