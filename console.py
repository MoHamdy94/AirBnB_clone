#!/usr/bin/python3
""" command interpreter """

import cmd
import sys
import models
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ class handel command interprete inherit from the cmd class """

    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "Place",
                 "State", "City", "Amenity", "Review"}

    def do_quit(self, arg):
        """ Quit and exit the program """
        return True
    do_exit = do_quit

    def help_quit(self):
        """ help for quit command """
        print('Quit command to exit the program')

    def do_EOF(self, arg):
        """Quits interpreter with ctrl+d"""
        return True

    def emptyline(self):
        """
        override to excute nothing if empty line entered
        """
        pass

    def do_create(self, arg):
        ''' Usage: create <class>
        Creates a class instance,saves it (to the JSON file)
        and prints its id '''
        args = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
            else:
                '''create new object'''
                new_obj = eval(args[0])()
                '''save new object to json file'''
                storage.save()
                '''print its id'''
                print(f"{new_obj.id}")

    def do_show(self, arg):
        '''
        Prints string representation of
    an instance based on class name and id
        '''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        '''get the dictionary of stored objects'''
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_all(self, arg):
        '''Usage: all '''
        args = arg.split()
        obj_list = []
        if args:
            if args[0] not in HBNBCommand.__classes:
                print("** class doesn't exist **")
                return
            else:
                for value in storage.all().values():
                    if args[0] == value.__class__.__name__:
                        obj_list.append(value.__str__())
        else:
            for value in storage.all().values():
                obj_list.append(value.__str__())
        print(obj_list)

    def do_destroy(self, arg):
        '''Usage: destroy <class name> <id>
            Delete an instance based on class name and id
            and save the change in JSON file'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            for key, value in storage.all().items():
                if args[0] == value.__class__.__name__ and args[1] == value.id:
                    del storage.all()[key]
                    storage.save()
                    return
                else:
                    print("** no instance found **")

    def do_update(self, arg):
        """ Update the basemodel"""
        args = arg.split()
        if len(args) == 0:
            print(" class name missing ")
            return
        if args[0] not in HBNBCommand.__classes:
            print(" class doesn't exist ")
            return
        if len(args) == 1:
            print(" instance id missing ")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all().keys():
            print(" no instance found ")
            return
        if len(args) == 2:
            print(" attribute name missing ")
            return
        if len(args) == 3:
            print(" value missing ")
            return
        if len(args) == 4:
            attribute_value = args[3]
        if attribute_value.startswith('"') and attribute_value.endswith('"'):
            attribute_value = attribute_value[1:-1]

        setattr(models.storage.all()[key], args[2], attribute_value)
        models.storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
