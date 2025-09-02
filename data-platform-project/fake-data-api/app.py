from flask import Flask, jsonify
from generators import generate_customers, generate_products, generate_orders

app = Flask(__name__)

@app.route('/customers')
def customers():
    return jsonify(generate_customers())

@app.route('/products')
def products():
    return jsonify(generate_products())

@app.route('/orders')
def orders():
    return jsonify(generate_orders())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)