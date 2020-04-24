# Context manager is an approach that allows to control the flow of
# creating objects and controlling their usage. Can be used with “with”
# statement, or also as a decorator.
# Any class can become a context manager if you overload it's __enter__
# and __exit__ methods:


class ContextManager:
    class_attribute = "some class attribute"

    def __init__(self):
        self.some_attribute = "some instance attribute"
        print('init method called')

    def some_method(self):
        print("some_method was called")

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exit method called')
        # if you want to handle an exception and not fail the whole script:
        return True


with ContextManager() as manager:
    # un-comment the following line to see that exception will be handled
    # if __exit__ returns True
    # raise Exception("asdlfjsldkfj")
    print('with statement block')
    print(manager.some_method())
    print(manager.some_attribute)
    print(manager.class_attribute)

print("some code after with statement")
