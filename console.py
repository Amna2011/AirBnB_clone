#!/usr/bin/python3
import cmd

from pexpect import EOF
class HBNBCommand(cmd.Cmd):
    x = input("(hbnb)")
    if x == EOF or x == quit:
        exit()
    elif x == help:
        """Documented commands (type help <topic>):
========================================
EOF  help  quit"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
