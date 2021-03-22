import unittest
from Calculator import Calculator
from CVSReader import CsvReader

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader('UnitTestAddition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(3, 3), 9)
        self.assertEqual(self.calculator.result, 9)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(28, 7), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_square_method_calculator(self):
        self.assertEqual(self.calculator.sq(5), 25)
        self.assertEqual(self.calculator.result, 25)

    def test_square_root_method_calculator(self):
        self.assertEqual(self.calculator.sqrt(25), 5)
        self.assertEqual(self.calculator.result, 5)

if __name__ == '__main__':
    unittest.main()
