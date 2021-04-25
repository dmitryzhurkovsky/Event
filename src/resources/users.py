from flask import request
from flask_restful import Resource

from src import session
from src.database.models import User


class UserListApi(Resource):
    def get(self, id=None):
        if not id:
            users = session.query(User).all()
            return [user.to_json() for user in users], 200
        user = session.query(User).filter_by(id=id).first()
        if not user:
            return "", 404
        return user.to_json(), 200

    def post(self):
        user_json = request.json
        if not user_json:
            return {"message": "Wrong data"}, 400
        try:
            user = User(
                username=user_json['username'],
                email=user_json['email'],
                password=user_json['password'],
                phone_number=user_json['phone_number'],
                age=user_json['age']
            )
            session.add(user)
            session.commit()
        except (KeyError, ValueError):
            return {"message": "Wrong data"}, 400
        return {"message": "Created successfully", "id": user.id}, 201

    def put(self, id):
        user_json = request.json
        if not user_json:
            return {"message": "Wrong data"}, 400
        try:
            session.query(User).filter_by(id=id).update(
                dict(
                    username=user_json['username'],
                    email=user_json['email'],
                    password=user_json['password'],
                    phone_number=user_json['phone_number'],
                    age=user_json['age']
                )
            )
            session.commit()
        except (ValueError, KeyError):
            return {"message": "Wrong data"}, 400
        return {"message": "Update successfully"}, 200

    def patch(self, id):
        user = session.query(User).filter_by(id=id).first()
        if not user:
            return "", 404
        user_json = request.json
        username = user_json['username']
        email = user_json['email']
        password = user_json['password']
        phone_number = user_json['phone_number']
        age = user_json['age']

        if username:
            user.username = username
        if email:
            user.email = email
        if password:
            user.password = password
        if phone_number:
            user.phone_number = phone_number
        if age:
            user.age = age

        session.add(user)
        session.commit()
        return {"message": "Update successfully"}, 200

    def delete(self, id):
        user = session.query(User).filter_by(id=id).first()
        if not user:
            return "", 400
        session.query(User).delete(user)
        session.commit()
        return "", 204
