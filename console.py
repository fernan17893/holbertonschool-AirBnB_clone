#!/usr/bin/env python3
""" Entry point of command interpreter """
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City


class HBNBCommand(cmd.Cmd):
    """Shell class for HBNB project"""

    prompt = '(hbnb) '

    __classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "Amenity": Amenity,
        "Review": Review,
        "City": City
    }

    # basic commands
    def do_quit(self, args):
        """Quit the shell\n"""
        exit()

    def do_EOF(self, arg):
        """Quit the shell\n"""
        exit()

    def emptyline(self):
        """Do nothing in case of empty line\n"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseClass with error handling\n"""
        if arg == '':
            print('** class name missing **')
        elif arg not in self.__classes:
            print('** class doesn\'t exist **')
        else:
            obj = self.__classes[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string rep of an instance based on the class and ID\n"""
        args = arg.split()
        if arg == '':
            print('** class name missing **')
        elif args[0] not in self.__classes:
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print('** no instance found **')
        else:
            name = f"{args[0]}.{args[1]}"
            print(storage.all()[name])

    def do_destroy(self, arg):
        """Deletes an instance based on the classname and ID\n"""
        args = arg.split()
        if arg == '':
            print('** class name missing **')
        elif args[0] not in self.__classes:
            print('** class doesn\'t exist **')
        elif len(args) < 2:
            print('** instance id missing **')
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print('** no instance found **')
        else:
            name = f"{args[0]}.{args[1]}"
            storage.all().pop(name)
            storage.save()

    def do_all(self, arg):
        """Prints string representation of all objects or of a certain class"""
        args = arg.split()
        if len(args) == 0:
            li = [v.__str__() for (k, v) in storage.all().items()]
            print(li)
        elif len(args) == 1 and args[0] not in self.__classes:
            print('** class doesn\'t exist **')
        else:
            li = [v.__str__() for (k, v) in storage.all().items()
                  if v.__class__.__name__ == args[0]]
            print(li)

    def do_update(self, arg):
        """Use: update <class name> <id> <attribute name> <attribute value>"""
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.__classes:
            print('** class doesn\'t exist **')
        elif len(args) == 1:
            print('** instance id missing **')
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print('** no instance found **')
        elif len(args) == 2:
            print('** attribute name missing **')
        elif len(args) == 3:
            print('** value missing **')
        else:
            name = f"{args[0]}.{args[1]}"
            obj = storage.all()[name]
            setattr(obj, args[2], args[3])
            obj.save()

    def default(self, line):
        """Method called when input does not match any do_* commands"""
        try:
            args = line.split('.')
            cls = args[0]
            command = args[1]
            if command == 'all()':
                self.do_all(cls)
            if command == 'count()':
                li = [v.__class__.__name__ for (k, v) in storage.all().items()]
                print(li.count(cls))
        except Exception:
            print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
