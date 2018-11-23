from flask import Flask, redirect
app = Flask(__name__)
@app.route("/bmi/<weight>/<height>")
def bmi(weight,height):
    m = int(height)/100
    BMI = int(weight)/(m*m)

    if BMI < 16:
        return "Severely underweight"
    elif BMI < 18.5:
        return "underweight"
    elif BMI < 25:
        return "Normally"
    elif BMI < 30:
        return "overweight"
    else:
        return "obese"
if __name__ == "__main__":
    app.run(debug=True)