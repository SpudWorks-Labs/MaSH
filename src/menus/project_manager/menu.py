"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: projects_menus.py
                 Date: 2026/04/07
            Version: 1.6.1-2026.04.10
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


from menus.project_manager.display import ProjectDisplay
from menus.plugin_menu_template import Menu
from utilities.database import (
    insert_database, read_database
)
from validation.project_validation import *


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
        """
        ~ Select the project to work on. ~
        """

        name = input("Projects Name >>> ")

        projects = read_database('projects')
        project_names = [project['name'] for project in projects]

        if name in project_names:
            for project in projects:
                if name == project['name']:
                    ProjectDisplay(project).display()

    def import_project(self):
        """
        ~ Import a new project into the items list. ~
        """

        try:
            project = Project()

            insert_database("projects", {
                'name': project.name, 
                'path': project.path,
                'repos': project.repos,
                'run_command': project.run_command
            })

        except Exception as e:
            print(e)

            input("Press ENTER to continue...")
