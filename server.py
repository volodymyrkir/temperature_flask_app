"""This module contains server implementation"""
from flask import Flask, render_template, request, redirect, url_for
from zeep import Client

from business_logic import (convert_fahrenheit_celsius,
                            convert_celsius_fahrenheit,
                            get_weather_dict)
from consts import (DEFAULT_FAHRENHEIT_CELSIUS,
                    DEFAULT_CELSIUS_FAHRENHEIT,
                    WSD_URL)


app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static_files'
)

client = Client(WSD_URL)


@app.route('/', methods=['GET', 'POST'])
def index():
    conv_type = DEFAULT_CELSIUS_FAHRENHEIT['conversion_type_val']
    try:
        conv_type = request.args['conversion_type_val']
    except KeyError:
        pass

    selected_dict = (DEFAULT_CELSIUS_FAHRENHEIT
                     if conv_type == 'celsius_to_fahrenheit'
                     else DEFAULT_FAHRENHEIT_CELSIUS)
    selected_dict['weather_data'] = get_weather_dict()
    print(selected_dict)
    if request.method == 'POST':
        temperature = float(request.form['temperature'])
        if conv_type == 'celsius_to_fahrenheit':
            result = convert_celsius_fahrenheit(client, temperature)
        else:
            result = convert_fahrenheit_celsius(client, temperature)

        return render_template(
            'index.html',
            temperature=temperature,
            result=result,
            conversion_type_val=conv_type,
            weather_data=selected_dict['weather_data']
        )

    return render_template('index.html', **selected_dict)


@app.route('/switch_conversion', methods=['POST'])
def switch_conversion():
    conversion_type = request.form['conversion_type']

    if conversion_type == 'fahrenheit_to_celsius':
        return redirect(url_for('index',
                                conversion_type_val='fahrenheit_to_celsius'))
    else:
        return redirect(url_for('index',
                                conversion_type_val='celsius_to_fahrenheit'))


@app.template_filter('to_float')
def to_float(s):
    try:
        return float(s)
    except ValueError:
        return None


if __name__ == '__main__':
    app.run()
