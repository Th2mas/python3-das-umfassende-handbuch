import unittest


class ImmutableListTests(unittest.TestCase):

    def test_tuple_creation(self):
        a = (1, 2, 3, 4, 5)

        self.assertEqual(a[3], 4)
        self.assertEqual(type(a), tuple)

    def test_tuple_creation_with_only_one_element(self):
        a = (2)

        self.assertEqual(type(a), int)

        b = (2,)

        self.assertEqual(type(b), tuple)

    def test_tuple_creation_with_no_element(self):
        a = ()

        self.assertEqual(len(a), 0)
        self.assertEqual(type(a), tuple)

    def test_tuple_packing(self):
        d = 26, 7, 1987

        self.assertEqual(type(d), tuple)
        self.assertEqual(len(d), 3)

    def test_tuple_unpacking(self):
        d = (26, 7, 1987)

        (day, month, year) = d
        self.assertEqual(day, 26)
        self.assertEqual(month, 7)
        self.assertEqual(year, 1987)

    def test_swap_with_tuples(self):
        a = 10
        b = 20
        c, d = 30, 40

        a, b = b, a
        c, d = d, c

        self.assertEqual(a, 20)
        self.assertEqual(b, 10)
        self.assertEqual(c, 40)
        self.assertEqual(d, 30)

    def test_tuple_unpacking_with_splat_operator(self):
        numbers = (1, 2, 3, 4, 5)
        first, *others, last = numbers  # the asterisk is called the splat operator or simply extended unpacking

        self.assertEqual(first, 1)
        self.assertEqual(others, [2, 3, 4])
        self.assertEqual(last, 5)

    def test_tuple_unpacking_with_splat_different_position(self):
        numbers = (1, 2, 3, 4, 5)
        *others, four, five = numbers   # you can use the splat operator only once when unpacking

        self.assertEqual(others, [1, 2, 3])
        self.assertEqual(four, 4)
        self.assertEqual(five, 5)

    def test_tuple_reference_can_be_updated(self):
        a = ([],)
        a[0].append('Hello World')

        self.assertEqual(a, (['Hello World'],))
