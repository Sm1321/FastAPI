from fastapi import FastAPI,Path
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



# @app.get('/patient/{patient_id}')
# def view_paitent_data(patient_id : str): #paitent Id is string
#     #load the All paiteints Data
#     data = load_data()
#     if patient_id in data:
#         return data[patient_id]
#     return {'error':'Paitent Details Not found'}

@app.get('/patient/{patient_id}')
def view_paitent_data(patient_id : str = Path(...,description = 'ID of the Patient DB',example = "P001")): #paitent Id is string
    #load the All paiteints Data
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    return {'error':'Paitent Details Not found'}