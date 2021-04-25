from datetime import date

from src import session, engine
from src.database.models import Event, User, Base


def populating_datebase():
    independence_day = Event(
        title='Independence Day',
        description='About Independence Day',
        distributed_by='Government',
        max_limit_members=1000000,
        date=date(2021, 7, 4),
    )
    eleciton = Event(
        title='Election',
        description='About election',
        distributed_by='Government',
        max_limit_members=10000000,
        date=date(2020, 12, 26),
    )
    party = Event(
        title='Party with friends',
        description='About party with friends',
        distributed_by='Mr. Brown',
        max_limit_members=15,
        date=date(2021, 1, 29)
    )
    travel_around_world = Event(
        title='Travel Around World',
        description='About travel around world',
        distributed_by='Patrick Samuel',
        max_limit_members=3,
        date=date(2021, 5, 7)
    )
    parachute_jumping = Event(
        title='Parachute Jumping',
        description='About parachute jumping',
        distributed_by='Sam Jackson',
        max_limit_members=2,
        date=date(2021, 8, 10)
    )

    dmitry = User(
        username='Dmitry',
        email='dmitry@gmail.com',
        password='esfdsd',
        phone_number='+375296658086',
        age=24
    )
    stas = User(
        username='Stas',
        email='stas@gmail.com',
        password='dsadsa',
        phone_number='+375337689877',
        age=24
    )
    danik = User(
        username='Danik',
        email='danik@gmail.com',
        password='dsdsd',
        phone_number='+375293458231',
        age=24
    )
    oleg = User(
        username='Oleg',
        email='oleg@gmail.com',
        password='sdsads',
        phone_number='+375297836578',
        age=33
    )
    pasha = User(username='Pasha',
        email='pasha@gmail.com',
        password='dsdf',
        phone_number='+375769857483',
        age=21
    )


    session.add(independence_day)
    session.add(eleciton)
    session.add(travel_around_world)
    session.add(parachute_jumping)
    session.add(party)

    session.add(dmitry)
    session.add(stas)
    session.add(oleg)
    session.add(pasha)
    session.add(danik)

    session.commit()


if __name__ == '__main__':
    print('Populating db...')
    populating_datebase()
    print('Successfully populated!')
