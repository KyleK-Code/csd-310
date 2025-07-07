# Author: Kyle Klausen
# Date: 6/27/25 
# Assignment 7_2
# Description: Uses unit test to verify the city formatting function 
# works correctly with various combinations of city, country,#population, and language.


# test_cities.py

import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    def test_city_country(self):
        self.assertEqual(city_country("santiago", "chile"), "Santiago, Chile")
        self.assertEqual(city_country("tokyo", "japan"), "Tokyo, Japan")
        self.assertEqual(city_country("paris", "france"), "Paris, France")

if __name__ == "__main__":
    unittest.main()