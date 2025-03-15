import sqlalchemy
from database.db_session import SqlAlchemyBase


class Users(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, nullable=True)
    user_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)