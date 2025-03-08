import unittest
from conversions import (
    convertCelsiusToKelvin, convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius, convertFahrenheitToKelvin,
    convertKelvinToCelsius, convertKelvinToFahrenheit
)

class TestTemperatureConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        test_cases = [
            (300.0, 573.15),  
            (0.0, 273.15),    
            (-273.15, 0.0),   
            (100.0, 373.15),  
            (-100.0, 173.15)  
        ]
        for celsius, expected_kelvin in test_cases:
            result = convertCelsiusToKelvin(celsius)
            self.assertAlmostEqual(result, expected_kelvin, places=2)

    def test_convertCelsiusToFahrenheit(self):
        test_cases = [
            (300.0, 572.0),   
            (0.0, 32.0),      
            (-273.15, -459.67),
            (100.0, 212.0),   
            (-100.0, -148.0)  
        ]
        for celsius, expected_fahrenheit in test_cases:
            result = convertCelsiusToFahrenheit(celsius)
            self.assertAlmostEqual(result, expected_fahrenheit, places=2)

    def test_convertFahrenheitToCelsius(self):
        test_cases = [
            (572.0, 300.0),
            (32.0, 0.0),
            (-459.67, -273.15),
            (212.0, 100.0),
            (-148.0, -100.0)
        ]
        for fahrenheit, expected_celsius in test_cases:
            result = convertFahrenheitToCelsius(fahrenheit)
            self.assertAlmostEqual(result, expected_celsius, places=2)

    def test_convertFahrenheitToKelvin(self):
        test_cases = [
            (572.0, 573.15),
            (32.0, 273.15),
            (-459.67, 0.0),
            (212.0, 373.15),
            (-148.0, 173.15)
        ]
        for fahrenheit, expected_kelvin in test_cases:
            result = convertFahrenheitToKelvin(fahrenheit)
            self.assertAlmostEqual(result, expected_kelvin, places=2)

    def test_convertKelvinToCelsius(self):
        test_cases = [
            (573.15, 300.0),
            (273.15, 0.0),
            (0.0, -273.15),
            (373.15, 100.0),
            (173.15, -100.0)
        ]
        for kelvin, expected_celsius in test_cases:
            result = convertKelvinToCelsius(kelvin)
            self.assertAlmostEqual(result, expected_celsius, places=2)

    def test_convertKelvinToFahrenheit(self):
        test_cases = [
            (573.15, 572.0),
            (273.15, 32.0),
            (0.0, -459.67),
            (373.15, 212.0),
            (173.15, -148.0)
        ]
        for kelvin, expected_fahrenheit in test_cases:
            result = convertKelvinToFahrenheit(kelvin)
            self.assertAlmostEqual(result, expected_fahrenheit, places=2)

if __name__ == "__main__":
    unittest.main()
