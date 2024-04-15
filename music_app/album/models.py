from django.core.validators import MinValueValidator
from django.db import models


class Album(models.Model):

    MAX_ALBUM_LENGTH = 30

    MAX_ARTISTS_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    MIN_PRICE_VALUE = 0.0

    GENRE_CHOICES = (
        ('Pop Music', 'Pop Music'),
        ('Jazz Music', 'Jazz Music'),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ('Dance Music', 'Dance Music'),
        ("Other", "Other"),
    )

    album_name = models.CharField(
        max_length=MAX_ALBUM_LENGTH,
        unique=True,
        blank=False,
        null=False
    )

    artist = models.CharField(
        max_length=MAX_ARTISTS_LENGTH,
        blank=False,
        null=False
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        choices=GENRE_CHOICES,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField()

    price = models.FloatField(
        blank=False,
        null=False,
        validators=([MinValueValidator(MIN_PRICE_VALUE)])
    )

    owner = models.ForeignKey(
        'user.Profile',
        on_delete=models.CASCADE,
        blank=True
    )
