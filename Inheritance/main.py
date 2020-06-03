from Inheritance.rectangle import Rectangle
from Inheritance.triangle import Triangle
from Inheritance.fake_shape import FakeShape

rect = Rectangle()
tri = Triangle()

rect.set_values(50, 40)
tri.set_values(50, 40)

rect.set_color("red")
tri.set_color("blue")

print(rect.area())
print(tri.area())

print(rect.get_color())
print(tri.get_color())

fake = FakeShape("fake")
fake.set_values(4, 5)
print(fake.get_height())
print(fake.get_width())