#!/usr/bin/env python3
""" Entry point of command interpreter """
import cmd, sys


class HBNBCommand(cmd.Cmd):
    """Shell class for HBNB project"""

    prompt = '(HBNB) '

    #basic commands
    def do_quit(self, arg):
        'Quit the shell\n'
        exit()

    def do_EOF(self, arg):
        'Quit the shell\n'
        exit()

    def emptyline(self):
        'Do nothing in case of empty line\n'
        pass

#help is provided by default but must be updated and documented


#empty line + ENTER should not execute anything



## quit and EOF to exit the program

if __name__ == '__main__':
    HBNBCommand().cmdloop()
