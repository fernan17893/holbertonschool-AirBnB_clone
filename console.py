#!/usr/bin/env python3
""" Entry point of command interpreter """
import cmd, sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Shell class for HBNB project"""

    prompt = '(hbnb) '

    __classes = {
        "BaseModel": BaseModel()
    }

    #basic commands
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
        """Creates a new instance of BaseClass with error handling"""
        if arg == '':
            print('** class name missing **')
        elif arg not in self.__classes:
            print('** class doesn\'t exist **')
        else:
            obj = self.__classes[arg]
            storage.new(obj)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class\
name and id. Ex: $ show BaseModel 1234-1234-1234"""
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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
