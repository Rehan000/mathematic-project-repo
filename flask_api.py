from flask import Flask
import mathematics

app = Flask(__name__)


@app.route('/math/<num>')
def math_func(num):
    ob1 = mathematics.Mathematics(int(num))
    result_dict = {"Number": int(num),
                   "Factorial": ob1.factorial(),
                   "Square": ob1.square(),
                   "Cube": ob1.cube(),
                   "Square Root": ob1.square_root()}
    return str(result_dict)
