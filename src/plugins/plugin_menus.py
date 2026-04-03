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


config = None
cwd = None
style = None


def copy_config(cfg, curr_dir, prompt_style):
    """
    ~ Copy the configuration information. ~
    """

    global config, cwd, style
    config = cfg
    cwd = curr_dir
    style = prompt_style


def clear():
    os.system('clear' if os.name != 'nt' else 'cls')


class ProjectMenu:
    def __init__(self):
        self.commands = {
            'import': self.import_project,
            'remove': self.remove_project,
            'exit': self.exit_menu
        }
        self.projects = {}
        self._rendering = True

    def import_project(self):
        print("work in progress...")

    def remove_project(self):
        print("work in progress...")

    def exit_menu(self):
        self._rendering = False

    def render(self):
        while self._rendering:
            clear()
            # ~ Display the existing projects. ~ #
            if self.projects:
                print("Here are the available projects:\n")

                for project in self.projects:
                    print(f"~~~ {project['name']} ~~~")
                    print(f"{project['path']}\n\n")

            else:
                print("There are no projects here!")
                print("\nType `import` to add an existing one.\n")

            # ~ Display the available commands. ~ #
            command_list = list(self.commands.keys())
            for i, command in enumerate(command_list, 1):
                print(f"\t{command}", end='')

                if i % 3 == 0:
                    print("\n")

            # ~ Get the users input. ~ #
            user_input = input(" >>> ")
            
            if user_input.lower() in command_list:
                self.commands[user_input.lower()]()

        clear()


class AssistantMenu:
    def __init__(self):
        self.commands = {
            'chat': self.chat,
            'create': self.create,
            'exit': self.exit_menu
        }
        self.models = {}
        self._rendering = True

    def chat(self):
        print("work in progress...")

    def create(self):
        print("work in progress...")

    def exit_menu(self):
        self._rendering = False

    def render(self):
        while self._rendering:
            clear()
            # ~ Display the existing projects. ~ #
            if self.models:
                print("Here are the available assistant models:\n")

                for model in self.models:
                    print(f"~~~ {model['name']} ~~~")
                    print(f"{model['desc']}\n\n")

            else:
                print("There are no models here!")
                print("\nType `create` to create one.\n")

            # ~ Display the available commands. ~ #
            command_list = list(self.commands.keys())
            for i, command in enumerate(command_list, 1):
                print(f"\t{command}", end='')

                if i % 3 == 0:
                    print("\n")

            # ~ Get the users input. ~ #
            user_input = input(" >>> ")
            
            if user_input.lower() in command_list:
                self.commands[user_input.lower()]()

        clear()
