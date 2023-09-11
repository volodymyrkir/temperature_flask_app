"""This module contains logic for interaction of server wth SOAP service"""
import requests
from zeep import Client

from consts import API_URL


def convert_fahrenheit_celsius(client: Client, value: float) -> float:
    """
    Converts given fahrenheit value to celsius using soap client.
    :param client: SOAP client
    :param value: fahrenheit value
    :return: celsius value
    """
    return round(
        float(client.service.FahrenheitToCelsius(Fahrenheit=value)),
        1
    )


def convert_celsius_fahrenheit(client: Client, value: float) -> float:
    """
    Converts given celsius value to fahrenheit using soap client.
    :param client: SOAP client
    :param value: celsius value
    :return: fahrenheit value
    """
    return round(
        float(client.service.CelsiusToFahrenheit(Celsius=value)),
        1
    )


def get_weather_dict() -> dict[str, tuple]:
    """
    Parses weather API results on some big cities.
    :return: Dict of cities with current temp in c and f measures.
    """
    cities = ['London', 'New York', 'Kyiv', 'Warsaw',
              'Helsinki', 'Brazilia', 'Sydney', 'Peking']
    temps_dict = {}
    for city in cities:
        answer = requests.get(API_URL + city).json()['current']
        temp_c, temp_f = answer['temp_c'], answer['temp_f']
        temps_dict[city] = temp_c, temp_f

    return temps_dict
