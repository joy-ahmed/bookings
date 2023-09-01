from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """ Custom user Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHERS = "others"

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHERS, 'Others')
    )

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_BANGLA = 'bn'
    LANGUAGE_SPANISH = 'sp'

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, 'English'),
        (LANGUAGE_BANGLA, 'Bangla'),
        (LANGUAGE_SPANISH, 'Spanish'),
    )

    CURRENCY_USD = 'usd'
    CURRENCY_BDT = 'bdt'
    CURRENCY_EURO = 'eur'

    CURRENCY_CHOICES = (
        (CURRENCY_USD, '$ USD'),
        (CURRENCY_BDT, '৳ BDT'),
        (CURRENCY_EURO, '€ EUR'),
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
