#!/usr/bin/python3
"""writing the base class"""
import json


class Base:
    """This class will be the “base” of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def from_json_string(json_string):
        """
            Returns a dict from a string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
    
    @classmethod
    def load_from_file(cls):
        """load from file"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as myfile:
                list_dicts = Base.from_json_string(myfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def to_json_string(list_dictionaries):
        """list of dictionary to json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return ("[]")
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def create(cls, **dictionary):
        """Return a class instanced from a dictionary of attributes.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def save_to_file(cls, list_objs):
        """save the instance of the obj to file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as myfile:
            if (list_objs is None or list_objs == []):
                myfile.write('[]')
            else:
                list_dict = [i.to_dictionary() for i in list_objs]
                myfile.write(Base.to_json_string(list_dict))
