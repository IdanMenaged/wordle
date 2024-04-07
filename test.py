import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_evaluate_guess(self):
        """
        try a few edge-casey cases
        """
        self.assertEqual(main.evaluate_guess('keeps', 'abbey'), ['grey', 'yellow', 'grey', 'grey',
                                                                 'grey'])  # to check for repeating letters

    def test_legal_guess(self):
        self.assertTrue(main.legal_guess('slangy', 'rabbit'))
        self.assertFalse(main.legal_guess('banana', 'abbey'))  # too long
        self.assertFalse(main.legal_guess('aaaaa', 'abbey'))  # gibberish
        self.assertFalse(main.legal_guess('ABBEY', 'abbey'))  # upper case


if __name__ == '__main__':
    unittest.main()
