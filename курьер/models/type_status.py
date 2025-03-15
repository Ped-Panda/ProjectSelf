import sqlalchemy
from database.db_session import SqlAlchemyBase


class TypeStatus(SqlAlchemyBase):
    __tablename__ = 'type_status'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, nullable=True)
    status = sqlalchemy.Column(sqlalchemy.String, nullable=True)