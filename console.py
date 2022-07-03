#!/usr/bin/env python3
""" Entry point of command interpreter """
import cmd, sys


class HBNBCommand(cmd.Cmd):


#help is provided by default but must be updated and documented


#empty line + ENTER should not execute anything



## quit and EOF to exit the program

if __name__ == '__main__':
    HBNBCommand().cmdloop()
