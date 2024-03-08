#!/usr/bin/python3
"""HBNBCommand class"""
import cmd
from models import storage
# from models.base_model import BaseModel


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
    
    """edit pycode style"""
    
    def do_create(self, name):
        name_check = name.split()
        if len(name_check) == 0:
            print("** class name missing **")
            return
        try:
            from models.base_model import BaseModel
            new_BaseModel = BaseModel()
            new_BaseModel.save()
            print(new_BaseModel.id)
        except ImportError:
            print("** class doesn't exist **")
            
    def do_show(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            if len(args) < 2:
                print("** instance id missing **")
                return
            objs = storage.all()
            obj = next((obj for obj in objs.values() if obj.id == args[1]), None)
            if obj is None:
                print("** no instance found **")
                return
            print(obj)
        except ImportError:
            print("** class doesn't exist **")
            
    def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            from models import storage
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            obj = objs.get(key)
            if obj is None:
                print("** no instance found **")
                return
            del objs[key]
            storage.save()
        except ImportError:
            print("** class doesn't exist **")
            
    def do_all(self, arg):
        try:
            objs = storage.all()
            if arg == "":
                print([str(obj) for obj in objs])
                return
            elif arg in ["BaseModel"]:
                print([str(obj) for obj in objs])
                return
            else:
                print("** class doesn't exist **")
                return
        except ImportError:
            print("** class doesn't exist **")
            
    
    def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            from models import storage
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            obj = objs.get(key)
            if obj is None:
                print("** no instance found **")
                return
            setattr(obj, args[2], args[3])
            storage.save()
        except ImportError:
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
