from flask import Flask, render_template
app = Flask(__name__)
# We can also add CSS tags to this
@app.route('/')
def home():
    # return 'VISHNU'
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about-us.html')

if __name__ == '__main__':
    app.run(debug=True)