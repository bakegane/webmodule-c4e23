from mongoengine import *

class User(Document):
    username = StringField()
    password = StringField()

#test
if __name__ == "__main__":
    from ..mlab import connect
    connect()
    print("User ---------")