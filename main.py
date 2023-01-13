import pandas as pd 
from fastapi import FastAPI,File,UploadFile,Form
import pandas as pd
import requests
import json


app = FastAPI() 

api_key = "e6f59815d4499acd64cf75a65e8e4e7b"

@app.post("/getPollutionData") 
def getpollutionData(latitude:str=Form(),longitude:str=Form()):
    url = "http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={APIKEY}".format(lat=latitude,lon=longitude,APIKEY=api_key) 
    try:
        resp =requests.get(url)
        resp = resp.json()
        return resp 
    except Exception as e:
        return {"code":404,"message":"error occurs "+repr(e)}
   

@app.get("/getCurrentWeather/{latitude}/{longitute}") 
def getCurrentWeather(latitude:str,longitude:str):
    print(latitude)
    print(longitude)
    url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIKEY}".format(lat=latitude,lon=longitude,APIKEY=api_key) 
    try:
        resp =requests.get(url)
        resp = resp.json()
        return resp 
    except Exception as e:
        return {"code":404,"message":"error occurs "+repr(e)}
   

        
    
    