#!/usr/bin/python3
"""Defines the cmd console."""
import cmd
import models

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
        """ create class instance and print id"""
        arg = parse(arg)
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)
            models.storage.save()
    
    def do_show(self, arg):
        "Display string representation"
        arg_n = parse(arg)
        obj_dict = models.storage.all()
        if len(arg_n) == 0:
            print("** class name missing **")
        elif arg_n[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_n) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_n[0], arg_n[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_n[0], arg_n[1])])

    def do_destroy(self, arg):

if __name__ == '__main__':
    HBNBCommand().cmdloop()