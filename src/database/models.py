from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from werkzeug.security import generate_password_hash


Base = declarative_base()

members = Table(
    'members', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('event_id', Integer, ForeignKey('events.id'), primary_key=True)
)


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    description = Column(String)
    distributed_by = Column(String(30), nullable=False)
    max_limit_members = Column(Integer)
    date = Column(Date, index=True, nullable=False)

    users = relationship('User', secondary=members, backref='events')

    def __init__(self, title, description, distributed_by, max_limit_members, date):
        self.title = title
        self.description = description
        self.distributed_by = distributed_by
        self.max_limit_members = max_limit_members
        self.date = date

    def __repr__(self):
        return f'Event({self.id}, {self.title}, {self.description}, {self.distributed_by}, {self.max_limit_members}, \
        {self.date})'

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "distributed_by": self.distributed_by,
            "max_limit_members": self.max_limit_members,
            "date": self.date.strftime("%Y-%m-%d")
        }

@dataclass
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True)
    password = Column(String(254), nullable=False)
    phone_number = Column(String(254), unique=True)
    age = Column(Integer)

    username: str
    email: str
    password: str
    phone_number: str
    age: str

    def __post_init__(self,):
        self.password = generate_password_hash(self.password)
        self.phone_number = generate_password_hash(self.phone_number)
