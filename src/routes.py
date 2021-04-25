from src import api
from src.database.models import User
from src.resources.events import EventListApi

api.add_resource(EventListApi, '/events', '/events/<id>', strict_slashes=False)


user1 = User()
print(user1)