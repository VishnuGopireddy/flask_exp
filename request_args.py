from flask import Flask, render_template, request
app = Flask(__name__)
import pandas as pd

@app.route('/')
def home():
    return 'Hello VISHNU, welcome to Flask'

@app.route('/details',methods=['GET'])
def call():
    name = request.args.get('name')
    age = request.args.get('age')
    place = request.args.get('place')
    return 'name is {} and age is {} from {}'.format(name, age, place)

@app.route('/from_file',methods=['POST'])
def get_details():
    df = pd.read_csv(request.files.get('file'))
    print(df.head())
    cols = df.columns[-2]
    print(cols)
    activity = df[cols].iloc[0]
    return activity

@app.route('/from_txt', methods=['POST'])
def get_details_txt():
    file = request.files.get('file')
    print('Open file {}', file)
    with open(file,'r') as f:
        txt = f.read()
        # txt = f.read(file)
        return '''
                    <pre>{{ content }}</pre> 
                '''

@app.route('/about')
def about():
    return 'I am Vishnu'

if __name__ == '__main__':
    app.run(debug=True)