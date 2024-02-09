#!/usr/bin/python3
"""
This module console.py that contains the entry
    point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    command interpreter
    """

    prompt = '(hbnb) '

    def do_quit(self, command):
        """exits the HBNB console"""
        exit()

    def help_quit(self):
        """Prints help doc for quit"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        exit()

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("Exits the program without formatting")

    def emptyline(self):
        """ Overrides the empty line method of CMD """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
