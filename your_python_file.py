from flask import Flask

app = Flask(__name__)
print('Hallo')

@app.route('/multiply')
def multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = a * b
    return str(result)

if __name__ == '__main__':
    app.run()
