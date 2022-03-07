#import distutils.log import debug
from flask import Flask
from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route("/sumasen/<string:a>/<string:b>")
def get_suma_sen(a):
    a = float(a)
    b = float(b)
    
    result = (2 * math.sin((a + b)/2)) * (math.cos((a - b)/2))
    
    return jsonify({"seno": result})

@app.route("/sumaseries/<string:x>/<string:n>")
def get_suma_series(x, n):
    x = int(x)
    n = int(n)
    result = 0
    sine = 0

    for i in range(n):
        sign = (-1)**i
        pi = 22/7
        y = x*(pi/180)
        sine += ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    
    result = round(sine,2)

    return jsonify({"sumas": result})

@app.route("/heron/<string:a>/<string:b>/<string:c>")
def get_formula_heron(a, b, c):
    a = int(a)
    b = int(b)
    c = int(c)

    s = (a+b+c)/2

    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    return jsonify({"area": area})

if __name__ == '__main__':
    app.run(debug = True, port=4000)
