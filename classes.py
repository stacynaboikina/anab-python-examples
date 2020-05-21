

class MyClass:
    class_attribute = "class attribute"

    def __init__(self):
        internal_var = "internal variable"
        print("[MyClass]: Init is called")
        with open("test_file.txt", "r") as f:
            self.instance_attribute = f"instance attribute: {f.read()}"

    @property
    def instance_property(self):
        with open('test_file.txt', "r") as f:
            return f"instance property: {f.read()}"

    def public_instance_method(self):
        print("[MyClass]: Public instance method")

    def _protected_instance_method(self):
        print("[MyClass]: Protected instance method")

    def __private_insance_method(self):
        print("[MyClass]: Private instance method")

    @classmethod
    def class_method(cls):
        print("[MyClass]: Class method")
        print(f"[MyClass]: {cls.instance_property}")



# Getting class reference:
#  - MyClass. outside of class (with or without creating an object)
#  - cls. inside class
# Getting instance reference:
#  - MyClass(). outside of class (by creating an instance (aka object))
#  - self. inside class

# Class methods and attributes are available without
# creating an object of class:
# print("Call class method on class ref:")
# MyClass.class_method()
# >> Class method
# <property object at 0x7efe6ed735e8>
#
# - please, note that when used inside class method
# property will not behave as expected and will only return a
# reference. Although properties are available to be called
# without creating an instance, they will not return you the value.
#
print("Get class attribute on class ref:")
print(MyClass.class_attribute)
# >> class attribute

# Creating an instance of a class:
print("Create instance (object) of a class:")
obj_of_my_class = MyClass()

# You can call class methods on an instance as well:
print("Call class method on an instance:")
obj_of_my_class.class_method()
# >> Class method
# <property object at 0x7ffa33ed8318>

print("Call instance attribute:")
print(obj_of_my_class.instance_attribute)
# >> instance attribute: Some value

# Calling property looks the same as calling instance attribute,
# but there is one difference in behaviour (see below TODO)
print("Call property on instance:")
print(obj_of_my_class.instance_property)
# >> instance property: Some value
# TODO: try to call instance property multiple times and compare it
# with calling instance_attribute multiple times. This is the main
# difference in using instance attr and instance prop.


print("Call public instance method:")
obj_of_my_class.public_instance_method()
# >> Public instance method

print("Call private instance method (DON'T DO THIS!!!):")
obj_of_my_class._protected_instance_method()
# >> Protected instance method
# although it will work, it's not supposed to be used. Protected
# instance methods are intended to be used outside of class or
# its children. Although, you can use it in it's children.

# print("Call private instance method (THIS WILL FAIL):")
# obj_of_my_class.__private_instance_method()
# >> AttributeError: 'MyClass' object has no attribute '__private_instance_method'
# so, this will fail because it's a private method and you cannot use
# it neither on an object of a class, nor in it's children.


# inherit from MyClass:
class ChildClass(MyClass):
    pass


print("MyClass.class_attribute value:")
print(MyClass.class_attribute)

print("Change ChildClass.class_attribute value to 1")
ChildClass.class_attribute = 1
print("ChildClass.class_attribute value:")
print(ChildClass.class_attribute)

print("MyClass.class_attribute value:")
print(MyClass.class_attribute)

print("Let's create 2 instances of ChildClass:")
inst1 = ChildClass()
inst2 = ChildClass()

print("Let's change class_attribute on one of the instances:")
inst2.class_attribute = "inst2"
print("Changing class_attribute on an instance will not affect other instances:")
print(inst1.class_attribute)
print("class_attribute for inst2 will change:")
print(inst2.class_attribute)

print("Let's change class_attribute on class level:")
ChildClass.class_attribute = "class attr changed"
print("inst1.class_attribute:")
print(inst1.class_attribute)
print("inst2.class_attribute:")
print(inst2.class_attribute)
inst3 = ChildClass()
print(inst3.class_attribute)

inst1.instance_attribute = "new value"
print(inst1.instance_attribute)
print(inst2.instance_attribute)
print("REFERENCES:")
print(inst1)
print(inst2)
print(ChildClass())