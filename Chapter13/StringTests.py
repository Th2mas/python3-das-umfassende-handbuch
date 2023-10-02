import unittest


class StringTests(unittest.TestCase):

    def test_string_with_multiple_lines(self):
        s = """A string!
        I am a string!
        Me too!
        """

        self.assertEqual(s, "A string!\n        I am a string!\n        Me too!\n        ")

    def test_string_with_space_as_separator(self):
        s = "A string" "A second string"   "A third string"

        self.assertEqual(s, "A stringA second stringA third string")

    def test_string_multiple_lines_without_additional_escape_characters_and_spaces(self):
        s = (
            "I am "
            "a very "
            "long string"
        )

        self.assertEqual(s, "I am a very long string")

    def test_string_as_bytes(self):
        b = b"I am a bytes string"

        self.assertEqual(b, b"I am a bytes string")
        self.assertEqual(type(b), bytes)

    def test_bytearray_with_argument(self):
        ba = bytearray(3)

        self.assertEqual(ba, b"\x00\x00\x00")

    def test_raw_string(self):
        rs = r"A raw string \\\f with many \t\ escape sequences\\t"

        self.assertEqual(rs, "A raw string \\\\\\f with many \\t\\ escape sequences\\\\t")

    def test_split_without_separator_splits_space(self):
        s = "A b, c-d e/f"
        result = s.split()

        self.assertEqual(result, ["A", "b,", "c-d", "e/f"])

    def test_split_with_separator(self):
        s = "A-b-c-d-e"
        result = s.split("-")

        self.assertEqual(result, ["A", "b", "c", "d", "e"])

    def test_split_with_separator_and_maxsplit(self):
        s = "A-b-c-d-e-f"
        result = s.split("-", 3)

        self.assertEqual(result, ["A", "b", "c", "d-e-f"])

    def test_rsplit_with_separator_and_maxsplit(self):
        s = "A-b-c-d-e-f"
        result = s.rsplit("-", 2)

        self.assertEqual(result, ['A-b-c-d', 'e', 'f'])

    def test_split_with_no_separator_but_multiple_spaces(self):
        s = "A b  c     d"
        result = s.split()

        self.assertEqual(result, ["A", "b", "c", "d"])

    def test_split_with_no_separator_but_multiple_whitespaces(self):
        s = "\rA b  c\t \v    \n     d"
        result = s.split()

        self.assertEqual(result, ["A", "b", "c", "d"])

    def test_split_with_separator_multiple_times(self):
        s = "A b  c     d"
        result = s.split(" ")

        self.assertEqual(result, ["A", "b", "", "c", "", "", "", "", "d"])

    def test_splitlines_splits_string_with_os_specific_line_separators(self):
        s = "Unix\nWindows\r\nMac\rLast line"

        result = s.splitlines()

        self.assertEqual(result, ['Unix', 'Windows', 'Mac', 'Last line'])

    def test_splitlines_splits_string_with_os_specific_line_separators_with_keeplines(self):
        s = "Unix\nWindows\r\nMac\rLast line"

        result = s.splitlines(True)

        self.assertEqual(result, ['Unix\n', 'Windows\r\n', 'Mac\r', 'Last line'])

    def test_partition_creates_tuple_of_string_with_first_occurrence_of_sep(self):
        website = 'https://www.google.com'

        result = website.partition('.')

        self.assertEqual(result, ('https://www', '.', 'google.com'))

    def test_rpartition_creates_tuple_of_string_with_last_occurrence_of_sep(self):
        website = 'https://www.google.com'

        result = website.rpartition('.')

        self.assertEqual(result, ('https://www.google', '.', 'com'))

    def test_find_returns_index_of_first_substring(self):
        s = 'Why do we fall? So we can learn to pick ourselves up'

        sub1 = s.find("d")
        sub2 = s.find("we")

        self.assertEqual(sub1, 4)
        self.assertEqual(sub2, 7)

    def test_find_does_not_throw_error_when_string_cannot_be_found(self):
        s = 'Batman'

        result = s.find('Superman')

        self.assertEqual(result, -1)

    def test_rfind_returns_index_of_last_substring(self):
        s = 'Why do we fall? So we can learn to pick ourselves up'

        result = s.rfind("we")

        self.assertEqual(result, 19)

    def test_index_returns_index_of_first_substring(self):
        s = 'Why do we fall? So we can learn to pick ourselves up'

        sub1 = s.index("d")
        sub2 = s.index("we")

        self.assertEqual(sub1, 4)
        self.assertEqual(sub2, 7)

    def test_index_throws_value_error_if_substring_is_not_found(self):
        s = 'Batman'

        with self.assertRaises(ValueError):
            s.index('Superman')

    def test_rindex_returns_index_of_last_substring(self):
        s = 'Why do we fall? So we can learn to pick ourselves up'

        result = s.rindex("we")

        self.assertEqual(result, 19)

    def test_count_returns_number_of_occurrences_of_substring(self):
        s = "Hello Hello hello Hello"

        result = s.count("Hello")

        self.assertEqual(result, 3)

    def test_replace_returns_string_with_replaced_value(self):
        s = "Python is really bad"

        result = s.replace("bad", "good")

        self.assertEqual(result, "Python is really good")

    def test_replace_with_count_returns_string_with_only_few_replacements(self):
        s = 'Why wedo wewe fall?'

        result = s.replace("we", "", 2)

        self.assertEqual(result, "Why do we fall?")

    def test_lower_returns_string_with_only_lowercase_letters(self):
        s = "BAtmAn"

        result = s.lower()

        self.assertEqual(result, "batman")

    def test_upper_returns_string_with_only_uppercase_letters(self):
        s = "BAtmAn"

        result = s.upper()

        self.assertEqual(result, "BATMAN")

    def test_swapcase_returns_string_with_swapped_upper_and_lowecase_letters(self):
        s = "BAtmAn"

        result = s.swapcase()

        self.assertEqual(result, "baTMaN")

    def test_capitalize_returns_string_with_first_character_capitalized(self):
        s = "why do we fall?"

        result = s.capitalize()

        self.assertEqual(result, "Why do we fall?")

    def test_title_returns_string_with_each_word_being_capitalized(self):
        s = "why do we fall?"

        result = s.title()

        self.assertEqual(result, "Why Do We Fall?")

    def test_expandtabs_replaces_tabs_with_spaces(self):
        s = "Why\n\tdo\n\t\twe fall?"
        expected = """Why
        do
                we fall?"""

        result = s.expandtabs()

        self.assertEqual(result, expected)

    def test_expandtabs_with_tabsize_replaces_tabs_with_tabsize_spaces(self):
        s = "Why\n\tdo\n\t\twe fall?"
        expected = """Why
    do
        we fall?"""

        result = s.expandtabs(4)

        self.assertEqual(result, expected)

    def test_strip_removes_whitespace_characters_on_both_sides_of_string(self):
        s = "    \n\t   Why do we fall?   \t\t\r\n  "

        result = s.strip()

        self.assertEqual(result, "Why do we fall?")

    def test_strip_with_chars_removes_characters_defined_in_the_string(self):
        s = "Why do we fall?"

        result = s.strip("Whl?")

        self.assertEqual(result, "y do we fa")

    def test_lstrip_removes_whitespace_characters_on_left_side_of_string(self):
        s = "    \n\t   Why do we fall?   \t\t\r\n  "

        result = s.lstrip()

        self.assertEqual(result, "Why do we fall?   \t\t\r\n  ")

    def test_rstrip_removes_whitespace_characters_on_left_side_of_string(self):
        s = "    \n\t   Why do we fall?   \t\t\r\n  "

        result = s.rstrip()

        self.assertEqual(result, "    \n\t   Why do we fall?")

    def test_center_fills_string_with_whitespaces_and_centers_string(self):
        s = "Why do we fall?"
        expected = "     Why do we fall?     "

        result = s.center(25)

        self.assertEqual(result, expected)

    def test_center_returns_string_if_width_is_too_short(self):
        s = "Why do we fall?"

        result = s.center(10)

        self.assertEqual(result, s)

    def test_ljust_fills_string_on_right_side_with_whitespaces(self):
        s = "Why do we fall?"
        expected = "Why do we fall?          "

        result = s.ljust(25)

        self.assertEqual(result, expected)

    def test_rjust_with_char_fills_string_on_right_side_with_given_char(self):
        s = "Why do we fall?"
        expected = "Why do we fall?----------"

        result = s.ljust(25, '-')

        self.assertEqual(result, expected)

    def test_zfill_fills_string_on_left_side_with_zeroes(self):
        amount = "13.57"

        result = amount.zfill(10)

        self.assertEqual(result, "0000013.57")

    def test_isalnum_returns_true_if_string_contains_only_characters_and_digits(self):
        s = "abcd1234"

        result = s.isalnum()

        self.assertTrue(result)

    def test_isalnum_returns_false_if_string_contains_not_only_characters_and_digits(self):
        s = "abcd1234!"

        result = s.isalnum()

        self.assertFalse(result)

    def test_isalpha_returns_true_if_string_contains_only_characters(self):
        s = "abcdAbcd"

        result = s.isalpha()

        self.assertTrue(result)

    def test_isalpha_returns_false_if_string_contains_not_only_characters(self):
        s = "abcd1234"

        result = s.isalpha()

        self.assertFalse(result)

    def test_isdigit_returns_true_if_string_contains_only_digits(self):
        s = "1234"

        result = s.isdigit()

        self.assertTrue(result)

    def test_isdigit_returns_false_if_string_contains_not_only_digits(self):
        s = "12.34"

        result = s.isdigit()

        self.assertFalse(result)

    def test_startswith_returns_bool_depending_on_whether_string_starts_with_argument(self):
        s = "Hello World"

        startsWithCapitalH = s.startswith("Hello")
        startsWithLowercaseH = s.startswith("hello")

        self.assertTrue(startsWithCapitalH)
        self.assertFalse(startsWithLowercaseH)

    def test_startswith_with_start_shifts_the_starting_position(self):
        s = "Hello World"

        result = s.startswith("Wor", 6)

        self.assertTrue(result)

    def test_endswith_returns_bool_depending_on_whether_string_ends_with_argument(self):
        s = "Hello World"

        result = s.endswith("World")

        self.assertTrue(result)

    def test_join_joins_list_with_separator(self):
        separator1 = ","
        separator2 = ""
        names = ["Bruce", "Clark", "Tony"]

        result1 = separator1.join(names)
        result2 = separator2.join(names)

        self.assertEqual(result1, "Bruce,Clark,Tony")
        self.assertEqual(result2, "BruceClarkTony")

    def test_join_joins_every_character_of_string(self):
        s = "Hello"
        separator = ":"

        result = separator.join(s)

        self.assertEqual(result, "H:e:l:l:o")
