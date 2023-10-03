import unittest


class StringFormatTests(unittest.TestCase):
    def test_format_with_two_enumerated_placeholders(self):
        template = "It is {0}:{1}am"

        result = template.format(8, 36)

        self.assertEqual(result, "It is 8:36am")

    def test_format_with_two_empty_placeholders(self):
        template = "It is {}:{}am"

        result = template.format(8, 36)

        self.assertEqual(result, "It is 8:36am")

    def test_format_with_named_placeholders(self):
        template = "It is {hour}:{minute}am"

        result = template.format(hour=8, minute=36)

        self.assertEqual(result, "It is 8:36am")

    def test_format_with_enumerated_and_named_placeholders(self):
        template = "It is {hour}:{0}am"

        result = template.format(36, hour=8)

        self.assertEqual(result, "It is 8:36am")

    def test_format_with_empty_and_named_placeholders(self):
        template = "It is {hour}:{}am"

        result = template.format(36, hour=8)

        self.assertEqual(result, "It is 8:36am")

    def test_format_with_reused_placeholder(self):
        template = "{y}{em} yeast, {}{em} flour, {}{em} salt"

        result = template.format(100, 1, y=10, em='g')

        self.assertEqual(result, "10g yeast, 100g flour, 1g salt")

    def test_format_with_braces(self):
        template = "{{Not formatted}} string. Formatted: {v}"

        result = template.format(v="Test")

        self.assertEqual(result, "{Not formatted} string. Formatted: Test")

    def test_format_with_access_on_attributes(self):
        template = "Real: {i.real}, Imag: {i.imag}"

        result = template.format(i=15 + 20j)

        self.assertEqual(result, "Real: 15.0, Imag: 20.0")

    def test_format_list_with_index(self):
        template = "{list[0]}, {list[1]}"

        result = template.format(list=["Bruce", "Wayne"])

        self.assertEqual(result, "Bruce, Wayne")

    def test_format_with_format_specifier(self):
        template = "Pi: {:.2f}"

        result = template.format(3.14159265)

        self.assertEqual(result, "Pi: 3.14")

    def test_format_with_minimum_width_specifier(self):
        template = "{:15}|{:15}"

        result = template.format("Bruce", "Wayne")

        self.assertEqual(result, "Bruce          |Wayne          ")

    def test_format_with_minimum_width_specifier_smaller_than_actual_string(self):
        template = "{firstname:7} {lastname:3}"

        result = template.format(firstname="Barry", lastname="Allen")

        self.assertEqual(result, "Barry   Allen")
