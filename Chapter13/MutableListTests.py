import unittest


class MutableListTests(unittest.TestCase):
    def test_list_replace_element(self):
        l = [1, 2, 3, 4]
        self.assertEqual(2, l[1])

        l[1] = 1000
        self.assertEqual(1000, l[1])

    def test_list_replace_sublist(self):
        groceries = ["Bread", "Milk", "Eggs", "Apples", "Water"]
        self.assertEqual(["Bread", "Milk"], groceries[0:2])

        groceries[0:2] = ["Cucumber", "Oats"]
        self.assertEqual(["Cucumber", "Oats"], groceries[0:2])
        self.assertEqual(["Cucumber", "Oats", "Eggs", "Apples", "Water"], groceries)

    def test_list_replace_sublist_with_less_elements(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        l[1:5] = [5, 4, 3]

        self.assertEqual([1, 5, 4, 3, 6, 7, 8, 9], l)

    def test_list_remove_sublist(self):
        l = [1, 2, 3, 4, 5]

        l[0:3] = []

        self.assertEqual([4, 5], l)

    def test_list_replace_with_step_size(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        l[0:9:3] = ['A', 'B', 'C']

        self.assertEqual(['A', 2, 3, 'B', 5, 6, 'C', 8, 9], l)

    def test_list_replace_with_step_size_throws_value_error_if_right_side_has_not_enough_elements(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        with self.assertRaises(ValueError):
            l[0:9:2] = ['A', 'B']
