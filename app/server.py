from fastapi import FastAPI
import numpy as np


class_names = ['Class A', 'Class B', 'Class C']

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Classification API!"}

