import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds235328.mlab.com:35328/register

host = "ds235328.mlab.com"
port = 35328
db_name = "movie"
user_name = "databaselession"
password = "Passwords0"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())