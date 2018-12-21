import mlab
from models.user import User

mlab.connect()
User(username="admin", password="321").save()
User(username="abc", password="456").save()
User(username="jqk", password="lmn").save()
for user in User.objects():
    print(user.username, user.password)