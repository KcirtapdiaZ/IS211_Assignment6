class ConversionNotPossibleException(Exception):
    pass

def convert(fromUnit: str, toUnit: str, value: float) -> float:
    conversions = {
        "Celsius": {"Kelvin": value + 273.15, "Fahrenheit": (value * 9/5) + 32},
        "Fahrenheit": {"Celsius": (value - 32) * 5/9, "Kelvin": (value - 32) * 5/9 + 273.15},
        "Kelvin": {"Celsius": value - 273.15, "Fahrenheit": (value - 273.15) * 9/5 + 32},
        # Add distance conversions here...
    }
    
    if fromUnit == toUnit:
        return value
    
    try:
        return conversions[fromUnit][toUnit]
    except KeyError:
        raise ConversionNotPossibleException(f"Conversion from {fromUnit} to {toUnit} is not possible.")
