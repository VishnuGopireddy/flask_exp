from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello VISHNU, welcome to Flask'

@app.route('/about')
def about():
    return 'I am Vishnu'

if __name__ == '__main__':
    app.run(debug=True)