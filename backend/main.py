import requests
from fastapi import FastAPI

app = FastAPI()

AWS_LAMBDA_URL = "http://lambda:8080/2015-03-31/functions/function/invocations"

@app.post("/analyze/")
def analyze_text(text: str):
    payload = {"body": {"text": text}}
    response = requests.post(AWS_LAMBDA_URL, json=payload)
    return response.json()
