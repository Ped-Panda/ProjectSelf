import sqlalchemy
from database.db_session import SqlAlchemyBase


class Kurers(SqlAlchemyBase):
    __tablename__ = 'kurer'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, nullable=True)
    kurer_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    free = sqlalchemy.Column(sqlalchemy.Integer)