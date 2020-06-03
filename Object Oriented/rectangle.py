class Rectangle():
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def set_height(self, value):
        self.__height = value

    def get_height(self):
        return self.__height

    def set_width(self, value):
        self.__width = value

    def get_height(self):
        return self.__width

    def area(self):
        return self.__width*self.__height


rect1 = Rectangle(20, 60)
rect2 = Rectangle(50, 40)

print(rect1.area())
print(rect2.area())
