from mongoengine import Document, StringField, BooleanField, EmailField


class Contact(Document):
    name = StringField(required=True, max_length=100)
    email = EmailField(required=True)
    message_sent = BooleanField(default=False)
    phone_number = StringField()
    address = StringField()
    meta = {'collection': 'contacts'}
