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

    def test_format_with_minimum_width_specifier_with_alignment(self):
        template = "Sum: {sum:>5} Euro"

        result = template.format(sum=443)

        self.assertEqual(result, "Sum:   443 Euro")

    def test_format_with_minimum_width_specifier_with_alignment_and_sign(self):
        template = "Temperature: {temperature:=7}°C"

        result1 = template.format(temperature=12.5)
        result2 = template.format(temperature=-12.5)

        self.assertEqual(result1, "Temperature:    12.5°C")
        self.assertEqual(result2, "Temperature: -  12.5°C")

    def test_format_with_minimum_width_specifier_align_center_and_fill_character(self):
        template = "{text:-^25}"

        result = template.format(text="Hello World")

        self.assertEqual(result, "-------Hello World-------")

    def test_format_show_sign_with_plus_sign(self):
        template = "Sum: {:+}"

        result1 = template.format(123)
        result2 = template.format(-123)

        self.assertEqual(result1, "Sum: +123")
        self.assertEqual(result2, "Sum: -123")

    def test_format_show_only_negative_sign(self):
        template = "Sum: {:-}"

        result1 = template.format(123)
        result2 = template.format(-123)

        self.assertEqual(result1, "Sum: 123")
        self.assertEqual(result2, "Sum: -123")

    def test_format_show_only_negative_sign_but_same_width(self):
        template = "Sum: {: }"

        result1 = template.format(123)
        result2 = template.format(-123)

        self.assertEqual(result1, "Sum:  123")
        self.assertEqual(result2, "Sum: -123")

    def test_format_combine_align_and_sign(self):
        template = "Costs: {:0=+10}"

        result1 = template.format(123)
        result2 = template.format(-123)

        self.assertEqual(result1, "Costs: +000000123")
        self.assertEqual(result2, "Costs: -000000123")

    def test_format_with_type(self):
        template = "Number in bits: {:b}"

        result = template.format(8)

        self.assertEqual(result, "Number in bits: 1000")

    def test_format_with_type_additional_prefix(self):
        template = "{num:#b} and {num:b}"

        result = template.format(num=10)

        self.assertEqual(result, "0b1010 and 1010")

    def test_format_floating_point_numbers(self):
        template = "Num: {:e}"

        result = template.format(123.456)

        self.assertEqual(result, "Num: 1.234560e+02")

    def test_ord_returns_value_corresponding_to_character(self):
        result = ord("j")

        self.assertEqual(result, 106)

    def test_chr_returns_character_corresponding_to_value(self):
        result = chr(106)

        self.assertEqual(result, "j")

    def test_string_with_unicode(self):
        s = "\u20ac"

        self.assertEqual(s, "€")
