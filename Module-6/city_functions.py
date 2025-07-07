# Author: Kyle Klausen
# Date: 06/27/25
# Assignment 7_2
# Description: Defines a function that formats city and country names, optionally 
# including population and language details, then prints examples.

#city_functions.py

def city_country(city, country, population=None, language=None):
    """Return 'City, Country' with optional population and language."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result

# Test function calls
if __name__ == "__main__":
    print(city_country("santiago", "chile"))
    print(city_country("tokyo", "japan", 13929286))
    print(city_country("paris", "france", 2140526, "french"))