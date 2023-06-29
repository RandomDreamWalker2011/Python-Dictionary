class MyClass:
    @classmethod 
    def my_class_method(cls, input_1, input_2): 
        print("This is a class method")
        print("Class:", cls)
        print("Input 1:", input_1)
        print("Input 2:", input_2)
    # Can be used outside of class

    def my_instance_method(self, input_2):
        print("This is an instance method")
        print("Class Instance:", self)
        print("Input 1:", input_1)

# Calling the class method using the class itself
MyClass.my_class_method("foo", "Evil fuu")

# Creating an instance of MyClass
hero = MyClass()

# Calling the instance method using the instance object
hero.my_instance_method("fod")
