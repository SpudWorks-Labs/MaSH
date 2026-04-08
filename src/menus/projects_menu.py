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


import os
from pathlib import Path

from menus.plugin_menu_template import Menu
from utilities.database import update_database, read_database
from utilities.utils import clear
from utilities.validation import Project


class ProjectDisplay:
    def __init__(self, project):
        self.name = project[0]
        self.path = project[1]
        self.repos = project[2]

    def display(self):
        while True:
            print(self.path)
            items = Path(self.path).iterdir()
            item_base = [item.name for item in items]
            for item in item_base:
                print(item)
                
            user_input = input(" >>> ").split(" ")

            if user_input[0] == 'cd':
                if user_input[1] in item_base:
                    self.path += "/" + user_input[1]
                elif user_input[1] == '..':
                    length = len("/" + Path(self.path).name)
                    self.path = self.path[:-length]


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
            'select': self.select_project,
            'exit'  : self.exit_menu
        }
        super().__init__(
            self.commands,
            "projects",
            render_prompt
        )

    def select_project(self):
        name = input("Projects Name >>> ")

        projects = read_database('projects')
        project_names = [project[0] for project in projects]

        if name in project_names:
            for project in projects:
                if name == project[0]:
                    ProjectDisplay(project).display()

    def import_project(self):
        """
        ~ Import a new project into the items list. ~
        """

        try:
            project = Project()

            update_database("projects", (project.name, project.path, project.repos))
        except Exception as e:
            print(e)

            input("Press ENTER to continue...")
