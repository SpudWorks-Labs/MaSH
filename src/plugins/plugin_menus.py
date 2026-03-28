"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: plugin_menus.py
                 Date: 2026/03/24
            Version: 1.0.0-2026.03.28
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


def menu_template(name, commands):
    while True:
        print(f"Welcome to the {name} Menu!")
        print("\nHere are the available commands:\n")

        for command in commands:
            print(f"\t{command}\t", end='')

        print('\n')

        user_input = prompt(config["prompt"], style=style)

        if user_input.lower() == 'exit':
            break

        if user_input.lower() in commands:    
            print("These features are still in the works!")

        else:
            print("Sorry, that is not a valid command!")


def help_menu():
    print("\nHere are the available SpudCommands:")
    print("\n\t@>ai : AI Assistant settings menu.")
    print("\t@>projects : Project manager menu.")
    print("\t@>help : Display this message\n\n")