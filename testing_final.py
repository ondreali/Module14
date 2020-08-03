
"""
program:testing_fina;
Author: Ondrea Li
Last date modfied: 08/02/20

The purpose of this program is to test the iInal_anagram
"""

import unittest
from Final import Final_anagram as fa


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.is_anagram = 'yellow'
        self.isnot_anagram = 'lemon'
        self.anagram = Final_anagram(self.isnot_anagram)

    def tearDown(self):
        del self.anagram

    def test_constructor(self):
        with self.assertRaises(InvalidWordException):
            self.anagram = Final_Functions(self.word_symbol)



if __name__ == '__main__':
    unittest.main()
