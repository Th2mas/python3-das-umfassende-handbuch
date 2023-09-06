import unittest


class SequentialDatatypeTests(unittest.TestCase):

    def test_referencing_of_string(self):
        a = 'Hello'
        b = a
        b += ' World'

        # a string is immutable, therefore b got a copy of a and not a itself
        self.assertEqual(a, 'Hello')
        self.assertEqual(b, 'Hello World')

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

    def test_subsequence_with_indexing_operator(self):
        name = "Hello World"
        hello = name[0:5]

        self.assertEqual(hello, "Hello")

    def test_sublist_with_indexing_operator(self):
        abcd = ['a', 'c', 'b', 'd']
        ac = abcd[0:2]

        self.assertEqual(ac, ['a', 'c'])

    def test_subsequence_with_indexing_operator_omit_start_or_end(self):
        abcdefg = 'abcdefg'
        abc = abcdefg[:3]
        defg = abcdefg[3:]

        self.assertEqual("abc", abc)
        self.assertEqual("defg", defg)

    def test_substring_as_reference(self):
        batman = "Batman"
        robin = batman

        self.assertTrue(batman == robin)
        self.assertTrue(robin is batman)
        self.assertTrue(batman is robin)

        superman = batman[:]
        self.assertEqual(superman, batman)
        self.assertTrue(superman == batman)
        self.assertTrue(batman is superman)
        self.assertTrue(superman is batman)

    def test_subsequence_as_copy(self):
        batman = ["Batman"]
        robin = batman

        self.assertTrue(batman == robin)
        self.assertTrue(robin is batman)
        self.assertTrue(batman is robin)

        superman = batman[:]
        self.assertEqual(superman, batman)
        self.assertTrue(superman == batman)
        self.assertFalse(batman is superman)
        self.assertFalse(superman is batman)

    def test_slicing_with_step_size(self):
        digits = '0123456789'
        odd_digits = digits[1:10:2]
        even_digits = digits[0:9:2]

        self.assertEqual("13579", odd_digits)
        self.assertEqual("02468", even_digits)

    def test_slicing_with_step_size_no_bounds(self):
        digits = '0123456789'
        step_size = 2
        odd_digits = digits[1::step_size]
        even_digits = digits[::step_size]

        self.assertEqual("13579", odd_digits)
        self.assertEqual("02468", even_digits)

    def test_slicing_as_reverse(self):
        digits = '0123456789'
        last_five_reversed = digits[9:4:-1]
        odd_digits_reversed = digits[::-2]
        not_first_five_reversed = digits[4:0:-1]

        self.assertEqual("98765", last_five_reversed)
        self.assertEqual("97531", odd_digits_reversed)
        self.assertEqual("4321", not_first_five_reversed)

    def test_slicing_as_reverse_including_first_element(self):
        digits = '0123456789'

        # Special case: we can't simply set -1 as the end index, even though it would be excluded
        # The sliced string then becomes the empty string

        empty_string = digits[4:-1:-1]
        first_five_reversed = digits[4::-1]

        self.assertEqual('', empty_string)
        self.assertEqual('43210', first_five_reversed)

    def test_substring_with_incorrect_indices_no_exception(self):
        digits = '0123456789'
        d1 = digits[5:9:-1]
        d2 = digits[-4:9]  # rather hard to understand
        d3 = digits[3:100]
        d4 = digits[5:3]

        self.assertEqual("", d1)
        self.assertEqual("678", d2)
        self.assertEqual("3456789", d3)
        self.assertEqual("", d4)

    def test_length_of_string(self):
        s = 'Hello World'
        l = len(s)

        self.assertEqual(11, l)

    def test_length_of_array(self):
        a = ['a', 'b', 'c', 1, 2]
        l = len(a)

        self.assertEqual(5, l)

    def test_min_max_of_number_array(self):
        l = [5, 1, 10, -9.5, 12, -5]

        self.assertEqual(-9.5, min(l))
        self.assertEqual(12, max(l))

    def test_min_max_of_string(self):
        s = "Hello World"
        s2 = "Ww"

        # min/max on strings works on the char code
        self.assertEqual(" ", min(s))
        self.assertEqual("r", max(s))

        self.assertEqual("W", min(s2))
        self.assertEqual("w", max(s2))

    def test_min_max_of_mixed_array_raises_type_error(self):
        l = [1, 2, "world"]

        with self.assertRaises(TypeError):
            min(l)

        with self.assertRaises(TypeError):
            max(l)

    def test_index_on_array(self):
        digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

        self.assertEqual(3, digits.index(3))

    def test_index_on_string(self):
        s = "Hello world"

        self.assertEqual(2, s.index("l"))

    def test_index_with_subsection(self):
        a = [0, 11, 222, 3333, 44444, 3333, 222, 11, 0]

        self.assertEqual(1, a.index(11))
        self.assertEqual(7, a.index(11, 2))  # the second argument of 'index' is the starting position of the search
        self.assertEqual(8, a.index(0, -1))  # an argument < 0 starts at the end of the array and searches backwards
        self.assertEqual(0, a.index(0, -0))  # (-)0 is the same as the function without a second argument

    def test_index_raises_value_error_if_element_cannot_be_found(self):
        pi = [3, 1, 4, 1, 5, 9]

        with self.assertRaises(ValueError):
            pi.index(2)

    def test_count_occurrences_in_number_array(self):
        pi = [3, 1, 4, 1, 5, 9]

        self.assertEqual(2, pi.count(1))
        self.assertEqual(1, pi.count(3))

    def test_count_occurrences_in_string(self):
        s = "Hello World"

        self.assertEqual(3, s.count("l"))
