from flask import Flask, render_template, request

app = Flask(__name__)

def convert_units(value, from_unit, to_unit):
    conversions = {
        'meter': {'kilometer': value / 1000, 'centimeter': value * 100},
        'kilogram': {'gram': value * 1000, 'pound': value * 2.20462},
        'celsius': {'fahrenheit': (value * 9/5) + 32, 'kelvin': value + 273.15}
    }
    return conversions.get(from_unit, {}).get(to_unit, "Conversión no válida")

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            value = float(request.form['value'])
            from_unit = request.form['from_unit']
            to_unit = request.form['to_unit']
            result = convert_units(value, from_unit, to_unit)
        except ValueError:
            result = "Error en la entrada: asegúrate de que los valores sean numéricos."
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)