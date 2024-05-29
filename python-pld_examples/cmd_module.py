#!/usr/bin/python3
import cmd
from datetime import datetime
import os


class MyConsole(cmd.Cmd):
    intro = (
        """                                            Welcome to:                                                   \n"""
        """|\   _ \  _   \    |\  \  /  /|\   ____\|\   __  \|\   ___  \|\   ____\|\   __  \|\  \     |\  ___ \      \n"""
        """ \ \  \ \__\ \  \   \ \  \/  / | \  \___|\ \  \|\  \ \  \  \  \ \  \___|\ \  \|\  \ \  \    \ \   __/|     \n"""  
        """  \ \  \ |__| \  \   \ \    / / \ \  \    \ \  \ \  \ \  \  \  \ \_____  \ \  \ \  \ \  \    \ \  \_|/__   \n"""
        """   \ \  \    \ \  \   \/  /  /   \ \  \____\ \  \ \  \ \  \  \  \|____|\  \ \  \ \  \ \  \____\ \  \_|\ \  \n"""
        """    \ \__\    \ \__\__/  / /      \ \_______\ \_______\ \__\  \__\____\_\  \ \_______\ \_______\ \_______\ \n"""
        """     \|__|     \|__|\___/ /        \|_______|\|_______|\|__| \|__|\_________\|_______|\|_______|\|_______| \n"""
        """                  \|___|/                                       \|_________|                              \n"""
        "Type help to list commands.\n"
    )
    prompt = "(MyConsole)$ "

    def do_greet(self, arg):
        print("Hello, {:s}".format(arg))

    def do_exit(self, arg):
        print("Exiting MyConsole...")
        return True

    def do_date(self, arg):
        now = datetime.now()
        textual_date = now.strftime("%A, %B %d, %Y")
        print("Today's date: ", textual_date)

    def do_time(self, arg):
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S %p")
        print("Current Time: ", current_time)

    def do_datetime(self, arg):
        now = datetime.now()
        textual_date = now.strftime("%A, %B %d, %Y ")
        current_time = now.strftime("%I:%M:%S %p")
        print("Current datetime: ", textual_date, current_time)

    def do_pwd(self, arg):
        current_directory = os.getcwd()
        print("Current Working Directory: ", current_directory)

    def default(self, line):
        print("Unknown command: {:s}".format(line))

if __name__ == '__main__':
    MyConsole().cmdloop()