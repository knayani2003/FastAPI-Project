from fastapi import FastAPI
import models,users,login,blogs
from database import engine
app = FastAPI()

models.Base.metadata.create_all(engine)


app.include_router(login.router)
app.include_router(users.router)
app.include_router(blogs.router)

