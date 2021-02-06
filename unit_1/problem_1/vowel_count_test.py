import unittest

from vowel_count import count_in_substring

class VowelCountTest(unittest.TestCase):
    def test_for_first_and_last(self):
        s = "azcbo"
        expected = 2
        self.assertEqual(count_in_substring(s), expected)

if __name__ == '__main__':
    unittest.main()