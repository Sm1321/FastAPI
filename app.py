from fastapi import FastAPI,Path,HTTPException,Query
import json
from pydantic import BaseModel,
from typing import Annotated,Optional,List,Dict,Field,Literal 


class Patient(BaseModel):
    id : Annotated[str,Field(...,description = 'ID of the Patient',examples = ['P001'])]
    name : Annotated[str,Field(...,description = 'city Where the patient id Living' )]
    gender : Annotated[int,Literal['male','female','others'],Field(...,description = 'Gender of the person')]
    city:Annotated[str,Field(...,description = "City of the Person")]
    age : Annotated[int,Field(...,gt =0,lt = 120,decription = 'Age of the patient')]
    height :Annotated[float,Field(...,gt = 0,description = 'Height of the pateinet on mtrs]')] 
    weight:Annotated[float,Field(...,gt = 0,description = 'Weight of the patinet in kgs')]
    


#####################################################################
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
    raise HTTPException(status_code = 404,detail = "Paitent Not Found")
    # return {'error':'Paitent Details Not found'}


@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')
    
    data = load_data()

    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data