"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: plugin_menus.py
                 Date: 2026/03/24
            Version: 1.3.0-2026.04.06
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


def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

class Menu:
    def __init__(self, commands, menu, display_prompt):
        self.commands = commands
        self.menu = menu
        self.display_prompt = display_prompt
        self.items = self.get_items()
        self._rendering = True

    def get_items(self):
        # Replace with a database in future.
        if self.menu == 'projects':
            return [{
                'head': "MaSH", 
                'body': "~/Documents/SpudWorks/MaSH"
            }]
        elif self.menu == 'models':
            return [{
                'head': "SpudNet",
                'body': "A helpful assistant."
            }]

    def start(self):
        self._rendering = True
        self.render()
    
    def display_items(self):
        if self.items:
            print("Here are the available items:\n")

            for item in self.items:
                head = f"~~~ {item['head']} ~~~"
                
                print(f"{head}\n{item['body']}\n")

        else:
            print("There are no items here!\n")

    def display_commands(self, command_list):
        for i, command in enumerate(command_list, 1):
            print(f"\t{command}", end='\t')

            if i % 3 == 0:
                print('\n')

    def get_prompt(self, command_list):
        user_input = self.display_prompt()

        if user_input in command_list:
            self.commands[user_input]()

    def render(self):
        while self._rendering:
            clear()

            self.display_items()
            
            print("\n")
            command_list = list(self.commands.keys())

            self.display_commands(command_list)
            self.get_prompt(command_list)

        clear()

    def remove_item(self):
        name = input("Item Name >>> ")
        new_items = []

        for item in self.items:
            if name in item['head']:
                self.items.remove(item)

    def exit_menu(self):
        self._rendering = False


class ProjectMenu(Menu):
    def __init__(self, display_prompt):
        self.commands = {
            'import': self.import_project,
            'remove': self.remove_item,
            'exit': self.exit_menu
        }
        super().__init__(self.commands, "projects", display_prompt)

    def import_project(self):
        name = path = None

        while True:
            clear()
            
            name = input("Project Name >>> ")
            path = input("Project Path >>> ")

            print("Is this correct?\n")
            print(f"Name: {name}\nPath: {path}")

            if input(" (y/n) >>> ")[0] == 'y':
                break

        self.items.append({'head': name, 'body': path})


class AssistantMenu(Menu):
    def __init__(self, display_prompt):
        self.commands = {
            'chat': self.chat,
            'create': self.create,
            'remove':self.remove_item,
            'exit': self.exit_menu
        }

        super().__init__(self.commands, "models", display_prompt)

    def chat(self):
        print("work in progress...")

    def create(self):
        print("work in progress...")
