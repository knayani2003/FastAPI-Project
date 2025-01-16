from passlib.context import CryptContext


pwd_con = CryptContext(schemes=['bcrypt'],deprecated='auto')


class Hash():
    
    def get_password_has(password):
        return pwd_con.hash(password)
    

    def verify(plain_pass,hash_pass):
        return pwd_con.verify(plain_pass,hash_pass)