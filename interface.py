from flask import Flask,render_template,request,jsonify
import utils

app = Flask(__name__)

@app.route('/')  #Base API
def home():
    print('Testing Home API')
    return render_template('home.html')

@app.route('/predict', methods = ['POST'])
def prediction():
    print('Testing prediction API')
    data = request.form
    if request.method == 'POST':
        print('Input data is :',data)
        x1 = float(data['SepalLengthCm'])
        x2 = float(data['SepalWidthCm'])
        x3 = float(data['PetalLengthCm'])
        x4 = float(data['PetalWidthCm'])

        prediction = utils.predict_class(x1,x2,x3,x4)

        return render_template('after.html', data=prediction)

    else:
        return jsonify({'Message':'Unsuccessful'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)