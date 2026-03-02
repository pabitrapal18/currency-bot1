from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()

    source_currency = data['queryResult']['parameters']['unit-currency']['currency']
    amount = data['queryResult']['parameters']['unit-currency']['amount']
    target_currency = data['queryResult']['parameters']['currency-name']

    #print(source_currency)
    #print(target_currency)
    #print(amount)

    cf = fetch_conversion_factor(source_currency, target_currency)
    #converted_amount = amount * cf

    converted_amount = amount * cf
    return {
        "fulfillmentText": f"{amount} {source_currency} = {converted_amount:.2f} {target_currency}"
    }
    #return jsonify(response)
    #print(converted_amount)
    #return str(converted_amount)



def fetch_conversion_factor(source_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/d8862b748fa88cb0d1b5ab25/pair/{source_currency}/{target_currency}"

    response = requests.get(url)
    data = response.json()

    #print(data)

    return data['conversion_rate']


if __name__ == '__main__':
    app.run(debug=True)