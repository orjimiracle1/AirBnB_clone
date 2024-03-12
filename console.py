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
        """Display string representation"""
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
        """Delete an instance using its id """
        arg_n = parse(arg)
        obj_dict = storage.all()
        if len(arg_n) == 0:
            print("** class name missing **")
        elif arg_n[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_n) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_n[0], arg_n[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_n[0], arg_n[1])]
            storage.save()

    def do_all(self, arg):
        '''Display string representations of all instances '''
        arg_n = parse(arg)
        if len(arg_n) > 0 and arg_n[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(arg_n) > 0 and arg_n[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(arg_n) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)
    
    def do_count(self, arg):
        """
        Retrieve the number of instances of a given class.
        """
        arg_n = parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_n[0] == obj.__class__.__name__:
                count += 1
        print(count)

def do_update(self, arg):
        """
        Update instance based on the given id
        """
        arg_n = parse(arg)
        obj_dict = storage.all()
        if len(arg_n) == 0:
            print("** class name missing **")
            return False
        if arg_n[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_n) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_n[0], arg_n[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_n) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_n) == 3:
            try:
                type(eval(arg_n[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg_n) == 4:
            obj = obj_dict["{}.{}".format(arg_n[0], arg_n[1])]
            if arg_n[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg_n[2]])
                obj.__dict__[arg_n[2]] = valtype(arg_n[3])
            else:
                obj.__dict__[arg_n[2]] = arg_n[3]
        elif type(eval(arg_n[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_n[0], arg_n[1])]
            for k, v in eval(arg_n[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()