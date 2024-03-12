#!/usr/bin/python3
"""Defines the cmd console."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        exit()
    
    def do_EOF(self, arg):
        """EOF to exit console"""
        print()
        exit()
    
    def emptyline(self):
        """Do nothing"""
        pass
    
    def do_create(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
        
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()