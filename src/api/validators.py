from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from rest_framework.exceptions import ValidationError
from rest_framework.fields import get_error_detail
from django.utils.translation import gettext as _


def validate_password_pair(password, confirm_password):
    try:
        validate_password(password)
    except DjangoValidationError as e:
        raise ValidationError(get_error_detail(e), 'invalid_password_validation')

    if password != confirm_password:
        raise ValidationError(
            {'confirm_password': _('Password and confirm_password are not equal')},
            'invalid_confirmation'
        )
