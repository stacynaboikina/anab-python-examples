# ABC allows you to create fully abstract classes and this is the most object
# oriented way to do so in Python. Additionally to defining abstract methods
# and properties, you can also add some hooks that will be triggered by abstract
# class's children, inspect which classes implement an abstract base class. So,
# many interesting possibilities are available if you need them :)
#
# To create an abstract class with abc, just inherit from abc.ABC and define some
# abstract methods.
import abc


class AbstractClass(abc.ABC):
    def __init__(self):
        self._some_prop = "Abstract Property value"

    @classmethod
    @abc.abstractmethod
    def some_method(cls):
        print("Some method in Abstract class")

    @property
    def some_prop(self):
        return self._some_prop

    # this is not needed, but you can add this to make user create
    # a setter this way:
    @some_prop.setter
    @abc.abstractmethod
    def some_prop(self, val):
        self._some_prop = val


class SubClass(AbstractClass):
    def some_method(self):
        super().some_method()
        print("Some method in SubClass")

    @property
    def some_prop(self):
        return super().some_prop

    # You can just add a setter here without adding it in abstract class,
    # although then it will not be mandatory.
    # please, note that you are setting abstract class's property:
    @AbstractClass.some_prop.setter
    def some_prop(self, val):
        self._some_prop = val


# the following line will throw an error, behaving 100% OOP-ish:
# m = AbstractClass()
sub_class = SubClass()
sub_class.some_method()
sub_class.some_prop = "new value"
print(sub_class.some_prop)

