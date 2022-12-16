import sqlalchemy.sql.functions
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship
import sqlalchemy
from src.database_config.database import Base
from fastapi_users.db import SQLAlchemyBaseUserTableUUID


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "auth_user"

# user_group_association = Table(
#     "auth_user_group",
#     Base.metadata,
#     Column("user_id", ForeignKey("auth_user.id"), primary_key=True),
#     Column("group_id", ForeignKey("auth_group.id"), primary_key=True)
# )
#
# group_permission_association = Table(
#     "auth_group_permission",
#     Base.metadata,
#     Column("group_id", ForeignKey("auth_group.id"), primary_key=True),
#     Column("permission_id", ForeignKey("auth_permission.id"), primary_key=True)
# )
#
#
# class User(Base):
#     __tablename__ = "auth_user"
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     username = Column(String, nullable=False)
#     password = Column(String, nullable=False)
#     first_name = Column(String, nullable=False)
#     last_name = Column(String, nullable=False)
#     email = Column(String, nullable=False, index=True, unique=True)
#     last_login = Column(DateTime, nullable=True)
#     date_joined = Column(DateTime, server_default=sqlalchemy.sql.functions.now())
#     is_active = Column(Boolean, default=True, nullable=False)
#     is_superuser = Column(Boolean, default=False)
#     groups = relationship("Group", secondary=user_group_association, backref="users")
#
#
# class Group(Base):
#     __tablename__ = "auth_group"
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(String, nullable=False)
#     description = Column(String)
#     permissions = relationship("Permission", secondary=group_permission_association, backref="groups")
#
#
# class Permission(Base):
#     __tablename__ = "auth_permission"
#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     name = Column(String, nullable=False)
#     code_name = Column(String, nullable=False)
