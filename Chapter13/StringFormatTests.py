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
