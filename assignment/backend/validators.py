from django.core.validators import RegexValidator
from rest_framework.exceptions import ValidationError


def validate_regex(user_input, regex, message):
    try:
        regex_validator = RegexValidator(regex, message)
        regex_validator(user_input)
    except Exception:
        raise ValidationError(f"invalid apiKey. must match regex {regex}")
