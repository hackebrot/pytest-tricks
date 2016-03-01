# -*- coding: utf-8 -*-

import pytest

RULES = (
    (3 * 5, "FizzBuzz"),
    (3, "Fizz"),
    (5, "Buzz"),
)


def fizzbuzz(number):
    for div_number, substitution in RULES:
        if not number % div_number:
            return substitution
    return str(number)


@pytest.mark.parametrize(
    'number, word', [
        (1, '1'),
        (3, 'Fizz'),
        (5, 'Buzz'),
        (10, 'Buzz'),
        (15, 'FizzBuzz'),
        (16, '16')
    ]
)
def test_fizzbuzz(number, word):
    assert fizzbuzz(number) == word
