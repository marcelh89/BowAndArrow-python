__author__ = 'marcman'


class Stage:

    def __init__(self, description):
        self._description = description

    def get_description(self):
        return self._description