from flask import Flask, render_template
from kiteconnect import KiteConnect

app = Flask(__name__)

# Replace with your actual API key and API secret
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/place_order', methods=['POST'])
def place_order():
    kite = KiteConnect(api_key=api_key)
    request_token = "YOUR_REQUEST_TOKEN"  # Manually input the request token obtained from Zerodha's authorization
    data = kite.generate_session(request_token, api_secret=api_secret)
    access_token = data["access_token"]
    kite.set_access_token(access_token)

    # Define order details
    order_details = {
        "tradingsymbol": "INFY",
        "exchange": "NSE",
        "transaction_type": "BUY",
        "quantity": 1,
        "order_type": "MARKET",
        "price": None,
        "product": "CNC"
    }

    # Place the order
    try:
        order_id = kite.place_order(variety=kite.VARIETY_REGULAR, order_params=order_details)
        result = "Order placed successfully. Order ID: " + str(order_id)
    except Exception as e:
        result = "Error placing order: " + str(e)

    return result
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000,  debug=True)
