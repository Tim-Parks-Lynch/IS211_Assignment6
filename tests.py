import unittest
from conversions import *
from conversions_refactored import *


class ConversionTestCase(unittest.TestCase):
    # Known Values Section
    celsius_kelvin_known_values = (
        (300.00, 573.15),
        (10.00, 283.15),
        (40.00, 313.15),
        (-10.00, 263.15),
        (0, 273.15),
    )

    celsius_fahrenheit_known_values = (
        (0, 32),
        (-273.15, -459.67),
        (37.00, 98.60),
        (100.00, 212.00),
        (40.00, 104.00),
    )

    kelvin_fahrenheit_known_values = (
        (0, -459.67),
        (255.37, 0),
        (273.15, 32.00),
        (1941.00, 3034.13),
        (5800.00, 9980.33),
    )

    miles_yards_known_values = (
        (1.00, 1760.00),
        (100.00, 176000.00),
        (50.00, 88000.00),
        (0.50, 880.00),
        (25.00, 44000.00),
    )

    miles_meters_known_values = (
        (1.00, 1609.34),
        (100.00, 160934.40),
        (50.00, 80467.20),
        (0.50, 804.67),
        (25.00, 40233.60),
    )

    yards_meters_known_values = (
        (1.00, 0.91),
        (100.04, 91.44),
        (50.02, 45.72),
        (0.50, 0.46),
        (25.01, 22.86),
    )

    # Kelvin to Celsius known values
    kelvin_celsius_known_values = tuple(
        tup[::-1] for tup in celsius_kelvin_known_values
    )
    # Fahrenheit to Celsius known values
    fahrenheit_celsius_known_values = tuple(
        tup[::-1] for tup in celsius_fahrenheit_known_values
    )
    # Fahrenheit to Kelvin known values
    fahrenheit_kelvin_known_values = tuple(
        tup[::-1] for tup in kelvin_fahrenheit_known_values
    )
    # Yards to Miles known values
    yards_miles_known_values = tuple(
        tup[::-1] for tup in miles_yards_known_values
    )
    # Meters to Miles known values
    meters_miles_known_values = tuple(
        tup[::-1] for tup in miles_meters_known_values
    )
    # Meters to Yards known values
    meters_yards_known_values = tuple(
        tup[::-1] for tup in yards_meters_known_values
    )

    # Testing Section
    def test_convert_celsius_to_kelvin_good_values(self):
        """
        convert_celsius_to_kelvin should give known result with known input
        """
        for celsius, kelvin in self.celsius_kelvin_known_values:
            result = convert_celsius_to_kelvin(celsius)
            self.assertEqual(result, kelvin)

    def test_convert_celsius_to_fahrenheit_good_values(self):
        """
        convert_celsius_to_fahrenheit should give known result with known input
        """
        for celsius, fahrenheit in self.celsius_fahrenheit_known_values:
            result = convert_celsius_to_fahrenheit(celsius)
            self.assertEqual(result, fahrenheit)

    def test_convert_kelvin_to_celsius_good_values(self):
        """
        convert_kelvin_to_celsius should give known result with known input
        """

        for kelvin, celsius in self.kelvin_celsius_known_values:
            result = convert_kelvin_to_celsius(kelvin)
            self.assertEqual(result, celsius)

    def test_convert_kelvin_to_fahrenheit_good_values(self):
        """
        convert_kelvin_to_fahrenheit should give known result with known input
        """

        for kelvin, fahrenheit in self.kelvin_fahrenheit_known_values:
            result = convert_kelvin_to_fahrenheit(kelvin)
            self.assertEqual(result, fahrenheit)

    def test_convert_fahrenheit_to_celsius_good_values(self):
        """convert_fahrenheit_to_celsius should give known result with known input"""

        for fahrenheit, celsius in self.fahrenheit_celsius_known_values:
            result = convert_fahrenheit_to_celsius(fahrenheit)
            self.assertEqual(result, celsius)

    def test_convert_fahrenheit_to_kelvin_good_values(self):
        """convert_fahrenheit_to_kelvin should give known result with known input"""

        for fahrenheit, kelvin in self.fahrenheit_kelvin_known_values:
            result = convert_fahrenheit_to_kelvin(fahrenheit)
            self.assertEqual(result, kelvin)

    # Refactored Code Tests
    def test_convert_refactor_miles_to_yards_good_values(self):
        """tests the refactored code for miles to yards"""

        for miles, yards in self.miles_yards_known_values:
            result = convert("Miles", "Yards", miles)
            self.assertAlmostEqual(result, yards)

    def test_convert_refactor_yards_to_miles_good_values(self):
        """tests the refactored code for yards to miles"""

        for yards, miles in self.yards_miles_known_values:
            result = convert("Yards", "Miles", yards)
            self.assertAlmostEqual(result, miles)

    def test_convert_refactor_miles_to_meters_good_values(self):
        """tests the refactored code for miles to meters"""

        for miles, meters in self.miles_meters_known_values:
            result = convert("MILES", " meters ", miles)
            self.assertAlmostEqual(result, meters)

    def test_convert_refactor_meters_to_miles_good_values(self):
        """tests the refactored code for meters to miles"""

        for meters, miles in self.meters_miles_known_values:
            result = convert("Meters", "Miles", meters)
            self.assertAlmostEqual(result, miles)

    def test_convert_refactor_yards_to_meters_good_values(self):
        """tests the refactored code for yards to meters"""

        for yards, meters in self.yards_meters_known_values:
            result = convert("Yards", "Meters", yards)
            self.assertAlmostEqual(result, meters)

    def test_convert_refactor_meters_to_yards_good_values(self):
        """tests the refactored code for meters to yards"""

        for meters, yards in self.meters_yards_known_values:
            result = convert("Meters", "Yards", meters)
            self.assertAlmostEqual(result, yards)

    def test_convert_refactor_celsius_to_kelvin_good_values(self):
        """
        tests the refactored code for celsius to kelvin
        """

        for celsius, kelvin in self.celsius_kelvin_known_values:
            result = convert("Celsius", "kelvin", celsius)
            self.assertEqual(result, kelvin)

    def test_convert_refactor_celsius_to_fahrenheit_good_values(self):
        """
        tests the refactored code for celsius to fahrenheit
        """
        for celsius, fahrenheit in self.celsius_fahrenheit_known_values:
            result = convert("celsius", "fahrenheit", celsius)
            self.assertEqual(result, fahrenheit)

    def test_convert_refactor_kelvin_to_celsius_good_values(self):
        """
        tests the refactored code for kevlin to celsius
        """

        for kelvin, celsius in self.kelvin_celsius_known_values:
            result = convert("kelvin", "celsius", kelvin)
            self.assertEqual(result, celsius)

    def test_convert_refactor_kelvin_to_fahrenheit_good_values(self):
        """
        tests the refactored code for kelvin to fahrenheit
        """

        for kelvin, fahrenheit in self.kelvin_fahrenheit_known_values:
            result = convert("kelvin", "fahrenheit", kelvin)
            self.assertEqual(result, fahrenheit)

    def test_convert_refactor_fahrenheit_to_celsius_good_values(self):
        """
        tests the refactored code for fahrenheit to celsius
        """

        for fahrenheit, celsius in self.fahrenheit_celsius_known_values:
            result = convert("fahrenheit", "celsius", fahrenheit)
            self.assertEqual(result, celsius)

    def test_convert_refactor_fahrenheit_to_kelvin_good_values(self):
        """
        tests the refactored code for fahrenheit to kelvin
        """

        for fahrenheit, kelvin in self.fahrenheit_kelvin_known_values:
            result = convert("fahrenheit", "kelvin", fahrenheit)
            self.assertEqual(result, kelvin)

    def test_convert_refactor_incorrect_measurement_parameters(self):
        """
        tests that converting from temp to distance throws an error
        """
        self.assertRaises(
            ConversionNotPossible, convert, "celsius", "meters", 10
        )


if __name__ == "__main__":
    unittest.main()
