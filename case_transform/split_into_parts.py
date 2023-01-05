def split_from_camel_case(identifier: str) -> list[str]:
    result = [[]]
    for letter in identifier:
        if letter.isupper() and result[-1] != []:
            result.append([])

        result[-1].append(letter)

    return [
        ''.join(part)
        for part in result
    ]


def split_from_upper_camel_case(identifier: str) -> list[str]:
    return split_from_camel_case(identifier)


def split_from_snake_case(identifier: str) -> list[str]:
    return identifier.split('_')


def split_from_upper_snake_case(identifier: str) -> list[str]:
    return identifier.split('_')


def split_from_kebab_case(identifier: str) -> list[str]:
    return identifier.split('-')


def split_from_upper_kebab_case(identifier: str) -> list[str]:
    return identifier.split('-')
