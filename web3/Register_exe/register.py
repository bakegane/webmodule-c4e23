from mongoengine import Document, StringField, BooleanField

class Register(Document):
    username = StringField()
    password = StringField()
    email_verified = BooleanField(default=False)