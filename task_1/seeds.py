import json

from mongoengine.errors import NotUniqueError

from models import Author, Quote


def save_authors_to_db():
    with open('authors.json', encoding='utf-8') as fd:
        authors = json.load(fd)

        for author in authors:
            try:
                author_model = Author(name=author.get('fullname'), born_date=author.get('born_date'),
                                      born_location=author.get('born_location'), description=author.get('description'))
                author_model.save()
            except NotUniqueError:
                print(f'The author {author.get("name")} has been already added')


def save_quotes_to_db():
    with open('quotes.json', encoding='utf-8') as fd:
        quotes = json.load(fd)

        for quote in quotes:
            try:
                author = Author.objects(name=quote.get('author')).first()
                quote_model = Quote(quote=quote.get('quote'), tags=quote.get('tags'), author=author)
                quote_model.save()
            except NotUniqueError:
                print(f'The quote {quote.get("quote")} has been already added')
