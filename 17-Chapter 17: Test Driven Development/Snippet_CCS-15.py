import unittest
from coffee_shop_simulator import CoffeeShopSimulator


class CoffeeShopSimulatorTests(unittest.TestCase):
    def test_convert_to_float(self):
        # Test a string conversion to float
        test_float = 1.23
        test_string = "1.23"
        self.assertEqual(CoffeeShopSimulator.convert_to_float(
            test_string), test_float)

    def test_x_of_y_with_numbers(self):
        # Test that x_of_y returns a list of x numbers of y
        number_list = [1, 1, 1, 1, 1]
        self.assertEqual(CoffeeShopSimulator.x_of_y(5, 1), number_list)

    def test_x_of_y_with_strings(self):
        # Test that x_of_y returns a list of x strings of y
        string_list = ["a", "a", "a", "a"]
        self.assertEqual(CoffeeShopSimulator.x_of_y(4, "a"), string_list)


if __name__ == '__main__':
    unittest.main()
