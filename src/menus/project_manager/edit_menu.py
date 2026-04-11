"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
                File: edit_menu.py
                 Date: 2026/04/10
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


from validation.project_validation import *


class EditMenu:
    def __init__(self, project):
        """
        ~ Initialize the edit menu variables. ~

        Argumetns:
            - project (dict) : A dictionary containing the
              information for the project.
        """

        self.project = project

    def process_cmd(self):
        """
        ~ Process the command to change project settings. ~
        """

        user_input = input(" >>> ")

        # ~ Change the name of the project. ~ #
        if user_input == 'name':
            name = str(ProjectName())
            update_database(
                'projects', self.name,
                {'name': name}
            )

        # ~ Change the projects working path. ~ #
        elif user_input == 'path':
            path = str(ProjectPath())
            update_database(
                'projects', self.name,
                {'path': path}
            )

        # ~ Change repo link for saving the project. ~ #
        elif user_input == 'repo':
            repos = str(ProjectRepos())
            update_database(
                'projects', self.name,
                {'repos': repos}
            )

        # ~ Run the project with the set rule. ~ #
        elif user_input == 'run':
            # Maybe ask for the command that runs the file
            # and the path of the file.
            run_command = input("Run Command >>> ")
            update_database(
                'projects', self.name,
                {'run_command': run_command}
            )

    def display(self):
        """
        ~ Display the edit project settings menu. ~
        """

        print("Project Settings:")

        for key, value in self.project.items():
            print(f"{key} = {value}")
       
        print("Type the key you want to edit.")
        print("(i.e. `name`)")

        self.process_cmd()