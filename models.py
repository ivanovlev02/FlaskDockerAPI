# Импорты ниже требуются для создания моделей и работой с БД

from sqlalchemy.orm import relationship  # род. класс для создания моделей
from sqlalchemy import create_engine  # создание движка для подключения к БД
from sqlalchemy.orm import sessionmaker, DeclarativeBase  # создание сессии подключения
import sqlalchemy as sq
import os
from dotenv import load_dotenv  # нужен для использования переменных окр.

load_dotenv()
user = 'netology_flask'
password = 'netology'
db = 'db_postgres'

engine = create_engine('postgresql://{user}:{password}@127.0.0.1:5431/{db}')
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = 'owners'

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    name = sq.Column(sq.String(50), nullable=False, unique=True)
    user_pass = sq.Column(sq.String(100), nullable=False, unique=True)


class Advertisement(Base):

    __tablename__ = 'advertisements'

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True)
    header = sq.Column(sq.Text, nullable=False)
    desc = sq.Column(sq.Text, nullable=True)
    created_at = sq.Column(sq.DateTime, server_default=sq.func.now())
    owner_id = sq.Column(sq.Integer, sq.ForeignKey('owners.id'), nullable=False)

    owner = relationship('User', backref='advertisements')


Base.metadata.create_all(bind=engine)
