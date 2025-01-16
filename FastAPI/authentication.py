from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import token_gen  # Import your token functions
import models  # Your models should be imported here

# OAuth2PasswordBearer is used to declare the token URL
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials"
    )
    # Validate and decode the token, get the user_id from it
    user_email = token_gen.verify_token(token, credentials_exception)

    # You may retrieve the user from the database by their user_id if needed
    return user_email  # Returning only the user ID for simplicity
