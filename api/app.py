from http import HTTPStatus

from fastapi import FastAPI

from models_pydantic import User

app = FastAPI()


@app.get(
    '/user/random/', response_model=User,
    response_model_exclude={'location'},
    status_code=HTTPStatus.OK
)
async def get_random_user(location: int = 10) -> User:
    """Извлекаем из БД рандомного пользователя для показа."""
    return User()


@app.post('/user/create/', status_code=HTTPStatus.CREATED)
async def creat_user(user: User) -> User:
    return user


@app.patch('/user/update/{user_id}', status_code=HTTPStatus.OK)
async def update_user(user_id: int, user: User):
    pass
