import factory
import string
import random

from random import randint
from .models import *

class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author
    name = factory.Faker('sentence',nb_words=2)

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = factory.Faker('sentence',nb_words=2)

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    title = factory.Faker('sentence',nb_words=4)
    author = AuthorFactory()
    category = CategoryFactory()
    description = factory.Faker('sentence',nb_words=6)
    quantity = randint(1,10)
    price = randint(1,20)*1000
    image = factory.LazyAttribute(
            lambda _: ContentFile(
                factory.django.ImageField()._make_data(
                    {'width': 250, 'height': 400}
                ), 'example.jpg'
            )
        )
