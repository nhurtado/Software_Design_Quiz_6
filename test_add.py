import unittest
import main


class TestAddFunction(unittest.TestCase):

    def test_add_exists(self):
        self.assertTrue("add" in dir(main), "Add function does not exist")

    def test_add_receives_strings(self):
        main.add("1,2,3")

if __name__ == '__main__':
    unittest.main()
