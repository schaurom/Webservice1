import webbrowser
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/multiply')
def multiply():
    a = request.args.get('a')
    b = request.args.get('b')

    if a is None or b is None:
        return 'Error: a an b are required parameters.'

    try:
        a=int(a)
        b=int(b)
    except ValueError:
        return 'Error: a and b must be integers.'

    result = a * b
    return render_template('result.html', a=a, b=b, result=result)

if __name__ == '__main__':
    # Öffne den Browser und navigiere zur Anwendungsseite
    webbrowser.open('http://localhost:5000')
    #starte app
    app.run()

