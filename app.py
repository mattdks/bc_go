from flask import Flask, render_template, request
import pandas as pd

def sort_data():
    try:
        df = pd.read_csv('testdata1.csv')
        points = df["Points"]
        return str(points)
    except Exception as e:
        return f"Error reading CSV: {str(e)}"

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