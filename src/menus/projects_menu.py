"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: projects_menus.py
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


class ProjectMenu(Menu):
    """
    ~ The Project Menu logic and information. ~

    Inherits Menu Class

    Functions:
        - __init__       : Initialize the project menu.
        - import_project : Import a new project.
    """

    def __init__(self, render_prompt):
        """
        ~ Initialize the project manager menu. ~

        Arguments:
            - render_prompt
                (function) : The function to render the
                             customized prompt.

        Attributes:
            - commands
                (dict) : A dictionary of all the available
                         commands.
        """

        self.commands = {
            'import': self.import_project,
            'remove': self.remove_item,
            'exit'  : self.exit_menu
        }
        super().__init__(
            self.commands,
            "projects",
            render_prompt
        )

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

            # ~ Verify the information is correct. ~ #
            if input(" (y/n) >>> ")[0] == 'y':
                break

        self.items.append({'head': name, 'body': path})