from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "welcome to fastapi"}
@app.get("/name")
def read_name():
    return[{"name":"java"}]
@app.get("/weather")
def read_weather(city:str):
    return{"city":city,
           "temperature":28,
           "condition":"sunny"}