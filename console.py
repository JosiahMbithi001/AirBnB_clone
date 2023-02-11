#!/usr/bin/env python3
"""HBNBCommand Class.
Custom command line for AirBnB project.
"""
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Defines methods and attributes of the console"""

    prompt = "(hbnb) "

    models = ("Amenity", "BaseModel", "City", "Place", "Review", "State", "User")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exits the program when user calls EOF"""
        return True

    def emptyline(self):
        # Overrides the dafult repeating of previous command
        return False

    def do_create(self, arg):
        """Creates a new instance of a class, saves it and prints the id"""
        error = HBNBCommand.HBNBCommand_error_handler(arg)
        if error:
            return

        obj = eval(arg)()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an object based on the class
        name and id
        """
        error = HBNBCommand.HBNBCommand_error_handler(arg, command="show")
        if error:
            return

        arg = arg.split()
        objects = storage.all()
        key = f"{arg[0]}.{arg[1]}"
        obj = objects.get(key)
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an object based on the class name and id"""
        error = HBNBCommand.HBNBCommand_error_handler(arg, command="destroy")

        if error:
            return

        arg = arg.split()
        key = f"{arg[0]}.{arg[1]}"
        objects = storage.all()
        if key in objects and storage.delete(objects[key]):
            pass
        else:
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
