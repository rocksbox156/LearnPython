# Decorators
print("hi", "ny name is Rishi", sep="---")
x = "hi"

def timer(func):
    def wrapper(*args, **kwargs):
        import time
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        print("{0} took {1} sec".format(func.__name__, t2-t1))
        return result
    return wrapper

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before: " + original_function.__name__)
        original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display():
    print("display function ran")


@decorator_function
@timer
def display_info(name, age):
    print("display_info ran with arguments", (name, age))


display_info("John", 25)



