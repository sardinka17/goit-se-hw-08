import pika
from faker import Faker
from pika import BasicProperties

from connect_to_db import connect_to_db
from connection import get_channel, get_connection
from models import Contact

fake = Faker('uk-Ua')
exchange_name = 'Contact Service'
queue_name = 'contacts'

connection = get_connection()
channel = get_channel()
channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(exchange=exchange_name, queue=queue_name)


def create_contacts():
    for _ in range(10):
        contact = Contact(name=fake.name(),
                          email=fake.email(),
                          phone_number=fake.phone_number(),
                          address=fake.street_address())

        if contact.save():
            channel.basic_publish(exchange=exchange_name,
                                  routing_key=queue_name,
                                  body=str(contact.id).encode(),
                                  properties=BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))
        else:
            print(f'Failed to save contact {contact}.')

    connection.close()


if __name__ == '__main__':
    connect_to_db(drop=True)
    create_contacts()
