from flask import Flask, render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('paginap.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/testform', methods=['POST'])
def testform ():
    number_1 = int(request.form['number1'])
    number_2 = int(request.form['number2'])
    result = sum((number_1,number_2))
    print(result)
    return render_template('paginap.html',resultado=result,textolibre="puto")




if __name__ == '__main__':
    app.run(debug=True)
