from connect import connect_to_db
from parse_command import find_quotes_by_tags, find_quotes_by_author
from seeds import save_quotes_to_db, save_authors_to_db

if __name__ == '__main__':
    connect_to_db()
    save_authors_to_db()
    save_quotes_to_db()

    while True:
        command = input(str('Enter a command: '))

        if 'name' in command:
            cmd, first_name, last_name = command.split(' ')
            name = f'{first_name} {last_name}'
            print(find_quotes_by_author(name))
        elif 'tags' in command:
            cmd, tags = command.split(':')
            print(find_quotes_by_tags(tags))
        elif 'tag' in command:
            cmd, tags = command.split(':')
            print(find_quotes_by_tags(tags))
        elif 'exit' in command:
            print('Good bye!')
            break
        else:
            print('Command is invalid! Please, try again.')
