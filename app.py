import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

def get_price(total_quantity, price_per_bag, quantity_per_bag):
    kgs = int((total_quantity % int(total_quantity)) * 100) #8.23 --> .23
    print(kgs/quantity_per_bag + int(total_quantity))
    return (kgs/quantity_per_bag + int(total_quantity)) * price_per_bag

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    total_quantity, price_per_bag, quantity_per_bag = [float(x) for x in request.form.values()]
    output = get_price(total_quantity, price_per_bag, quantity_per_bag)
    output = round(output, 3)
    return render_template('index.html', prediction_text='Total cost for {} at {} be ₹{}'.format(total_quantity,
                                                                                                  price_per_bag, output))

if __name__ == "__main__":
    app.run(debug=True)
