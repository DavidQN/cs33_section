# decorators in its simplest form
# are just a function being called in another function

# we need this because a decorator is essentially going to use this library to allow us
# to do something with the methods
import functools


def my_decorator(func):
    # in order to create a decorator you actually have to use a decorator @functools.wraps()
    # from functools (i know quite redundant)
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator")
        func()
        print("After the decorator")

    return function_that_runs_func


@my_decorator
def my_function():
    print("I'm the function")


my_function()
