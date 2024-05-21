from models import Author, Quote


def find_quotes_by_tags(tags: str):
    quotes_dict = {}

    for tag in tags.split(','):
        quote_objects = Quote.objects(tags__iregex=tag)
        quotes = [quote_object.quote for quote_object in quote_objects]
        quotes_dict.update({tag: quotes})

    return quotes_dict


def find_quotes_by_author(author: str):
    authors_dict = {}
    author_objects = Author.objects(name__iregex=author)

    for author_object in author_objects:
        quote_objects = Quote.objects(author=author_object)
        authors_dict[author_object.name] = [quote_object.quote for quote_object in quote_objects]

    return authors_dict
