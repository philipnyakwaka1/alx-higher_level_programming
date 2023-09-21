#!/usr/bin/python3
"""This is a module for the Base clase"""

import json
import csv
import turtle


class Base():
    """This is the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The __init__ method initializes the class
        Args:
            id: id attribute of the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """converts a list of dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries, ensure_ascii=False)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs])
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns list representation of json string"""

        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns and instance with all attributes already set"""

        if dictionary and len(dictionary) != 0:
            if cls.__name__ == "Square":
                new = cls(1)
            elif cls.__name__ == "Rectangle":
                new = cls(1, 1)
            if hasattr(new, "update") and callable(getattr(new, "update")):
                new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + ".json"
        instances = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                json_string = f.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**data) for data in dictionaries]
        except Exception as ex:
            pass
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes data in CSV"""

        filename = cls.__name__ + ".csv"
        if list_objs is None or len(list_objs) == 0:
            return "[]"

        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]

        with open(filename, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fields)
            writer.writeheader()
            for obj in list_objs:
                data = obj.to_dictionary()
                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV"""

        filename = cls.__name__ + ".csv"
        objects = []
        try:
            with open(filename, "r", encoding="utf-8", newline="") as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    row = {key: int(value) for key, value in row.items()}
                    obj = cls.create(**row)
                    objects.append(obj)
        except Exception as ex:
            pass
        return objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """

        t = turtle.Turtle()

        t.speed(5)
        turtle.bgcolor("#DEB887")

        def draw_rectangle(width, height):
            for _ in range(2):
                t.forward(width)
                t.left(90)
                t.forward(height)
                t.left(90)

        for rectangle in list_rectangles:
            t.penup()
            t.goto(t.xcor() + 50, t.ycor() + 50)
            t.pendown()
            draw_rectangle(rectangle.width, rectangle.height)

        def draw_square(side_length):
            for _ in range(4):
                t.forward(side_length)
                t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(t.xcor() - 50, t.ycor() - 50)
            t.pendown()
            draw_square(square.size)
