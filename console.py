#!/usr/bin/python3
import cmd 
class HBNBCommand(cmd.Cmd):
    def __init__(self):
        prompt = "(hbnb) "
    def cmdloop(self):
        """my documentation of cmd loop"""
        while True:
            x = input("(hbnb) ")

            if x == "EOF" or x == "quit":
                exit()
            elif x == "help quit":
                print("Quit command to exit the program\n")
            elif x == "help":
                print(
        """Documented commands (type help <topic>):
========================================
EOF  help  quit""")
            elif x == "\n":
                pass
            else:
                pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

