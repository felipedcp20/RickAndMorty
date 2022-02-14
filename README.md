
### Steps: 
  


1. create a virtual env: 

```python3.8 -m venv venv```

2. Activate the virtual env: 

```source venv/bin/activate```

3. Run requirements:

```pip install -r requirements.txt``` 

4. Run the api with :

```uvicorn main:app --reload``` 

5. The endpoints names: 
   -http://127.0.0.1:8000/name
   -http://127.0.0.1:8000/location
   -http://127.0.0.1:8000/episode

6. you can use openAPI to use the api and pass arguments to the endpoints
    - http://127.0.0.1:8000/docs

7. All 200 responses return the Json in a ```.zip``` with the name of the endpoint used and the time 
