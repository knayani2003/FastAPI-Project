from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

engine = create_engine('postgresql://postgres:password@localhost:yourport/database',echo=True)

Session = sessionmaker(bind=engine)

Base = declarative_base()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()