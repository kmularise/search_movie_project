from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
import sys
import urllib.request
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],#정규식, '*'에 의해 어떤 서버가 와도 안전하다. #origins 잘 조작하면 될 수도.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/coffee")
def get_coffee():
    return {"Coffee_list" : ['Americano', 'Caffe Latte']}

@app.get("/items/{item_id}")
def read_item(item_id, q: Union[str, None] = None):
    print(item_id)
    item_id = 100
    return {"item_id": item_id, "q": q}

@app.get("/naver/api/{item}")
def naver_api(item):
    client_id = "PjzbnOIph6qc3QDqKr7v"
    client_secret = "vZRdjAxmbG"
    encText = urllib.parse.quote(str(item))
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    
    if(rescode==200):
        response_body = response.read()
        answer = json.loads(response_body.decode('utf-8'))
    else:
        print("Error Code:" + rescode)
    return answer

