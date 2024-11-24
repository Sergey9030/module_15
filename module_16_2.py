from fastapi import FastAPI, Path


app = FastAPI()


@app.get("/")  # http://127.0.0.1:8000
async def main_page() -> dict:
    return {"message": "Главная страница"}


@app.get("/admin")  # http://127.0.0.1:8000/admin
async def admin_page() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")  # http://127.0.0.1:8000/user/25
async def user_page1(user_id: int = Path(ge=1, le=100, description="Enter User ID", example="25")) -> dict:
    return {"message": f"Вы вошли как пользователь {user_id}"}


@app.get("/user/{username}/{age}")  #http://127.0.0.1:8000/user/Serg/59
async def user_page2(username: str = Path(min_length=5, max_length=20, description="Enter username", example="John"),
                     age: int = Path(ge=18, le=120, description="Enter age", example="25")) -> dict:
    return {"message": f"Информация о пользователе. Имя:{username}, Возраст:{age}."}

