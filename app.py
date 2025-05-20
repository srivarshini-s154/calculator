from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    expression = ""
    result = ""

    if request.method == 'POST':
        expression = request.form.get('expression', '')

        # Replace symbols with Python equivalents
        expression = expression.replace('×', '*').replace('÷', '/').replace('^', '**')

        try:
            # Evaluate the expression safely
            result = str(eval(expression))
        except ZeroDivisionError:
            result = "Error: Cannot divide by 0"
        except Exception:
            result = "Invalid Expression"

    return render_template('calculator.html', expression=expression, result=result)


if __name__ == '__main__':
    app.run(debug=True)
