from connect_to_db import connect_to_db
from connection import get_channel, get_connection
from models import Contact

connection = get_connection()
channel = get_channel()
queue_name = 'contacts'


def send_email(pk):
    print(f'Email is sent to {pk}.')


def callback(ch, method, _, body):
    pk = body.decode()
    contact = Contact.objects(id=pk, message_sent=False).first()

    if contact:
        send_email(pk)
        contact.update(id=pk, message_sent=True)
    else:
        print(f'{pk}: contact was not found')

    ch.basic_ack(delivery_tag=method.delivery_tag)


def listen_to_contacts():
    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print('[*] Waiting for messages. To exit press CTRL+C')

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()

    connection.close()


if __name__ == '__main__':
    connect_to_db(drop=False)
    listen_to_contacts()
