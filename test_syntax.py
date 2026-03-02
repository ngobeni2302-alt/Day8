import unittest
from io import StringIO
import sys

# import your file here
# example: import advanced_loops as loops
import syntax as loops   # <-- CHANGE THIS


class TestAdvancedLoops(unittest.TestCase):

    # Helper to capture printed output
    def capture_output(self, func, *args):
        captured = StringIO()
        sys.stdout = captured
        func(*args)
        sys.stdout = sys.__stdout__
        return captured.getvalue().strip()

    # 1. print_odds_reverse
    def test_print_odds_reverse(self):
        output = self.capture_output(loops.print_odds_reverse, 5)
        self.assertTrue(len(output) > 0)

    # 2. count_multiples
    def test_count_multiples(self):
        output = self.capture_output(loops.count_multiples, 10, 2)
        self.assertTrue(len(output) > 0)

    # 3. print_triangle
    def test_print_triangle(self):
        output = self.capture_output(loops.print_triangle, 3)
        lines = output.split("\n")
        self.assertEqual(len(lines), 3)

    # 4. print_number_triangle
    def test_print_number_triangle(self):
        output = self.capture_output(loops.print_number_triangle, 4)
        lines = output.split("\n")
        self.assertEqual(len(lines), 4)

    # 5. sum_until_limit
    def test_sum_until_limit(self):
        output = self.capture_output(loops.sum_until_limit, 10)
        self.assertTrue(output.isdigit())

    # 6. factorial
    def test_factorial(self):
        self.assertEqual(loops.factorial(0), 1)
        self.assertEqual(loops.factorial(1), 1)
        self.assertEqual(loops.factorial(5), 120)

    # 7. count_digits
    def test_count_digits(self):
        self.assertEqual(loops.count_digits(1), 1)
        self.assertEqual(loops.count_digits(12345), 5)

    # 8. reverse_number
    def test_reverse_number(self):
        self.assertEqual(loops.reverse_number(1234), 4321)
        self.assertEqual(loops.reverse_number(1000), 1)

    # 9. multiplication_table
    def test_multiplication_table(self):
        output = self.capture_output(loops.multiplication_table, 5)
        lines = output.split("\n")
        self.assertEqual(len(lines), 10)

    # 10. print_pyramid
    def test_print_pyramid(self):
        output = self.capture_output(loops.print_pyramid, 3)
        lines = output.split("\n")
        self.assertEqual(len(lines), 3)


if __name__ == "__main__":
    unittest.main()