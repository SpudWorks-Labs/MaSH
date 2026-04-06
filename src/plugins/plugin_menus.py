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


# ~ Import System Modules. ~#
import os


def clear():
    """
    ~ Clear the screen. ~
    """

    os.system('clear' if os.name != 'nt' else 'cls')

class Menu:
    """
    ~ Template class for the menus. ~ 

    Functions:
        - __init__ : Initialize the menu template.
        - get_items : Get the necessary items.
        - start : Start the menu and render it.
        - render_items : Render the items found.
        - render_commands : Render the available
          commands.
        - render_prompt : Render the command prompt.
        - render : Render the entire menu.
        - remove_item : Remove and item from the list.
        - exit_menu : Exit the menu.

    """

    def __init__(self, commands, menu, render_prompt):
        """
        ~ Initialize the Menu Template. ~

        Arguments:
            - commands : A dictionary of available
              commands.
            - menu : The name of the menu.
            - render_prompt : Render the command prompt.

        Attributes:
            - commands : Equals commands argument.
            - menu : Equals the menu argument.
            - render_prompt : Equals the render_prompt argument.
            - items : A list of all of the items.
            - _rendering : State of if the menu is
              rendering.
        """

        self.commands = commands
        self.menu = menu
        self.render_prompt = render_prompt
        self.items = self.get_items()
        self._rendering = True

    def get_items(self):
        """
        ~ Get a list of the items for the menu. ~

        Returns;
            list : a list containing all of the items.
        """

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
        """
        ~ Start the rendering and render the menu. ~
        """

        self._rendering = True
        self.render()
    
    def render_items(self):
        """
        ~ Render all of the items for the menu. ~
        """

        # ~ Check if there are items in the list. ~ #
        if self.items:
            print("Here are the available items:\n")

            # ~ Display the items. ~ #
            for item in self.items:
                head = f"~~~ {item['head']} ~~~"
                
                print(f"{head}\n{item['body']}\n")

        else:
            print("There are no items here!\n")

    def render_commands(self, command_list):
        """
        ~ Render all of the available commands. ~
        """

        # ~ Display each command in a 3 per row format. ~ #
        for i, command in enumerate(command_list, 1):
            print(f"\t{command}", end='\t')

            if i % 3 == 0:
                print('\n')

    def render_prompt(self, command_list):
        """
        ~ Render the command prompt. ~
        """

        user_input = self.render_prompt()

        # ~ Check if the command is available and run ~ #
        # ~ its method.                               ~ #
        if user_input in command_list:
            self.commands[user_input]()

    def render(self):
        """
        ~ Render the entire menus information. ~
        """

        # ~ The  menu rendering loop. ~ #
        while self._rendering:
            clear()

            self.render_items()
            
            print("\n")
            command_list = list(self.commands.keys())

            self.render_commands(command_list)
            self.render_prompt(command_list)

        clear()

    def remove_item(self):
        """
        ~ Remove an item from the irtems list. ~
        """

        name = input("Item Name >>> ")
        new_items = []

        # ~ Remove the item form the list if it exists. ~ #
        for item in self.items:
            if name in item['head']:
                self.items.remove(item)

    def exit_menu(self):
        """
        ~ Exit the menu. ~
        """

        self._rendering = False


class ProjectMenu(Menu):
    """
    ~ The Project Menu logic and information. ~

    Inherits Menu Class

    Functions:
        - __init__ : Initialize the project menu.
        - import_project : Import a new project.
    """

    def __init__(self, render_prompt):
        """
        ~ Initialize the project manager menu. ~

        Arguments:
            - render_prompt : The function to render the
              customized prompt.

        Attributes:
            - commands dict : A dictionary of all the
              available commands.
        """

        self.commands = {
            'import': self.import_project,
            'remove': self.remove_item,
            'exit': self.exit_menu
        }
        super().__init__(self.commands, "projects", render_prompt)

    def import_project(self):
        """
        ~ Import a new project into the items list. ~
        """

        name = path = None

        # ~ Get the information of the project. ~ #
        while True:
            clear()
            
            name = input("Project Name >>> ")
            path = input("Project Path >>> ")

            print("Is this correct?\n")
            print(f"Name: {name}\nPath: {path}")

            # ~ Verify the user is happy with the informatino. ~ #
            if input(" (y/n) >>> ")[0] == 'y':
                break

        self.items.append({'head': name, 'body': path})


class AssistantMenu(Menu):
    """
    ~ The calss to handle the Assistant Menu. ~

    Inherits Menu Class

    Functions:
        - __init__ : Initialize the Assitants Menu.
        - chat : Talk to the selected model.
        - create : Create a new custom Assistant.
    """

    def __init__(self, render_prompt):
        """
        ~ Initialize the Assistant Menu. ~

        Arguments:
            - render_prompt : TThe function to render the
              customized prompt.

        Attributes:
            - commands dict : A dictionary of all of the
              available commands.
        """

        self.commands = {
            'chat': self.chat,
            'create': self.create,
            'remove':self.remove_item,
            'exit': self.exit_menu
        }

        super().__init__(self.commands, "models", render_prompt)

    def chat(self):
        """
        ~ Start chatting with the selected LLM model. ~
        """

        print("work in progress...")

    def create(self):
        """
        ~ Create a new model. ~
        """

        print("work in progress...")
