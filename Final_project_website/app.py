from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def man():
    return render_template('index.html')

@app.route('/predict')
def ma():
    return render_template('home_page.html')


@app.route('/predict1',methods = ['POST'])
def home():
    data1=float(request.form['a'])
    data2=float(request.form['b'])
    data3=float(request.form['c'])
    data4=float(request.form['d'])
    data5=float(request.form['i'])
    #data6=request.form['f']
    #data7=request.form['g']
    #data8=request.form['h']
    #data9=request.form['i']
    arr = np.array([[data1,data2,data3,data4,data5]])
    print(data1)
    pred = model.predict(arr)
    #pr=pred[0]
    return render_template('form.html', data =pred)

if __name__ == "__main__":
    app.run(debug=True)