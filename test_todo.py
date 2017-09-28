from todo import Controller
import unittest

class TestController(unittest.TestCase):
     def test_print(self):
        self.assertEqual(Print().lets_print(), "")


if __name__ == '__main__':
    unittest.main()
