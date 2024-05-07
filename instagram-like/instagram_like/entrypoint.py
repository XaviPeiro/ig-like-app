from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import schemas, models
from database import engine, SessionLocal

# Create every model extending from base in to the DB.
models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# ----- Endpoints -----
# ----- async -----


@app.get("/async")
async def root_async():
    return {"message": "Hello World"}


# ----- sync -----


@app.get("/sync")
def root_sync():
    return {"message": "Hello World"}


@app.post("/sync/user", response_model=schemas.User)
def singup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db, user)
    except Exception as e:
        a=1


@app.get("/sync/user", response_model=list[schemas.User])
def users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    try:
        return get_users(db, skip, limit)
    except Exception as e:
        a = 1


# POST an image (v1:metadata; v2:metadata+img)
@app.post("sync/image")
def post_image():
    ...


# GET logged_user images
@app.get("sync/image/{image_id}")
def get_images(image_id: int):
    ...


# ----- "Respository" -----

def create_user(db: Session, user: schemas.UserCreate):
    # fake_hashed_password = user.password + "notreallyhashed"
    # db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db_user = models.User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


