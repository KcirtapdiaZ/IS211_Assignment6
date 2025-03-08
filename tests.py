import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit, convertFahrenheitToCelsius, convertFahrenheitToKelvin, convertKelvinToCelsius, convertKelvinToFahrenheit

class TestConversions(unittest.TestCase):
    
    def test_convertCelsiusToKelvin(self):
        test_cases = [
            (0.0, 273.15),  # 0°C -> 273.15K
            (100.0, 373.15), # 100°C -> 373.15K
            (-273.15, 0.0),  # Absolute zero -> 0K
            (25.0, 298.15),  # Room temperature -> 298.15K
            (300.0, 573.15)  # High temperature -> 573.15K
        ]
        
        for celsius, expected_kelvin in test_cases:
            result = convertCelsiusToKelvin(celsius)
            self.assertAlmostEqual(result, expected_kelvin, places=2)
            
    def test_convertCelsiusToFahrenheit(self):
        test_cases = [
            (0.0, 32.0),    # 0°C -> 32°F
            (100.0, 212.0), # 100°C -> 212°F
            (-40.0, -40.0), # -40°C -> -40°F (special case)
            (25.0, 77.0),   # Room temperature -> 77°F
            (300.0, 572.0)  # High temperature -> 572°F
        ]
        
        for celsius, expected_fahrenheit in test_cases:
            result = convertCelsiusToFahrenheit(celsius)
            self.assertAlmostEqual(result, expected_fahrenheit, places=2)

    def test_convertFahrenheitToCelsius(self):
        test_cases = [
            (32.0, 0.0),    # 32°F -> 0°C
            (212.0, 100.0), # 212°F -> 100°C
            (-40.0, -40.0), # -40°F -> -40°C
            (77.0, 25.0),   # 77°F -> 25°C
            (572.0, 300.0)  # 572°F -> 300°C
        ]
        
        for fahrenheit, expected_celsius in test_cases:
            result = convertFahrenheitToCelsius(fahrenheit)
            self.assertAlmostEqual(result, expected_celsius, places=2)
            
    def test_convertFahrenheitToKelvin(self):
        test_cases = [
            (32.0, 273.15),   # 32°F -> 273.15K
            (212.0, 373.15),  # 212°F -> 373.15K
            (-40.0, 233.15),  # -40°F -> 233.15K
            (77.0, 298.15),   # 77°F -> 298.15K
            (572.0, 573.15)   # 572°F -> 573.15K
        ]
        
        for fahrenheit, expected_kelvin in test_cases:
            result = convertFahrenheitToKelvin(fahrenheit)
            self.assertAlmostEqual(result, expected_kelvin, places=2)
            
    def test_convertKelvinToCelsius(self):
        test_cases = [
            (273.15, 0.0),    # 273.15K -> 0°C
            (373.15, 100.0),  # 373.15K -> 100°C
            (0.0, -273.15),   # 0K -> -273.15°C
            (298.15, 25.0),   # 298.15K -> 25°C
            (573.15, 300.0)   # 573.15K -> 300°C
        ]
        
        for kelvin, expected_celsius in test_cases:
            result = convertKelvinToCelsius(kelvin)
            self.assertAlmostEqual(result, expected_celsius, places=2)
            
    def test_convertKelvinToFahrenheit(self):
        test_cases = [
            (273.15, 32.0),    # 273.15K -> 32°F
            (373.15, 212.0),   # 373.15K -> 212°F
            (0.0, -459.67),    # 0K -> -459.67°F
            (298.15, 77.0),    # 298.15K -> 77°F
            (573.15, 572.0)    # 573.15K -> 572°F
        ]
        
        for kelvin, expected_fahrenheit in test_cases:
            result = convertKelvinToFahrenheit(kelvin)
            self.assertAlmostEqual(result, expected_fahrenheit, places=2)
            
if __name__ == "__main__":
    unittest.main()
