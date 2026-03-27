"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: plugin_menus.py
                 Date: 2026/03/24
            Version: 0.6.0-2026.03.27
===========================================================

        Copyright (C) 2026 SpudWorks Labs.

This program is free software: you can redistribute it
and/or modify it under the terms of the GNU Affero 
General Public License as published by the Free
Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be
useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.  See the GNU Affero General Public License for
more details.

You should have received a copy of the GNU Affero General
Public License along with this program.
If not, see <https://www.gnu.org/licenses/>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


from prompt_toolkit import prompt


config = None
cwd = None
style = None


def copy_config(cfg, curr_dir, prompt_style):
    global config, cwd, style
    config = cfg
    cwd = curr_dir
    style = prompt_style


def ai_menu():
    while True:
        print("Welcome to the AI Menu!")
        print("\nHere are the available commands:\n")
        print("\tchat\t\ttrain\t\texit")

        user_input = prompt(config["prompt"], style=style)

        if user_input.lower() in ["chat", "train", "exit"]:
            if user_input.lower() == 'exit':
                break
                
            print("These features are still in the works!")

        else:
            print("Sorry, that is not a valid command!")


def projects_menu():
    while True:
        print("Welcome to the Projects Manager!")
        print("\nHere are the available commands:\n")
        print("\topen\t\tnew\t\texit")

        user_input = prompt(config["prompt"], style=style)

        if user_input.lower() in ["chat", "train", "exit"]:
            if user_input.lower() == 'exit':
                break
                
            print("These features are still in the works!")

        else:
            print("Sorry, that is not a valid command!")
    

def help_menu():
    print("\nHere are the available SpudCommands:")
    print("\n\t@>ai : AI Assistant settings menu.")
    print("\t@>projects : Project manager menu.")
    print("\t@>help : Display this message\n\n")