import sqlalchemy
from database.db_session import SqlAlchemyBase


class Orders(SqlAlchemyBase):
    __tablename__ = 'orders'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, nullable=True)
    user = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    kurer = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    date_start = sqlalchemy.Column(sqlalchemy.String)
    date_end = sqlalchemy.Column(sqlalchemy.String)
    text_order = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    status = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

