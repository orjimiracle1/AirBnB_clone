#!/usr/bin/python3
"""Creates the CLI cmd console."""
import cmd
import re
from shlex import split
"""
    models imports
"""
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City

#parser
def parse(arg):
    """Parser to process stdin data"""
    str_brackets = re.search(r"\[(.*?)\]", arg)
    curl_b = re.search(r"\{(.*?)\}", arg)
    if curl_b is None:
        if str_brackets is None:
            return [x.strip(",") for x in split(arg)]
        else:
            lex_er = split(arg[:str_brackets.span()[0]])
            ret = [x.strip(",") for x in lex_er]
            ret.append(str_brackets.group())
            return ret
    else:
        lex_er = split(arg[:curl_b.span()[0]])
        ret = [i.strip(",") for i in lex_er]
        ret.append(curl_b.group())
        return ret


class HBNBCommand(cmd.Cmd):
    """
    Declares the command cmd class for
    HBNB
    """

    __classes = {
        "BaseModel",
        "State",
        "User",
        "Amenity",
        "Place",
        "City",
        "Review"
    }

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing."""
        pass

    def default(self, arg):
        """Actions when input is invalid"""
        args_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        pattern = re.search(r"\.", arg)
        if pattern is not None:
            args_n = [arg[:pattern.span()[0]], arg[pattern.span()[1]:]]
            pattern = re.search(r"\((.*?)\)", args_n[1])
            if pattern is not None:
                command = [args_n[1][:pattern.span()[0]], pattern.group()[1:-1]]
                if command[0] in args_dict.keys():
                    signal = "{} {}".format(args_n[0], command[1])
                    return args_dict[command[0]](signal)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to quit"""
        print()
        return True

    def do_create(self, arg):
        """
        Initiakize class instance and print id.
        """
        args_n = parse(arg)
        if len(args_n) == 0:
            print("** class name missing **")
        elif args_n[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args_n[0])().id)
            storage.save()

    def do_show(self, arg):
        """
            Using id print instance represatation
        """
        args_n = parse(arg)
        objs_dict = storage.all()
        if len(args_n) == 0:
            print("** class name missing **")
        elif args_n[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_n) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_n[0], args_n[1]) not in objs_dict:
            print("** no instance found **")
        else:
            print(objs_dict["{}.{}".format(args_n[0], args_n[1])])

    def do_destroy(self, arg):
        """Delete class instance based on id given"""
        args_n = parse(arg)
        objs_dict = storage.all()
        if len(args_n) == 0:
            print("** class name missing **")
        elif args_n[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_n) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_n[0], args_n[1]) not in objs_dict.keys():
            print("** no instance found **")
        else:
            del objs_dict["{}.{}".format(args_n[0], args_n[1])]
            storage.save()

    def do_all(self, arg):
        """
        Display string representations of all instances.
        """
        args_n = parse(arg)
        if len(args_n) > 0 and args_n[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if len(args_n) > 0 and args_n[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(args_n) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, arg):
        """
        Instance head count, get total
        """
        args_n = parse(arg)
        count = 0
        for value in storage.all().values():
            if args_n[0] == value.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
            Update instance attributes and methods of the class
        """
        args_n = parse(arg)
        objs_dict = storage.all()
        if len(args_n) == 0:
            print("** class name missing **")
            return False
        if args_n[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args_n) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args_n[0], args_n[1]) not in objs_dict.keys():
            print("** no instance found **")
            return False
        if len(args_n) == 2:
            print("** attribute name missing **")
            return False
        if len(args_n) == 3:
            try:
                type(eval(args_n[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(args_n) == 4:
            obj = objs_dict["{}.{}".format(args_n[0], args_n[1])]
            if args_n[2] in obj.__class__.__dict__.keys():
                value_type = type(obj.__class__.__dict__[args_n[2]])
                obj.__dict__[args_n[2]] = value_type(args_n[3])
            else:
                obj.__dict__[args_n[2]] = args_n[3]
        elif type(eval(args_n[2])) == dict:
            obj = objs_dict["{}.{}".format(args_n[0], args_n[1])]
            for k, v in eval(args_n[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    value_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = value_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
