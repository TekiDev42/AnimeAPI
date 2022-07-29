def validation_fields(fields: list[str]) -> bool:
    fields_is_valid = 0

    for field in fields:
        if len(field) > 0:
            fields_is_valid += 1

    return fields_is_valid == len(fields)
