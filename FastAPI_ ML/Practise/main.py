from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Path
from fastapi import Query
import json

app = FastAPI() # create an object of fastapi

def load_data():
    with open('patience.json', 'r') as f:

        data = json.load(f)

        return data



@app.get("/") #defining URL / Route / PATH

def hello():
    return {'message' : 'Patient Management System API'}


@app.get("/about") # Defining aother route

def about():
    return {'message' : 'A fully functional API to manage your patient records'}


@app.get("/address") #Defining  address route

def address():
    return {'message' : 'I am a resident of YKSG-1 ,Daffodil International University,Savar , Dhaka'}


@app.get("/view")

def view():
    data = load_data()

    return data


# Route for a specific patient
@app.get("/patient/{patient_id}")

 
def view_patient( patient_id : str = Path(..., description='ID of the patient in the DB',example='P001')):
    data = load_data()  #First load all patient data

    if patient_id in data :
        return data[patient_id]

    raise  HTTPException(status_code=404, detail='Patient not found')







    ############################ Query parameter########################################


@app.get('/sort')

def sort_patients(sort_by : str= Query(...,description='Sort on the basis of height , weight or BMI')
                  
                  , order : str = Query('ascending',description='sort in ascending order')):


    valid_fields =['height','weight','BMI']

    if sort_by not in valid_fields :
        raise HTTPException(status_code= 400, detail='Invalid filed , select fron {valid_fields}')  #Bad Request


    if order not in ['ascending','descending'] :
        raise HTTPException(status_code=400,detail='Invalid order select between ascending or descending')


    data = load_data()


    sort_oreder = True if order == 'desc' else False
    sorted_data = sorted(data.values(),key=lambda x : x.get(sort_by,0) , reverse= sort_oreder)

    return sorted_data





