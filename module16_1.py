from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # http://127.0.0.1:8000
async def main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/admin")  # http://127.0.0.1:8000/admin
async def admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")  # http://127.0.0.1:8000/user/25
async def user_page1(user_id: str) -> dict:
    return {"message": f"V1. Вы вошли как пользователь {user_id}"}


@app.get("/user/{username}/{age}")  #http://127.0.0.1:8000/user/Serg/59
async def user_page2(username: str, age: int) -> dict:
    return {"message": f"V1. Информация о пользователе. Имя:{username}, Возраст:{age}."}

"""
В следующих двух функциях работает только та, которая описана раньше.
При этом при попытке выполнения запроса для второй функции он обрабатывается
первой и происходит ошибка.
"""

@app.get("/user")  # http://127.0.0.1:8000/user?username=Serg&age=59
async def user_page3(username: str, age: int) -> dict:
    return {"message": f"V2. Информация о пользователе. Имя:{username}, Возраст:{age}."}


@app.get("/user")  # http://127.0.0.1:8000/user?user_id=25
async def user_page4(user_id: str) -> dict:
    return {"message": f"V2. Вы вошли как пользователь {user_id}"}
