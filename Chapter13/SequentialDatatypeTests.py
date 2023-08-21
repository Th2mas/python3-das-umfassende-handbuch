import unittest


class SequentialDatatypeTests(unittest.TestCase):
    def test_in_operator(self):
        elements = ["one", 2, 3.0, "four", 5, "six"]
        self.assertTrue("one" in elements)

    def test_not_in_operator(self):
        elements = ["one", 2, 3.0, "four", 5, "six"]
        self.assertTrue(7 not in elements)

    def test_in_operator_on_string(self):
        self.assertTrue("t" in "test")

    def test_in_operator_does_not_check_for_sub_lists(self):
        elements = ["one", 2, 3.0, "four", 5, "six"]
        other_elements = [2, 3.0]
        self.assertFalse(other_elements in elements)

    def test_list_concatenation(self):
        a = [1, 2]
        b = [3, 4]

        c = a + b
        self.assertEqual([1, 2, 3, 4], c)
        a += b
        self.assertEqual(a, c)

    def test_list_repetition_operator(self):
        a = [1, 2]
        b = 3 * a

        self.assertEqual([1, 2, 1, 2, 1, 2], b)

    def test_list_repetition_operator_on_strings(self):
        c = "ho"
        c *= 3

        self.assertEqual("hohoho", c)

    def test_indexing_operator_with_negative_numbers(self):
        a = [1, 2, 3, 4, 5, 6]
        self.assertEqual(4, a[-3])

    def test_indexing_operator_out_of_bounds(self):
        name = "Python"
        with self.assertRaises(IndexError):
            blank = name[1000]
