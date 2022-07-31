from typing import Generic

from django.core.exceptions import ValidationError


def fields_is_not_empty(fields: list[str]) -> bool:
    fields_is_valid = 0

    for field in fields:
        if len(field) > 0:
            fields_is_valid += 1

    return fields_is_valid == len(fields)


def fields_validator(fields: list[(str, Generic)]):
    for field in fields:
        try:
            field[1](field[0])
        except ValidationError as error:
            if hasattr(error, 'messages'):
                return False, error.messages[0]

            return False, error.message

    return True, None
