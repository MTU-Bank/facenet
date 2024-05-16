from fastapi import FastAPI
from model import get_predict


app = FastAPI()

@app.get('/')
def home():
    return {'result': 'OK'}

@app.post('/predict')
def predict(data: dict):  # data:{"path": [path_img1, path_img2]}
    paths = data['path']
    result = get_predict(paths)
    return result