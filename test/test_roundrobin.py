import unittest

from collection import RoundRobinArray


class TestRoundRobin(unittest.TestCase):
    def test_correct_order(self):
        arr = (1, 2, 3, 4)
        obj = RoundRobinArray(arr)
        self.assertEqual(obj.get(), arr[0])
        self.assertEqual(obj.get(), arr[1])
        self.assertEqual(obj.get(), arr[2])
        self.assertEqual(obj.get(), arr[3])
        self.assertEqual(obj.get(), arr[0])


if __name__ == '__main__':
    unittest.main()
