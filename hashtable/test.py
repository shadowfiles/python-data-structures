from hashtable import hashtable
import unittest

class test_hashtable(unittest.TestCase):
    CASES = 100
    def setUp(self):
        self.table = hashtable()

    def test_size_basic(self):
        for i in range(1, self.CASES + 1):
            self.table.add(chr(i), i)
            self.assertEqual(i, self.table.size)

    def test_duplicates(self):
        for i in range(self.CASES):
            self.table.add('a', i)
            self.assertEqual(i, self.table.get('a'))
            self.assertEqual(1, self.table.size)

    def test_get_basic(self):
        for i in range(1, self.CASES + 1):
            self.assertEqual(None, self.table.get(chr(i)))
            self.table.add(chr(i), i)
            self.assertEqual(i, self.table.size)
            self.assertEqual(i, self.table.get(chr(i)))

if __name__ == "__main__":
    unittest.main()
