import sqlalchemy.exc
from fastapi import APIRouter, Depends, status, HTTPException
from src.database_config.dependencies import get_session
from .schemas import UserOut, UserIn
from .dependencies import *
from .config import AuthSettings


auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}}
)


@auth_router.get('/', response_model=list[UserOut])
def get_users(db: Session = Depends(get_session)):
    users = db.query(User).all()
    return users


@auth_router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserOut)
def add_user(user: UserIn, db: Session = Depends(get_session)):
    new_user = User(**user.dict())
    db.add(new_user)
    try:
        db.commit()
        db.refresh(new_user)
    except sqlalchemy.exc.SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=e.__context__.__str__())
    return new_user

