# Decorators are wrappers that wrap your function and can modify it's parameters or
# return value.
#
# For example, making an HTTP request you might be operating on JSONs, but want to
# always return stringified JSON. This is a perfect task for a decorator: you run
# the function or method inside a decorator and once it returns a value, you
# make "json.dumps()" on result.


# Decorators can have parameters, then there will be 3 nested functions of which
# first accepts decorator's parameter:
def multiply(num):
    # decorators without parameters need only 2 nested functions, outer of which
    # receives function it's applied to as parameter:
    def my_decorator(func):
        # inner function of a decorator always receives parameters of a function
        # it's applied to:
        def inner(*args, **kwargs):
            new_args = []
            print("In decorator")
            new_args.append(args[0] * num)
            # don't forget to actually all the function inside :D
            res = func(*new_args, **kwargs)
            print(f"This is function result: {res}")
            # ...and to return it's result
            return res
        # always return reference to inner functions in outer functions,
        # otherwise they will not be called:
        return inner
    return my_decorator


@multiply(6)
def some_function(some_num):
    print("Inside function")
    return some_num


some_function(10)
