from flask import Flask, render_template, request
import pandas as pd

def sort_data():
    df = pd.read_csv('testdata1.csv')
    categories = df["Category"]
    points = df["Points"]
    mission = df["Mission"]
    bigdict={}
    for i in range(1,4):
        cat=categories[i*int(len(categories)/3)]
        bigdict[cat]={1:[],2:[],3:[],4:[]}
    for i in range(len(categories)):
        print()
        bigdict[categories[i]][int(points[i])].append(mission[i])

    return str(bigdict)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    result = None
    if request.method == 'POST':
        # Example: Replace this with your custom Python code
        result = sort_data()
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)