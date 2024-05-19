#!/usr/bin/python3
import cmd

#from pexpect import EOF
import cmd

class MyConsole(cmd.Cmd):
    prompt = "(hbnb) "
    HBNBCommand(cmd.Cmd)

class HBNBCommand(cmd.Cmd):
    x = input()
    if x == EOF or x == quit:
        exit()
    elif x == help:
        print(
        """Documented commands (type help <topic>):
========================================
EOF  help  quit""")
class MyConsole(cmd.Cmd):
    prompt = "(hbnb) "
    HBNBCommand(cmd.Cmd)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
