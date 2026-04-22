from fastapi import FastAPI
from app.api.routers.tasks import router as task_router

app = FastAPI(
    title="Todo List API",
    description="""In this project you are required to develop a RESTful API to allow users to manage their to-do list. 
            The previous backend projects have only focused on the CRUD operations, but this project will require you 
            to implement user authentication as well.
            This project is the challenge [roadmap.sh](https://roadmap.sh/projects/todo-list-api)""",
    version="0.0.1",
    contact={
        "name": "Mr YABA LOUO JEAN DE DIEU",
        "url": "https://portfolio-eight-dun-30.vercel.app",
        "email": "gauisyaba@gmail.com",
        "github": "https://github.com/victoire20"
    }
)


app.include_router(task_router)