from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
import token_gen, models, schemas
from hashing import Hash

router = APIRouter(
    prefix='/login',
    tags=['Login']
)

@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Query the user from the database
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User Not Found..!")

    # Verify password using the hashing utility
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Wrong Password Try Again..!")

    # Generate JWT token for the authenticated user
    access_token = token_gen.create_access_token(data={"sub": user.email})
    return schemas.Token(access_token=access_token, token_type="bearer")
