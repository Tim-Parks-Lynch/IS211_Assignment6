import unittest
import conversions


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
        (1941, 3034.13),
        (5800, 9980.33),
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

    # Testing Section
    def test_convert_celsius_to_kelvin_good_values(self):
        """
        convert_celsius_to_kelvin should give known result with known input
        """
        for celsius, kelvin in self.celsius_kelvin_known_values:
            result = conversions.convert_celsius_to_kelvin(celsius)
            self.assertEqual(kelvin, result)

    def test_convert_celsius_to_fahrenheit_good_values(self):
        """
        convert_celsius_to_fahrenheit should give known result with known input
        """
        for celsius, fahrenheit in self.celsius_fahrenheit_known_values:
            result = conversions.convert_celsius_to_fahrenheit(celsius)
            self.assertEqual(result, fahrenheit)

    def test_convert_kelvin_to_celsius_good_values(self):
        """
        convert_kelvin_to_celsius should give known result with known input
        """

        for kelvin, celsius in self.kelvin_celsius_known_values:
            result = conversions.convert_kelvin_to_celsius(kelvin)
            self.assertEqual(result, celsius)

    def test_convert_kelvin_to_fahrenheit_good_values(self):
        """
        convert_kelvin_to_fahrenheit should give known result with known input
        """

        for kelvin, fahrenheit in self.kelvin_fahrenheit_known_values:
            result = conversions.convert_kelvin_to_fahrenheit(kelvin)
            self.assertEqual(result, fahrenheit)

    def test_convert_fahrenheit_to_celsius_good_values(self):
        """convert_fahrenheit_to_celsius should give known result with known input"""

        for fahrenheit, celsius in self.fahrenheit_celsius_known_values:
            result = conversions.convert_fahrenheit_to_celsius(fahrenheit)
            self.assertEqual(result, celsius)

    def test_convert_fahrenheit_to_kelvin_good_values(self):
        """convert_fahrenheit_to_kelvin should give known result with known input"""

        for fahrenheit, kelvin in self.fahrenheit_kelvin_known_values:
            result = conversions.convert_fahrenheit_to_kelvin(fahrenheit)
            self.assertEqual(result, kelvin)


if __name__ == "__main__":
    unittest.main()
