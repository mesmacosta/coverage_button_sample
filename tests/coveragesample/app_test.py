from unittest import TestCase

from coveragesample import APP


class CoverageAppTestCase(TestCase):

    def test_sum_should_add_values(self):
        expected = 10
        result = APP.sum(5, 5)
        self.assertEqual(expected, result)
