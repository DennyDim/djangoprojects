from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from user.custom_validators import custom_username_validator


class Profile(models.Model):

    MIN_USERNAME_LENGTH = 2
    MAX_USERNAME_LENGTH = 15

    MIN_AGE_VALUE = 0

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        blank=False,
        null=False,
        validators=[MinLengthValidator(MIN_USERNAME_LENGTH),
                    custom_username_validator],
    )

    email = models.EmailField(
        blank=False,
        null=False
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=(MinValueValidator(MIN_AGE_VALUE),)
    )