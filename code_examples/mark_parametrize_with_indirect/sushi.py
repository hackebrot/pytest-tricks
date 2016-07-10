# -*- coding: utf-8 -*-


class Restaurant:
    def __init__(self, name, location, menu=None):
        if not menu:
            raise ValueError

        self.name = name
        self.location = location
        self.menu = menu


class Sushi:
    def __init__(self, name, ingredients=None):
        if not ingredients:
            raise ValueError

        self.name = name
        self.ingredients = ingredients

    def __contains__(self, ingredient):
        return ingredient in self.ingredients

    @property
    def is_vegetarian(self):
        for ingredient in ['Crab', 'Salmon', 'Shrimp', 'Tuna']:
            if ingredient in self:
                return False
        return True
