"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: plugin_menus.py
                 Date: 2026/03/24
            Version: 1.3.0-2026.04.03
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


import os

from prompt_toolkit import prompt


def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

class Menu:
    def __init__(self, commands, items):
        self.commands = commands
        self.items = items
        self._rendering = True

    def start(self):
        self._rendering = True
        self.render()
    
    def render(self):
        while self._rendering:
            clear()

            if self.items:
                print("Here are the available items:\n")

                for item in self.items:
                    print(f"~~~ {item['head']} ~~~\n{item['body']}\n")

            else:
                print("There are no items here!\n")
            
            print("\n")
            command_list = list(self.commands.keys())

            for i, command in enumerate(command_list, 1):
                print(f"\t{command}", end='\t')

                if i % 3 == 0:
                    print('\n')

            user_input = input(" >>> ")

            if user_input in command_list:
                self.commands[user_input]()

        clear()

    def exit_menu(self):
        self._rendering = False

class ProjectMenu(Menu):
    def __init__(self):
        self.commands = {
            'import': self.import_project,
            'remove': self.remove_project,
            'exit': self.exit_menu
        }
        self.projects = self.get_projects()

        super().__init__(self.commands, self.projects)

    def get_projects(self):
        return [{
            'head': "MaSH", 
            'body': "/home/bruhtato/Documents/SpudWorks/MaSH"
        }]

    def import_project(self):
        print("work in progress...")

    def remove_project(self):
        print("work in progress...")


class AssistantMenu(Menu):
    def __init__(self):
        self.commands = {
            'chat': self.chat,
            'create': self.create,
            'exit': self.exit_menu
        }
        self.models = self.get_models()

        super().__init__(self.commands, self.models)
    
    def get_models(self):
        return [{
            'head': "SpudNet",
            'body': "A helpful assistant."
        }]

    def chat(self):
        print("work in progress...")

    def create(self):
        print("work in progress...")
