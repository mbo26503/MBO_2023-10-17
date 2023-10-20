# 20/10/2023 09:21
# użycie SQLAlchemy biblioteki do komunikacji z DB

from sqlalchemy import (
    Column, Integer, String, ForeignKey, create_engine
)
# pip install sqlalchemy - instalacja modułów w Pythonie

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///:memory:')  # przechowuje db w pamięci
# engine = create_engine('sqlite:///:mydatabase.db')  # przechowuje db w pliku
# konkretnych typach DB (MySQL, PostgreSQL, itd. trzeba użyć specificznych bibiotek)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    addresses = relationship('Address',
                             back_populates='person',
                             order_by='Address.email',
                             cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.name}(id={self.id}'


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship('Person', back_populates='addresses')

    def __str__(self):
        return self.email

    __repr__ = __str__


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
sesion = Session()
anakin = Person(name='Anakin', age=38)  # przyjęło się, że w takim przypadku bez spacji przy zaku "="
obi = Person(name='Obi Wan Kenobi, age=40')
obi.addresses = [
    Address(email='obi@wp.pl'),
    Address(email='wanam@wp.pl')
]

sesion.add(anakin)
sesion.add(obi)
sesion.commit()

# wynik działania
# C:\Users\CSComarch\PycharmProjects\pythonProject\MBO_2023-10-17\baza_SQLAlchemy.py:13: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
#   Base = declarative_base()

all_ = sesion.query(Person).all()
print(all_)
# [Anakin(id=1, Obi Wan Kenobi, age=40(id=2]

an1 = sesion.query(Person).first()
print(an1)
print(type(an1))
print(an1.id, an1.name)

obi1 = sesion.query(Person).filter(
    Person.name.like('Obi%')
).first()
print(obi1)  # Obi Wan Kenobi, age=40(id=2
print(obi1.addresses)  # [obi@wp.pl, wanam@wp.pl]
