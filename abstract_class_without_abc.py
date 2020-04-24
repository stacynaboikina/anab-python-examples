# One of the ways of creating and abstract class is with pure Python.
# To do so, just raise an error in any method or property you want to
# oblige to implement in child classes. The convention is to use
# NotImplemented() or NotImplementedError() in such case.
#
# To explain how it works: in Python when a method of a child class is
# called, firstly the interpreter will try to find and execute method
# of child class. But if child class doesn't have such method, it will
# continue searching in closest parent, then (if there is one) in grand-
# parent and so on. This is why if parent throws an error, you'll see it.


class AbstractClass:
    def __init__(self):
        self._some_prop = "Abstract Property Value"
        self.my_attribute = "something"

    def some_method(self):
        raise ValueError("some_method must be implemented")

    @property
    def some_prop(self):
        raise NotImplementedError("some_prop must be implemented")


class SubClass(AbstractClass):
    # if you remove this method or property of this class, you'll get an error:
    def some_method(self):
        print("Some method in SubClass")

    @property
    def some_prop(self):
        return self._some_prop

    @some_prop.setter
    def some_prop(self, val):
        self._some_prop = val


# one of the disadvantages of this approach versus using abc is that
# you can create an instance of an abstract class. This is not 100%
# object oriented way.
abstract_class_instance = AbstractClass()

sub_class = SubClass()
sub_class.some_method()
sub_class.my_attribute = "some other value"
print(sub_class.my_attribute)

sub_class.some_prop = "new value"
print(sub_class.some_prop)
