"""
Sample Tests
"""

from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Tests the calc module"""

    def test_add_numbers(self):
        """Tests adding numbers"""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_substract_numbers(self):
        """Tests substracting numbers"""
        res = calc.substract(5, 4)
        self.assertEqual(res, 1)
