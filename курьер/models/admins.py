import sqlalchemy
from database.db_session import SqlAlchemyBase


class Admins(SqlAlchemyBase):
    __tablename__ = 'admin'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, nullable=True)
    admin_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)