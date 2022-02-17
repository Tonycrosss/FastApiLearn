from typing import List

from fastapi import FastAPI, Query, Path
from models.schemas import Book

app = FastAPI()

@app.get('/')
def home():
    return {'key': 'Hello'}

@app.get('/user/{pk}/items/{item}/')
def get_user_item(pk: int, item: str):
    return {'user': pk, 'item': item}

@app.post('/book')
def create_book(item: Book):
    return item

@app.get('/book')
def get_book(q: List[str] = Query(['test1', 'test2'], min_length=2, max_length=5, description='Search book')): # ... - required
    return q

@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=20), pages: int = Query(None, gt=10, le=500)):
    return {'pk': pk, 'pages': pages}