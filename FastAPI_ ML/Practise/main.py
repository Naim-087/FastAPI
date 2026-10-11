from fastapi import FastAPI
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

