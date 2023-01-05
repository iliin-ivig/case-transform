def first_letter_up(identifier: str) -> str:
    return identifier[0].upper() + identifier[1:].lower()


def to_camel_case(first_part: str, *rest_parts: str) -> str:
    return first_part.lower() + to_upper_camel_case(*rest_parts)


def to_upper_camel_case(*parts: str) -> str:
    return ''.join(
        first_letter_up(part)
        for part in parts
    )


def to_snake_case(*parts: str) -> str:
    return '_'.join(
        part.lower()
        for part in parts
    )


def to_upper_snake_case(*parts: str) -> str:
    return '_'.join(
        part.upper()
        for part in parts
    )


def to_kebab_case(*parts: str) -> str:
    return '-'.join(
        part.lower()
        for part in parts
    )


def to_upper_kebab_case(*parts: str) -> str:
    return '-'.join(
        part.upper()
        for part in parts
    )
