from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get('/')
async def main_page() -> str:
    return "Главная страница"


@app.get('/user/admin')
async def log_in_admin() -> str:
    return "Вы вошли как администратор"


@app.get('/user/{user_id}')
async def log_in_user(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get('/user')
async def info_user(username: str, age: int) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'


if __name__ == '__main__':
    uvicorn.run(app='module_16_1:app', host="127.0.0.1", port=8000, reload=True)