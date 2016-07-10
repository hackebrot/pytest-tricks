# -*- coding: utf-8 -*-

import pytest


@pytest.mark.parametrize(
    'sushi',
    ['Kappa Maki', 'Tamagoyaki', 'Inarizushi'],
    indirect=True,
)
@pytest.mark.parametrize(
    'side_dish',
    ['Edamame', 'Miso Soup'],
)
def test_fooshi_serves_vegetarian_sushi(fooshi_bar, sushi, side_dish):
    assert sushi.is_vegetarian
    assert sushi.name in fooshi_bar.menu
    assert side_dish in fooshi_bar.menu


def test_sushi(sushi):
    assert sushi.name
    assert sushi.ingredients
