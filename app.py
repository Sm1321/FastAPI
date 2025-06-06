from fastapi import FastAPI
import json


app = FastAPI()




def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
    return data


@app.get('/')
def hello():
    return {'messages':"Paitent Managemnet system API"}



@app.get('/about')
def about():
    return {'massage':'A fully Functional API to manage your paitent Records'}



@app.get('/view')
def view():
    data = load_data()
    return data 