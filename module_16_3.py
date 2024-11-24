from fastapi import FastAPI, Path

#  python -m uvicorn main:app

app = FastAPI()


users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")  # Весь словарь messages_db
async def get_all_dict() -> dict:
    return users


@app.post("/user/{username}/{age}")  # Добавляем юзера
async def post_user(username: str = Path(min_length=5, max_length=20, description="Enter username", example="John"),
                    age: int = Path(ge=18, le=120, description="Enter age", example="25")) -> str:
    new_index = str(int(max(users, key=int)) + 1)
    users[new_index] = f'Имя: {username}, возраст: {age}'
    return f"Пользователь:{username}, id={new_index} успешно добавлен."


@app.put("/user/{user_id}/{username}/{age}")  # Обновляем юзера по id
async def put_user(user_id: str, username: str = Path(min_length=5, max_length=20, description="Enter username", example="John"),
                   age: int = Path(ge=18, le=120, description="Enter age", example="25")) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f"Пользователь:{username}, id={user_id} успешно обновлен."


@app.delete("/user/{user_id}")  # Удаляем юзера по id
async def put_user(user_id: str) -> str:
    i = user_id
    users.pop(user_id)
    return f"Пользователь id={i} успешно удален."
