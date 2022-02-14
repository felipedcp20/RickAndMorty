import json
import requests
import zipfile
from os import remove
import time

from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/name')
def character(name: Optional[str] = None ):
    
    url = 'https://rickandmortyapi.com/api/character/'
    arg = {'name': name}
    response = requests.get(url, params=arg)
    
    if response.status_code == 200:
        response_json = json.loads(response.text)
        
        with open('data.json', 'w') as file:
            json.dump(response_json,file,indent=4)
        
        namefile = time.ctime()  
            
        with zipfile.ZipFile(f' character {namefile}.zip','w') as fzip:
            fzip.write('data.json')
            remove('data.json')   
            
        
        return response_json
    
@app.get('/location')   
def location(location: Optional[str] = None ):
    
    url = 'https://rickandmortyapi.com/api/location/'
    arg = {'name': location}
    response = requests.get(url, params=arg)
    
    if response.status_code == 200:
        response_json = json.loads(response.text)
        
        with open('data.json', 'w') as file:
            json.dump(response_json,file,indent=4)
        
        namefile = time.ctime()  
            
        with zipfile.ZipFile(f' location {namefile}.zip','w') as fzip:
            fzip.write('data.json') 
            remove('data.json')   
            
        
        return response_json
    
@app.get('/episode') 
def episode(episode: Optional[str] = None ):
    
    url = 'https://rickandmortyapi.com/api/episode/'
    arg = {'name': episode}
    response = requests.get(url, params=arg)
    
    if response.status_code == 200:
        response_json = json.loads(response.text)
        
        with open('data.json', 'w') as file:
            json.dump(response_json,file,indent=4)
        
        namefile = time.ctime()  
            
        with zipfile.ZipFile(f' episode {namefile}.zip','w') as fzip:
            fzip.write('data.json') 
            remove('data.json')   
            
        
        return response_json
                