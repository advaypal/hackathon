from flask import Flask, render_template, send_from_directory, request
import os
from py/data import write_img

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/img')
def images():
    return send_from_directory('static/img', "main.jpg")

@app.route('/py/data.py', methods=['POST'])
def py_file():
    return write_img(request.form.value[0])
    # return send_from_directory('py', "filename")

#@app.route('/favicon.ico')
#def index():
#    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
