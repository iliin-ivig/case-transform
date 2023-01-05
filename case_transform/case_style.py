from __future__ import annotations

from case_transform.convert_from_parts import (
    to_camel_case,
    to_upper_camel_case,
    to_snake_case,
    to_upper_snake_case,
    to_kebab_case,
    to_upper_kebab_case,
)

from dataclasses import dataclass
from enum import Enum
from typing import Callable
import re


@dataclass(frozen=True)
class CaseStyleItem:
    pattern: re.Pattern
    converter: Callable[..., str]


class CaseStyle(Enum):
    CAMEL_CASE = CaseStyleItem(
        re.compile(r'''
            # camelCase
            ([a-z][a-z\d]*)   # first hump starting with lowercase letter
            ([A-Z][a-z\d]*)*  # rest humps
            ''',
            re.X,
        ),
        to_camel_case,
    )

    UPPER_CAMEL_CASE = CaseStyleItem(
        re.compile(r'''
            # UpperCamelCase
            ([A-Z][a-z\d]*)+  # all humps must start with uppercase letter
            ''',
            re.X,
        ),
        to_upper_camel_case,
    )

    SNAKE_CASE = CaseStyleItem(
        re.compile(r'''
            # snake_case
                ([a-z][a-z\d]*)   # first part before `_` starting with lowercase letter
            (?:_([a-z][a-z\d]*))* # rest parts
            ''',
            re.X,
        ),
        to_snake_case,
    )

    UPPER_SNAKE_CASE = CaseStyleItem(
        re.compile(r'''
            # UPPER_SNAKE_CASE
                ([A-Z][A-Z\d]*)   # first part before `_` starting with uppercase letter
            (?:_([A-Z][A-Z\d]*))* # rest parts
            ''',
            re.X,
        ),
        to_upper_snake_case,
    )

    KEBAB_CASE = CaseStyleItem(
        re.compile(r'''
            # kebab-case
                ([a-z][a-z\d]*)   # first part before `-` starting with lowercase letter
            (?:-([a-z][a-z\d]*))* # rest parts
            ''',
            re.X,
        ),
        to_kebab_case,
    )

    UPPER_KEBAB_CASE = CaseStyleItem(
        re.compile(r'''
            # UPPER-KEBAB-CASE
                ([A-Z][A-Z\d]*)   # first part before `-` starting with uppercase letter
            (?:-([A-Z][A-Z\d]*))* # rest parts
            ''',
            re.X,
        ),
        to_upper_kebab_case,
    )

    @staticmethod
    def detect(identifier: str) -> CaseStyle | None:
        for style in CaseStyle:
            if style.match(identifier):
                return style

        return None

    def match(self, identifier: str) -> bool:
        return identifier == '' or self.value.pattern.fullmatch(identifier) is not None

    def split(self, identifier: str) -> tuple(str):
        if identifier == '':
            return ('',)

        result = self.value.pattern.fullmatch(identifier)
        if result is None:
            raise ValueError(f'Identifier "{identifier}" doesnt match {self}.')

        return result.groups()

    def __call__(self, *parts: str) -> str:
        if parts == tuple():
            return ''

        return self.value.converter(*parts)
