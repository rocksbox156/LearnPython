from Inheritance.polygon import Polygon


class FakeShape(Polygon):
    """
    We can re-implement a superclass' method in the subclass
    if we would like to. The following method illustrates that functionality.
    """
    def __init__(self, arg):
        self.arg = arg
    def get_height(self):
        return "hell no"

