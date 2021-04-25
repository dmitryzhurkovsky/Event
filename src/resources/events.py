import datetime

from flask import request
from flask_restful import Resource

from src import session
from src.database.models import Event


class EventListApi(Resource):
    def get(self, id=None):
        if not id:
            events = session.query(Event).all()
            return [event.to_json() for event in events], 200
        event = session.query(Event).filter_by(id=id).first()
        if not event:
            return "", 404
        return event.to_json(), 200

    def post(self):
        event_json = request.json
        if not event_json:
            return {"message": "Wrong data"}, 400
        try:
            event = Event(
                title=event_json['title'],
                description=event_json['description'],
                distributed_by=event_json['distributed_by'],
                max_limit_members=event_json['max_limit_members'],
                date=datetime.datetime.strptime(event_json['date'], '%Y-%m-%d')  # Преобразуем строку в объект.
            )
            session.add(event)
            session.commit()
        except (KeyError, ValueError):
            return {"message": "Wrong data"}, 400
        return {"message": "Created successfully", "id": event.id}, 201

    def put(self, id):
        event_json = request.json
        if not event_json:
            return {"message": "Wrong data"}, 400
        try:
            session.query(Event).filter_by(id=id).update(
                dict(
                    title=event_json['title'],
                    description=event_json['description'],
                    distributed_by=event_json['distributed_by'],
                    max_limit_members=event_json['max_limit_members'],
                    date=datetime.datetime.strptime(event_json['date'], '%Y-%m-%d')  # Преобразуем строку в объект.
                )
            )
            session.commit()
        except (ValueError, KeyError):
            return {"message": "Wrong data"}, 400
        return {"message": "Update successfully"}, 200

    def patch(self, id):
        event = session.query(Event).filter_by(id=id).first()
        if not event:
            return "", 404
        event_json = request.json
        title=event_json['title'],
        description=event_json['description'],
        distributed_by=event_json['distributed_by'],
        max_limit_members=event_json['max_limit_members'],
        date=datetime.datetime.strptime(event_json['date'], '%Y-%m-%d')  # Преобразуем строку в объект.

        if title:
            event.title = title
        if description:
            event.description = description
        if distributed_by:
            event.distributed_by = distributed_by
        if max_limit_members:
            event.max_limit_members = max_limit_members
        if date:
            event.date = date

        session.add(event)
        session.commit()
        return {"message": "Update successfully"}, 200

    def delete(self, id):
        event = session.query(Event).filter_by(id=id).first()
        if not event:
            return "", 400
        session.query(Event).delete(event)
        session.commit()
        return "", 204

