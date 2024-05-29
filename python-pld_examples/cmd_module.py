#!/usr/bin/python3
import cmd
from datetime import datetime
import os


class MyConsole(cmd.Cmd):
    intro = (
        "                                                                                       \n"
        "                                  Welcome to:                                          \n"
        "                                                                                       \n"
        " __       __             ______                                           __           \n"
        "/  \     /  |           /      \                                         /  |          \n"
        "$$  \   /$$ | __    __ /$$$$$$  |  ______   _______    _______   ______  $$ |  ______  \n"
        "$$$  \ /$$$ |/  |  /  |$$ |  $$/  /      \ /       \  /       | /      \ $$ | /      \ \n"
        "$$$$  /$$$$ |$$ |  $$ |$$ |      /$$$$$$  |$$$$$$$  |/$$$$$$$/ /$$$$$$  |$$ |/$$$$$$  |\n"
        "$$ $$ $$/$$ |$$ |  $$ |$$ |   __ $$ |  $$ |$$ |  $$ |$$      \ $$ |  $$ |$$ |$$    $$ |\n"
        "$$ |$$$/ $$ |$$ \__$$ |$$ \__/  |$$ \__$$ |$$ |  $$ | $$$$$$  |$$ \__$$ |$$ |$$$$$$$$/ \n"
        "$$ | $/  $$ |$$    $$ |$$    $$/ $$    $$/ $$ |  $$ |/     $$/ $$    $$/ $$ |$$       |\n"
        "$$/      $$/  $$$$$$$ | $$$$$$/   $$$$$$/  $$/   $$/ $$$$$$$/   $$$$$$/  $$/  $$$$$$$/ \n"
        "             /  \__$$ |                                                                \n"
        "             $$    $$/                                                                 \n"
        "              $$$$$$/                                                                  \n"
        "                                                                                       \n"
        "                          Type help to list commands                                   \n"
    )
    prompt = "(MyConsole)$ "

    def do_greet(self, arg):
        """Greet the user with the provided name"""
        print("Hello, {:s}".format(arg))

    def do_exit(self, arg):
        """Exit the console"""
        print("Exiting MyConsole...")
        return True

    def do_date(self, arg):
        """Print the current date in textual format"""
        now = datetime.now()
        textual_date = now.strftime("%A, %B %d, %Y")
        print("Today's date: ", textual_date)

    def do_time(self, arg):
        """Print the time in H/M/S AM/PM format"""
        now = datetime.now()
        current_time = now.strftime("%I:%M:%S %p")
        print("Current Time: ", current_time)

    def do_datetime(self, arg):
        """Print the current date and time"""
        now = datetime.now()
        textual_date = now.strftime("%A, %B %d, %Y ")
        current_time = now.strftime("%I:%M:%S %p")
        print("Current datetime: ", textual_date, current_time)

    def do_pwd(self, arg):
        """Print the current working directory"""
        current_directory = os.getcwd()
        print("Current Working Directory: ", current_directory)

    def default(self, line):
        print("Unknown command: {:s}".format(line))

if __name__ == '__main__':
    MyConsole().cmdloop()