# Serve model as a flask application

import pickle
import numpy as np
from flask import Flask, render_template, request
import sklearn

model = None
app = Flask(__name__)


def load_model():
    global model
    # model variable refers to the global variable
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)


@app.route('/')
def home_endpoint():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def get_prediction():
    # Works only for a single sample
    if request.method == 'POST':
        data1 = request.form['a']
        data2 = request.form['b']
        data3 = request.form['c']
        data4 = request.form['d']
        arr = np.array([[data1, data2, data3, data4]])
        # data = arr[np.newaxis, :]  # converts shape from (4,) to (1, 4)
        prediction = model.predict(arr)  # runs globally loaded model on the data
        return render_template('home.html', prediction='Your happiness score should be {}'.format(prediction))


if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run(host='0.0.0.0', port=5000)