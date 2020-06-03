# def square(x):
#     return pow(x, 2)
#
#
# def cube(x):
#     return pow(x, 3)
#
#
# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result
#
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# squares = my_map(square, my_list)
# print(squares)
# cubes = my_map(cube, my_list)
# print(cubes)


# def logger(msg):
#     def log_message():
#         print("Log:", msg)
#
#     return log_message
#
#
# log_hi = logger("Hi!")
# log_hi()


def html_tag(tag):

    def wrap_text(msg):
        print("<{0}>{1}</{0}>".format(tag, msg))

    return wrap_text

print_h1 = html_tag("h1")
print_h1("Test Headline!")
print_h1("Another Headline!")

print_p = html_tag("p")
print_p("Test Paragraph")
