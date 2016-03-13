from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/img')
def images():
    return send_from_directory('static/img', "main.jpg")

@app.route('/py/<path:filename>')
def py_file(filename):
    return send_from_directory('py', "filename")

#@app.route('/favicon.ico')
#def index():
#    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
