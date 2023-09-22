class BaseGeometry:
    """
    This is the BaseGeometry class.
    """

    def area(self):
        """
        This method raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate the 'value' parameter:
        - 'name' is always a string.
        - If 'value' is not an integer, raise a TypeError with the message '<name> must be an integer'.
        - If 'value' is less than or equal to 0, raise a ValueError with the message '<name> must be greater than 0'.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))



