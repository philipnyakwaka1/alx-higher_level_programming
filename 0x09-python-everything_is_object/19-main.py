def my_function():
    # Function code here

    my_function.my_attribute = getattr(
        my_function, "my_attribute", "Hello, I'm an attribute!")


print(my_function.my_attribute)  # Output: Hello, I'm an attribute!
