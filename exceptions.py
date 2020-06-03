result = None

a = float(input("number 1: "))
b = float(input("number 2: "))

try:
    result = a/b
except ZeroDivisionError as e:
    print("Error =", type(e))
except TypeError as e:
    print("Error =", type(e))
else:
    print("__else__")
finally:
    print("__finally__")

print("result = ", result)
print("end")