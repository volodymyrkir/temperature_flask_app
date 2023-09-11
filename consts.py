"""This module contains constants for whole project"""
import dotenv

import os

dotenv.load_dotenv()

WSD_URL = 'https://www.w3schools.com/xml/tempconvert.asmx?WSDL'

API_KEY = os.environ.get('API_KEY')

API_URL = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q='

DEFAULT_CELSIUS_FAHRENHEIT = {
    'conversion_type_val': 'celsius_to_fahrenheit',
    'temperature': 20.0,
    'result': 68
}
DEFAULT_FAHRENHEIT_CELSIUS = {
    'conversion_type_val': 'fahrenheit_to_celsius',
    'temperature': 68,
    'result': 20.0
}
