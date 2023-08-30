import unittest

from barkeputils import is_empty, is_not_empty


class TestUtils(unittest.TestCase):
    def test_is_empty_emptyCollectionPassed(self):
        self.assertTrue(is_empty([]))

    def test_is_empty_notEmptyCollectionPassed(self):
        self.assertFalse(is_empty([1]))

    def test_is_not_empty_emptyCollectionPassed(self):
        self.assertFalse(is_not_empty([]))

    def test_is_not_empty_notEmptyCollectionPassed(self):
        self.assertTrue(is_not_empty([1]))


if __name__ == '__main__':
    unittest.main()
