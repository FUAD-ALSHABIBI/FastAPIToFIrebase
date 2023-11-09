from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models import Fruit
import firebase
# app instance
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello worlds"}

@app.post("/addFruit")
async def add(fruit:Fruit):
    print(fruit)
    f = jsonable_encoder(fruit)
    print(f)
    firebase.setData(f)
    return {'msg': 'successfuly'}