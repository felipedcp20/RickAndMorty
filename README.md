
### Steps: 
  
1. Install python 3.8
https://www.python.org/downloads/

2. create a virtual env: 

```python3.8 -m venv venv```

3. Activate the virtual env: 

```source venv/bin/activate```

4. Run requirements:

```pip install -r requirements.txt``` 

5. Run the api with :

```uvicorn main:app --reload``` 

6. The endpoints names: 
   -http://127.0.0.1:8000/name
   -http://127.0.0.1:8000/location
   -http://127.0.0.1:8000/episode

7. you can use openAPI to use the api and pass arguments to the endpoints
    - http://127.0.0.1:8000/docs

8. All 200 responses return the Json in a ```.zip``` with the name of the endpoint used and the time 
