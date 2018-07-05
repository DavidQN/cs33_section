def wrapper(f):
    def wrapper2():
        print("About to run the function...")
        f()
        print("Done running the function.")

    return wrapper2


@wrapper
def hello():
    print("Hello, world!")


hello()
