import conversions


class ConversionNotPossible(Exception):
    """Raised when converting non-convertable measurements"""

    pass


def convert(from_unit, to_unit, value):
    from_unit_cleaned = from_unit.strip().lower()
    to_unit_cleaned = to_unit.strip().lower()

    if from_unit_cleaned == "miles" and to_unit_cleaned == "yards":
        return conversions.convert_miles_to_yards(value)
    elif from_unit_cleaned == "miles" and to_unit_cleaned == "meters":
        return conversions.convert_miles_to_meters(value)
    elif from_unit_cleaned == "meters" and to_unit_cleaned == "miles":
        return conversions.convert_meters_to_miles(value)
    elif from_unit_cleaned == "meters" and to_unit_cleaned == "yards":
        return conversions.convert_meters_to_yards(value)
    elif from_unit_cleaned == "yards" and to_unit_cleaned == "miles":
        return conversions.convert_yards_to_miles(value)
    elif from_unit_cleaned == "yards" and to_unit_cleaned == "meters":
        return conversions.convert_yards_to_meters(value)
    elif from_unit_cleaned == "celsius" and to_unit_cleaned == "kelvin":
        return conversions.convert_celsius_to_kelvin(value)
    elif from_unit_cleaned == "celsius" and to_unit_cleaned == "fahrenheit":
        return conversions.convert_celsius_to_fahrenheit(value)
    elif from_unit_cleaned == "kelvin" and to_unit_cleaned == "celsius":
        return conversions.convert_kelvin_to_celsius(value)
    elif from_unit_cleaned == "kelvin" and to_unit_cleaned == "fahrenheit":
        return conversions.convert_kelvin_to_fahrenheit(value)
    elif from_unit_cleaned == "fahrenheit" and to_unit_cleaned == "celsius":
        return conversions.convert_fahrenheit_to_celsius(value)
    elif from_unit_cleaned == "fahrenheit" and to_unit_cleaned == "kelvin":
        return conversions.convert_fahrenheit_to_kelvin(value)
    else:
        raise ConversionNotPossible(
            "Can't convert between temperature and distance"
        )
