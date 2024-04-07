import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_evaluate_guess(self):
        """
        try a few edge-casey cases
        """
        self.assertEqual(main.evaluate_guess('keeps', 'abbey'), ['grey', 'yellow', 'grey', 'grey',
                                                                 'grey'])  # to check for repeating letters


if __name__ == '__main__':
    unittest.main()
