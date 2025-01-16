from datetime import datetime, timedelta
from jose import JWTError, jwt
import models
from sqlalchemy.orm import Session

# Secret key and algorithm for JWT
SECRET_KEY = "your-secret-key"  # Make sure this key is stored securely, e.g., in environment variables.
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Function to create an access token
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to verify a token and retrieve the user data
def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub") 
        if user_id is None:
            raise credentials_exception
        return user_id  
    except JWTError:
        raise credentials_exception
