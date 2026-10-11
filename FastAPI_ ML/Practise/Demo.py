from fastapi import FastAPI

app = FastAPI() # create an object of fastapi

@app.get("/") #defining URL / Route / PATH

def hello():
    return {'message' : 'This is my first api'}


@app.get("/about") # Defining aother route

def about():
    return {'message' : 'I am a SWE student . Learning AI/ML'}


@app.get("/address") #Defining  address route

def address():
    return {'message' : 'I am a resident of YKSG-1 ,Daffodil International University,Savar , Dhaka'}