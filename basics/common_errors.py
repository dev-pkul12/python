# 1) SyntaxError : Occurs when Python code is not written in proper syntax.

# if True
#     print("Hello")   Missing colon


# 2) IndentationError Python relies on indentation instead of braces. Wrong indentation causes errors.
# def greet():
# print("Hello")   Indentation missing


# 3) NameError : When a variable/function is used before it is defined.
# print(value)   # value is not defined


# 4) TypeError : Happens when an operation is applied to an object of an inappropriate type.
# num = 5 + "10"   # int + str is invalid


# 5) ValueError : Raised when a function receives an argument of correct type but invalid value.
# int("abc")   # Cannot convert string to int


# 6) IndexError : Accessing a list/tuple index that does not exist.
# nums = [1, 2, 3]
# print(nums[5])   # Out of range


# 7) KeyError : When a dictionary key is not found.
# data = {"name": "Prasanna"}
# print(data["age"])   # 'age' key not present


# 8) AttributeError : When an invalid attribute is accessed for an object.
# text = "hello"
# text.push("world")   # str has no method push


# 9) ImportError / ModuleNotFoundError : Raised when Python cannot import a module or package.
# import non_existing_module


# 10) ZeroDivisionError : Raised when dividing a number by zero.
# result = 10 / 0