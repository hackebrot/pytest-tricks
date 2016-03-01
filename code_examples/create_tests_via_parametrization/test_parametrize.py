# -*- coding: utf-8 -*-

import pytest

@pytest.mark.parametrize('foo, bar', [
    ('foo1', 'bar1'),
    ('foo2', 'bar2')
])
def test_foobar(foo, bar):
    assert True
