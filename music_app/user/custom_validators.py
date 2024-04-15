from django.core.exceptions import ValidationError


def custom_username_validator(username: str):
    if any([not ch.isalnum() and ch != "_" for ch in username]):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")