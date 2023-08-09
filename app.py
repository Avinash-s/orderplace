from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/place_order', methods=['POST'])
def place_order():
    try:
        # Here, you can add the code to interact with the Zerodha Connect API
        # and place the order. Replace this with your actual logic.
        # You might want to use a more secure way to store API key and access token.
        result = "Order placed successfully"
    except Exception as e:
        result = "Error placing order: {}".format(str(e))

    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,  debug=True)
