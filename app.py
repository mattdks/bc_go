from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    result = None
    if request.method == 'POST':
        # Example: Replace this with your custom Python code
        result = "Python Code Executed Successfully!"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)