from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
import models, schemas
from hashing import Hash
from authentication import get_current_user
from typing import List

router = APIRouter(
    prefix="/user",
    tags=['User']
)

# POST route to create a new user
@router.post('/')
def create(request: schemas.User, db: Session = Depends(get_db)):
    hash_password = Hash.get_password_has(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hash_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get('/', response_model=schemas.Show_User)
def show_user(current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    
    user = db.query(models.User).filter(models.User.email == current_user).first()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user



@router.get('/',response_model=List[schemas.All_Blog])
def all_blog(current_user:str=Depends(get_current_user),db:Session=Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == current_user).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User not Found..!')

    all_blogs = db.query(models.Blog).filter(models.Blog.user_id==user.id).all()

    if not all_blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'No Blog Found..!')

    creator_info = schemas.Show_User(id=user.id, name=user.name, email=user.email)

    blogs_info = [schemas.Blog(id=blog.id, title=blog.title, body=blog.body) for blog in all_blogs]

    blog_with_creator = [schemas.All_Blog(creator=creator_info, blogs=blogs_info)]

    return blog_with_creator