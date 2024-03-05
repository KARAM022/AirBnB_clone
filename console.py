#!/usr/bin/env python3
"""HBNBCommand class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """The entry point of the command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """exit"""
        return True

    def help_quit(self):
        """help for exit"""
        print("Quit command to exit the program \n")

    def do_EOF(self, line):
        """quit whith EOF"""
        print("")
        return True

    def emptyline(self):
        """noyhing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
