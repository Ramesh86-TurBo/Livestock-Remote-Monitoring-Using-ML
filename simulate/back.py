from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Firebase URL for the "UserData/0000" node
firebase_url = 'https://livestock-c0cf1-default-rtdb.asia-southeast1.firebasedatabase.app/UsersData/0000.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_latest_acceleration')
def get_latest_acceleration():
    # Fetch the latest accelerometer data
    response = requests.get(firebase_url)
    data = response.json() if response.ok else {'x': 'N/A', 'y': 'N/A', 'z': 'N/A'}

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
