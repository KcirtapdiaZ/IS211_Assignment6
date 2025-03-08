class ConversionNotPossibleException(Exception):
    pass

def convert(fromUnit: str, toUnit: str, value: float) -> float:
    conversion_map = {
        'Celsius': {
            'Kelvin': lambda celsius: celsius + 273.15,
            'Fahrenheit': lambda celsius: celsius * 9 / 5 + 32
        },
        'Fahrenheit': {
            'Celsius': lambda fahrenheit: (fahrenheit - 32) * 5 / 9,
            'Kelvin': lambda fahrenheit: (fahrenheit + 459.67) * 5 / 9
        },
        'Kelvin': {
            'Celsius': lambda kelvin: kelvin - 273.15,
            'Fahrenheit': lambda kelvin: (kelvin * 9 / 5) - 459.67
        },
        'Miles': {
            'Yards': lambda miles: miles * 1760,
            'Meters': lambda miles: miles * 1609.34
        },
        'Yards': {
            'Miles': lambda yards: yards / 1760,
            'Meters': lambda yards: yards * 0.9144
        },
        'Meters': {
            'Miles': lambda meters: meters / 1609.34,
            'Yards': lambda meters: meters / 0.9144
        }
    }
    
    try:
        return conversion_map[fromUnit][toUnit](value)
    except KeyError:
        raise ConversionNotPossibleException(f"Conversion from {fromUnit} to {toUnit} is not possible.")
