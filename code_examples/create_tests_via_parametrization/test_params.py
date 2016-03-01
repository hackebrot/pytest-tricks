# -*- coding: utf-8 -*-

import pytest

@pytest.fixture(params=['apple', 'banana'])
def fruit(request):
    return request.param

def test_fruit(fruit):
    assert True
