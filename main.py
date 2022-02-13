import json
import requests
import zipfile
from os import remove
import time

from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def character(name: str ):
    
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
            
        
        return response_json
    
    
    
