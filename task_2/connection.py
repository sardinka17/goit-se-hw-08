from pika import PlainCredentials, BlockingConnection, ConnectionParameters


def get_connection():
    credentials = PlainCredentials('guest', 'guest')

    return BlockingConnection(ConnectionParameters(host='localhost', port=5672, credentials=credentials))


def get_channel():
    connection = get_connection()

    return connection.channel()
