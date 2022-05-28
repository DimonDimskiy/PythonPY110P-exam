import random
import itertools
import json

from faker import Faker

from conf import MODULE

START_PK = 1
START_YEAR = 1185
CURRENT_YEAR = 2023
MIN_PAGES = 1
MAX_PAGES = 3000
MIN_RATE = 0
MAX_RATE = 5
RATE_ROUND = 2
MIN_PRICE = 1
MAX_PRICE = 3000
PRICE_ROUND = 2


def main():
    with open("result file", "w", encoding="utf-8") as f:
        for _ in range(100):
            json.dump(next(dict_gen()), f, indent=4, ensure_ascii=False)


def dict_gen():
    yield {"model": MODULE,
           "pk": next(itertools.count(START_PK)),
           "fields": {
               "title": next(title_gen()),
               "year": next(year_gen()),
               "pages": next(pages_gen()),
               "isbn13": next(isbn13_gen()),
               "rating": next(rating_gen()),
               "price": next(price_gen()),
               "author": next(authors_gen())
           }
           }


def title_gen():
    """

    :return:
    """
    with open("books.txt", "r", encoding="utf-8") as file:
        yield random.choice(file.readlines()).strip()


def year_gen():
    yield random.randint(START_YEAR, CURRENT_YEAR)


def pages_gen():
    yield random.randint(MIN_PAGES, MAX_PAGES)


def isbn13_gen():
    faker = Faker()
    yield faker.isbn13()


def rating_gen():
    yield round(random.uniform(MIN_RATE, MAX_RATE), RATE_ROUND)


def price_gen():
    yield round(random.uniform(MIN_PRICE, MAX_PRICE), PRICE_ROUND)


def authors_gen():
    faker = Faker("ru_RU")
    authors_list = []
    for _ in range(random.randint(1, 3)):
        authors_list.append(faker.name())
    yield authors_list


if __name__ == "__main__":
    main()
