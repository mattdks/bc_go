from flask import Flask, render_template, request
import pandas as pd
import random

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

    return bigdict

def nine_events(dict):
    events=[]
    for key in dict:
        for i in range(3):
            pt=random.randint(1,4)
            events.append((dict[key][pt][random.randint(0,len(dict[key][pt])-1)],pt))
    random.shuffle(events)
    return events




app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    result1 = None
    event0 = None
    event1 = None
    event2 = None
    event3 = None
    event4 = None
    event5 = None
    event6 = None
    event7 = None
    event8 = None

    dict=sort_data()
    e=nine_events(dict)
    events=[]
    for i in e:
        s=i[0]+" - "+str(i[1])+" points"
        events.append(s)

    if request.method == 'POST':
        # Example: Replace this with your custom Python code
        result1 = ''
        event0=events[0]
        event1=events[1]
        event2=events[2]
        event3=events[3]
        event4=events[4]
        event5=events[5]
        event6=events[6]
        event7=events[7]
        event8=events[8]
    return render_template('index.html', result=result1,event0=event0,event1=event1,event2=event2,event3=event3,event4=event4,event5=event5,event6=event6,event7=event7,event8=event8)

if __name__ == '__main__':
    app.run(debug=True)