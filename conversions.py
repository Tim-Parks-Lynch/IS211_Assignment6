def convert_celsius_to_kelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = celsius + 273.15

    if kelvins < 0:
        return 0
    else:
        return kelvins


def convert_celsius_to_fahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = celsius * 1.8 + 32.00

    return round(fahrenheit, 2)


def convert_kelvin_to_celsius(kelvin):
    """
    Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius
    """
    celsius = kelvin - 273.15

    return celsius


def convert_kelvin_to_fahrenheit(kelvin):
    """
    Takes in float representing a Kelvin measurement, and returns the temperature converted into Fahrenheit
    """

    fahrenheit = (kelvin - 273.15) * 1.8 + 32

    return round(fahrenheit, 2)


def convert_fahrenheit_to_celsius(fahrenheit):
    """
    Takes in a float representing a Fahrenheit measurement, and returns the temperature converted into Celsius
    """
    celsius = (fahrenheit - 32) * 5 / 9

    return round(celsius, 2)


def convert_fahrenheit_to_kelvin(fahrenheit):
    """
    Takes in a float representing a Fahrenheit measurement, and returns the temperature converted into Kelvin
    """
    kelvin = (fahrenheit + 459.67) * 5 / 9

    return round(kelvin, 2)
