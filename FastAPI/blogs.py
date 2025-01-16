from fastapi import APIRouter,Depends,status,HTTPException
from database import get_db
from sqlalchemy.orm import Session
import models,schemas
from authentication import get_current_user
from typing import List

router = APIRouter(
    prefix='/blog',
    tags=['Blog']

)


@router.post('/',response_model=schemas.Created_Blog)
def create(request:schemas.Blog,current_user: str = Depends(get_current_user),db:Session=Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == current_user).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User Not Found')

    new_blog = models.Blog(title=request.title,body=request.body,user_id = user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


@router.get('/',response_model=schemas.Show_Blog_With_Creator)
def show_blog(id,current_user:str=Depends(get_current_user),db:Session=Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == current_user).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User not Found..!')

    blog = db.query(models.Blog).filter(models.Blog.id==id).first()

    if not blog or blog.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found..!')
    else:
        blog_response = schemas.Show_Blog_With_Creator(
        creator=schemas.Created_User(name=user.name, email=user.email),
        blogs=schemas.Blog(title=blog.title, body=blog.body)
    )
        return blog_response


@router.delete('/')
def delete(id,current_user:str=Depends(get_current_user),db:Session=Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == current_user).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User not Found..!')
    
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog or blog.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found..!')
    else:
        db.delete(blog)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'Blog Deleted Successfully..!')


@router.put('/')
def update(id,request:schemas.Blog,current_user:str=Depends(get_current_user),db:Session=Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == current_user).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User not Found..!')
    

    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if not blog or blog.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Blog with id {id} not found..!')
    else:
        blog.title = request.title
        blog.body = request.body        
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK,
                            detail=f'Blog Updated Successfully..!')