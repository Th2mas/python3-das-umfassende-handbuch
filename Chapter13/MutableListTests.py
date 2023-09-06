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

    def test_del_operator_remove_one_element(self):
        numbers = [1, 2, 3, 4]
        self.assertEqual(numbers[1], 2)
        self.assertEqual(len(numbers), 4)

        del numbers[1]
        self.assertEqual(numbers[1], 3)
        self.assertEqual(len(numbers), 3)

    def test_del_sublist(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        del numbers[1:3]
        self.assertEqual(numbers, [1, 4, 5, 6, 7, 8, 9])

    def test_del_sublist_with_slicing(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        del numbers[::2]
        self.assertEqual(numbers, [1, 3, 5, 7, 9])

    def test_append(self):
        elements = ['Water', 'Earth', 'Fire']

        elements.append('Air')
        self.assertEqual(elements, ['Water', 'Earth', 'Fire', 'Air'])

    def test_extend(self):
        elements = ['Water', 'Earth', 'Fire', 'Air']
        new_elements = ['Metal', 'Lightning', 'Sand']

        elements.extend(new_elements)
        self.assertEqual(elements, ['Water', 'Earth', 'Fire', 'Air', 'Metal', 'Lightning', 'Sand'])

    def test_insert_regular_case(self):
        numbers = [1, 2, 3, 4, 5, 7, 8, 9]
        numbers.insert(0, 0)
        numbers.insert(6, 6)

        self.assertEqual(numbers, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_insert_index_is_too_small(self):
        nums = [0, 1, 2]
        nums.insert(-15, -1)

        self.assertEqual(nums, [-1, 0, 1, 2])

    def test_insert_index_is_too_big(self):
        nums = [0, 1, 2]
        nums.insert(83, 3)

        self.assertEqual(nums, [0, 1, 2, 3])

    def test_pop_without_argument(self):
        hello = ['H', 'e', 'l', 'l', 'o']

        hello.pop()
        self.assertEqual(hello, ['H', 'e', 'l', 'l'])

    def test_pop_with_argument(self):
        hello = ['H', 'e', 'l', 'l', 'o']

        hello.pop(1)
        self.assertEqual(hello, ['H', 'l', 'l', 'o'])

    def test_pop_with_negative_index_removes_element_from_the_back(self):
        hello = ['H', 'e', 'l', 'l', 'o']

        hello.pop(-1)
        self.assertEqual(hello, ['H', 'e', 'l', 'l'])

    def test_pop_with_too_small_index_raises_index_error(self):
        hello = ['H', 'e', 'l', 'l', 'o']

        with self.assertRaises(IndexError):
            hello.pop(-6)

    def test_pop_with_too_large_index_raises_index_error(self):
        hello = ['H', 'e', 'l', 'l', 'o']

        with self.assertRaises(IndexError):
            hello.pop(99)

    def test_remove_removes_first_occurrence_of_passed_argument(self):
        hello = ['H', 'e', 'l', 'l', 'o']

        hello.remove('e')
        self.assertEqual(hello, ['H', 'l', 'l', 'o'])

    def test_remove_raises_value_error_if_passed_argument_does_not_exist_in_list(self):
        hello = ['H', 'e', 'l', 'l', 'o']

        with self.assertRaises(ValueError):
            hello.remove('z')

    def test_reverse(self):
        hello = ['H', 'e', 'l', 'l', 'o']

        # Instead of hello[::-1], this does not return a newly reversed list, but changes the list itself
        # This is usually faster and does not require that much space as the slicing operation
        hello.reverse()
        self.assertEqual(hello, ['o', 'l', 'l', 'e', 'H'])

    def test_sort_with_no_arguments(self):
        numbers = [0, 2, 4, 6, 8, 7, 9, 5, 3, 1]

        numbers.sort()
        self.assertEqual(numbers, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_sort_with_no_sort_relation_raises_type_error(self):
        complex_numbers = [5 + 13j, 1 + 4j, 6 + 2j]

        with self.assertRaises(TypeError):
            complex_numbers.sort()

    def test_sort_with_key_argument_being_built_in_function(self):
        names = ['Batman', 'Superman', 'Wonderwoman', 'Catwoman', 'Iron Man']

        names.sort(key=len)
        self.assertEqual(names, ['Batman', 'Superman', 'Catwoman', 'Iron Man', 'Wonderwoman'])

    def test_sort_with_key_argument_being_custom(self):
        complex_numbers = [5 + 13j, 1 + 4j, 6 + 2j]

        def custom_complex_real_sort(a: complex):
            return a.real

        complex_numbers.sort(key=custom_complex_real_sort)
        self.assertEqual(complex_numbers, [1 + 4j, 5 + 13j, 6 + 2j])

        complex_numbers.sort(key=lambda x: x.imag)
        self.assertEqual(complex_numbers, [6 + 2j, 1 + 4j, 5 + 13j])

    def test_sort_with_reverse_argument(self):
        numbers = [0, 2, 4, 6, 8, 7, 9, 5, 3, 1]

        numbers.sort(reverse=True)
        self.assertEqual(numbers, [9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

    def test_referencing_of_list(self):
        hello = ['H', 'e', 'l', 'l', 'o']
        world = hello
        world += ['W', 'o', 'r', 'l', 'd']

        # instead of creating a new copy of the list (like with string), we only pass a reference to world and then
        # modify the referenced list
        self.assertEqual(hello, ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd'])
        self.assertEqual(world, ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd'])
        self.assertEqual(hello, world)
        self.assertTrue(hello is world)
        self.assertTrue(world is hello)

    def test_referencing_of_sliced_list(self):
        hello = ['H', 'e', 'l', 'l', 'o']
        world = hello[:]    # creates a copy
        world += ['W', 'o', 'r', 'l', 'd']

        self.assertEqual(hello, ['H', 'e', 'l', 'l', 'o'])
        self.assertEqual(world, ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd'])
        self.assertFalse(hello is world)

    def test_list_stores_only_references(self):
        a = [[]]
        a = 4 * a   # does not copy the empty list, but simply created additional references
        a[0].append(10)

        self.assertEqual(a, [[10], [10], [10], [10]])
