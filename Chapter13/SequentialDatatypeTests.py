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

        self.assertEqual("98765", last_five_reversed)
        self.assertEqual("97531", odd_digits_reversed)

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
        d2 = digits[-4:9]   # rather hard to understand
        d3 = digits[3:100]
        d4 = digits[5:3]

        self.assertEqual("", d1)
        self.assertEqual("678", d2)
        self.assertEqual("3456789", d3)
        self.assertEqual("", d4)
