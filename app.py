from flask import Flask, render_template, request
import pandas as pd
import random
import json

def sort_data():
    df = pd.read_csv('testdata3.csv')
    categories = df["Type"]
    ids = df["ID"]
    points = df["Points"]
    mission = df["Mission"]
    bigdict={}
    for i in range(1,4):
        cat=categories[i*int(len(categories)/3)]
        bigdict[cat]={1:[],2:[],3:[],4:[]}
    for i in range(len(categories)):
        print()
        bigdict[categories[i]][int(points[i])].append((mission[i],ids[i]))

    return bigdict

def nine_events(dict):
    events=set()
    key1=list(dict.keys())[0]
    key2=list(dict.keys())[1]
    key3=list(dict.keys())[2]

    while len(events)<3:
        n=random.randint(1,4)
        x=random.randint(0,len(dict[key1][n])-1)
        events.add((dict[key1][n][x][0],dict[key1][n][x][1]))
    while len(events)<6:
        n=random.randint(1,4)
        x=random.randint(0,len(dict[key2][n])-1)
        events.add((dict[key2][n][x][0],dict[key2][n][x][1]))
    while len(events)<9:
        n=random.randint(1,4)
        x=random.randint(0,len(dict[key3][n])-1)
        events.add((dict[key3][n][x][0],dict[key3][n][x][1]))
    
    a=list(events)
    random.shuffle(a)
    return a

dict=sort_data()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run_code', methods=['POST'])
def run_code():
    event0 = None
    event1 = None
    event2 = None
    event3 = None
    event4 = None
    event5 = None
    event6 = None
    event7 = None
    event8 = None
    id0 = None
    id1 = None
    id2 = None
    id3 = None
    id4 = None
    id5 = None
    id6 = None
    id7 = None
    id8 = None
    e=nine_events(dict)
    events=[]
    id=[]
    j=json.dumps(id)
    for i in e:
        events.append(i[0])
        id.append(i[1])

    if request.method == 'POST':
        event0=events[0]
        event1=events[1]
        event2=events[2]
        event3=events[3]
        event4=events[4]
        event5=events[5]
        event6=events[6]
        event7=events[7]
        event8=events[8]
        id0 = id[0]
        id1 = id[1]
        id2 = id[2]
        id3 = id[3]
        id4 = id[4]
        id5 = id[5]
        id6 = id[6]
        id7 = id[7]
        id8 = id[8]
        
    return render_template('index.html', event0=event0,event1=event1,event2=event2,event3=event3,event4=event4,event5=event5,event6=event6,event7=event7,event8=event8,id0=id0,id1=id1,id2=id2,id3=id3,id4=id4,id5=id5,id6=id6,id7=id7,id8=id8,id_arr=j)

if __name__ == '__main__':
    app.run(debug=True)