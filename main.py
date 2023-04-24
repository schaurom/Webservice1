# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, request

app = Flask(__name__)

@app.route('/multiply')
def multiply():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = a * b
    return str(result)

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm sdfsdf')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
