"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: assistants_menus.py
                 Date: 2026/04/07
            Version: 1.5.1-2026.04.07
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


from menus.plugin_menu_template import Menu


class AssistantMenu(Menu):
    """
    ~ The class to handle the Assistant Menu. ~

    Inherits Menu Class

    Functions:
        - __init__ : Initialize the Assistants Menu.
        - chat     : Talk to the selected model.
        - create   : Create a new custom Assistant.
    """

    def __init__(self, render_prompt):
        """
        ~ Initialize the Assistant Menu. ~

        Arguments:
            - render_prompt
                (function) : The function to render the
                             customized prompt.

        Attributes:
            - commands
                (dict) : A dictionary of all of the
                         available commands.
        """

        self.commands = {
            'chat'  : self.chat,
            'create': self.create,
            'remove':self.remove_item,
            'exit'  : self.exit_menu
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
