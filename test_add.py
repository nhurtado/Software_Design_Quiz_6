import unittest
import main


class TestAddFunction(unittest.TestCase):

    def test_add_functions_exists(self):
        self.assertTrue("add" in dir(main), "Add function does not exist")

    def test_add_receives_numbers_delimited_by_commas(self):
        main.add("1,2,3,1")

    def test_add_correctly(self):
        self.assertEqual(main.add("1,2,3,1"), 7,
                         "incorrect number sum")
        self.assertEqual(main.add("3,4,5"), 12,
                         "incorrect number sum")

    def test_add_allows_number_delimiter(self):
        self.assertEqual(main.add(";1;2;3;1"), 7,
                         "incorrect number sum")
        self.assertEqual(main.add("%4%5%3"), 12,
                         "incorrect number sum")

    def test_add_dismisses_negative_numbers(self):
        self.assertEqual(main.add("1,2,3,-1"), 6,
                         "incorrect number sum")
        self.assertEqual(main.add("%4%5%-3"), 9,
                         "incorrect number sum")


class ExpectedFailureTestCase(unittest.TestCase):

    def test_add_other_types_fail(self):
        with self.assertRaises(TypeError):
            main.add(1)
            main.add({})
            main.add([1, 2, 3])

    def test_add_chars_in_list_fail(self):
        with self.assertRaises(ValueError):
            main.add('A,B,C')

    def test_add_different_delimiters_fail(self):
        with self.assertRaises(ValueError):
            main.add(";1.2&3'1")


if __name__ == '__main__':
    unittest.main()
