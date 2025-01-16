from pydantic import BaseModel
from typing import List

class User(BaseModel):
    
    name : str
    email : str
    password : str

class Created_User(BaseModel):
    name : str
    email: str

class Show_User(BaseModel):
    id:int
    name :str
    email:str

    class Config():
        orm_mode = True

    

class Login(BaseModel):
    email:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email : str 


class Blog(BaseModel):
    title:str
    body:str



class Created_Blog(BaseModel):
    user_id:int
    id:int
    title:str
    body:str

class Show_Blog(BaseModel):
    id:int
    title:str
    body:str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "title": "My First Blog Post",
                "body": "This is the content of the blog post."
            }
        }


class Show_Blog_With_Creator(BaseModel):
    creator: Created_User
    blogs: Blog

    class Config:
        orm_mode = True

class All_Blog(BaseModel):
    creator : Created_User
    blogs : List[Show_Blog]

    class Config():
        orm_mode = True

    