from hashtable import hashtable
import unittest

class test_hashtable(unittest.TestCase):
    CASES = 100
    BIG_CASES = 10000
    def setUp(self):
        self.table = hashtable()

    def test_size_basic(self):
        for i in range(1, self.CASES + 1):
            self.table.add(chr(i), i)
            self.assertEqual(i, self.table.size)

    def test_size_large(self):
        cases = self.BIG_CASES
        for i in range(1, cases + 1):
            self.table.add(chr(i), i)
            self.assertEqual(i, self.table.size)

    def test_size_remove(self):
        for i in range(1, self.CASES + 1):
            self.table.add(chr(i), i)
            self.assertEqual(i, self.table.size)

        for i in range(1, self.CASES + 1):
            self.assertEqual(i, self.table.remove(chr(i)))
            self.assertEqual(self.CASES - i, self.table.size)

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

    def test_unhashable(self):
        with self.assertRaises(NotImplementedError):
            self.table.add([1, 2, 3], "This should fail")

    def test_iterator(self):
        keys = set()
        for i in range(1, self.CASES + 1):
            self.table.add(chr(i), i)
            self.assertEqual(i, self.table.size)
            keys.add(chr(i))

        for key in self.table:
            self.assertTrue(key in keys)
            keys.remove(key)
            self.assertEqual(self.CASES, self.table.size)

        self.assertEqual(0, len(keys))

    def test_plus_basic(self):
        keys = set()
        table2 = hashtable()
        for i in range(1, self.CASES + 1):
            self.table.add(chr(i), i)
            table2.add(chr(self.CASES + i), self.CASES + i)

            keys.add(chr(i))
            keys.add(chr(self.CASES + i))

        self.assertEqual(self.CASES, self.table.size)

        self.table += table2

        self.assertEqual(self.CASES * 2, self.table.size)

        for key in self.table:
            self.assertTrue(key in keys)
            keys.remove(key)
            self.assertEqual(self.CASES * 2, self.table.size)

        self.assertEqual(0, len(keys))

    def test_plus_duplicate(self):
        keys = set()
        table2 = hashtable()
        for i in range(1, self.CASES + 1):
            self.table.add(chr(i), i)
            table2.add(chr(i), self.CASES - i)
            keys.add(chr(i))

        self.table += table2

        for key in self.table:
            self.assertTrue(key in keys)
            keys.remove(key)
            self.assertEqual(self.CASES, self.table.size)

        self.assertEqual(0, len(keys))

if __name__ == "__main__":
    unittest.main()
