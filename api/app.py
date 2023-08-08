from fastapi import FastAPI
from http import HTTPStatus

app = FastAPI()


@app.get('/user/', status_code=HTTPStatus.OK)
async def get_user():
    return 'User'


@app.post('/user/create/', status_code=HTTPStatus.CREATED)
async def creat_user():
    return 'Created!'
