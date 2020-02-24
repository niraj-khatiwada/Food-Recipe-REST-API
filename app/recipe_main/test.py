from django.test import TestCase
from .calc import sum

class TestSum(TestCase):
    def test_sum_of_two_numbers(self):
        self.assertEqual(sum(3,8), 11)