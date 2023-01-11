import pandas as pd 
from fastapi import FastAPI,File,UploadFile,Form
import pandas as pd
import requests
import json


app = FastAPI() 


@app.get("/getallemployee") 
def getEmployeeData():
    # https://dummy.restapiexample.com/api/v1/employees 
    resp = requests.get("https://dummy.restapiexample.com/api/v1/employees").json()
    
    return resp["data"]

@app.get("/getEmployeeDetails/{id}")
def getEmployeeDetails(id:int): 
    url = "https://dummy.restapiexample.com/api/v1/employee/{id}".format(id=id)
    resp = requests.get(url).json() 
    return resp["data"] 

    

