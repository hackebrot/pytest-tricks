# -*- coding: utf-8 -*-

import operator
import pytest

from foobar import Package, Woman, Man

PACKAGES = [
    Package('requests', 'Apache 2.0'),
    Package('django', 'BSD'),
    Package('pytest', 'MIT'),
]


@pytest.fixture(params=PACKAGES, ids=operator.attrgetter('name'))
def python_package(request):
    return request.param


@pytest.mark.parametrize('person', [
    Woman('Audrey'), Woman('Brianna'),
    Man('Daniel'), Woman('Ola'), Man('Kenneth')
])
def test_become_a_programmer(person, python_package):
    person.learn(python_package.name)
    assert person.looks_like_a_programmer


def test_is_open_source(python_package):
    assert python_package.is_open_source
