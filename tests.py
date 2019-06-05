import unittest

from snippets import (
    foo,
    lambda_array,
    read_file,
    calculate_unpaid_loans,
    calculate_paid_loans,
    average_paid_loans)


class TestMain(unittest.TestCase):

    def test_foo_has_baz(self):
        self.assertEqual(
            foo(), ['baz'])

    def test_lambdas_equals_19(self):
        lambdas = lambda_array()
        self.assertEqual(lambdas[0](10), 19)

    def test_number_of_loans_equals_15(self):
        json_file = read_file()
        self.assertEqual(len(json_file.get("loans")), 15)

    def test_calculate_unpaid_loans(self):
        json_file = read_file()
        self.assertEqual(calculate_unpaid_loans(json_file), 11062)

    def test_calculate_paid_loans(self):
        json_file = read_file()
        self.assertEqual(calculate_paid_loans(json_file), 29493.85304)

    def test_average_paid_loans(self):
        json_file = read_file()
        self.assertEqual(average_paid_loans(json_file), 2681.2593672727276)


if __name__ == '__main__':
    unittest.main()
