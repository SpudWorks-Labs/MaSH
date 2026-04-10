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


import os
from pathlib import Path
import subprocess
import sys

import git
from prompt_toolkit.application import run_in_terminal

from menus.plugin_menu_template import Menu
from utilities.database import (
    insert_database, read_database, update_database
)
from utilities.utils import clear
from utilities.validation import (
    Project, ProjectName, ProjectPath, ProjectRepos
)


class ProjectDisplay:
    """
    ~ The class that handles the logic for displaying the selected menu. ~

    Function:
        - __init__      : Initialize the project displayer.
        - save_project  : Push the updated project to the
                          repo.
        - display_items : Display all of the items in the
                          current directory.
        - edit_menu     : Edit the prrojects variables.
        - process_cmd   : Process the command received from
                          the user.
        - display       : Display the projects directory.
    """

    def __init__(self, project):
        """
        ~ Initialize the Project Displayer. ~

        Arguments:
            - project
                (dict) : The dictionary of the projects
                         information.

        Attributes:
            - name
                (str)  : The name of the project.
            - path
                (str)  : The path to the project.
            - basename
                (str)  : The basename of the projects path.
            - repos
                (str)  : The repo link for saving and
                         pushing.
            - run_command
                (str)  : The command to run the project.
            - item_bases
                (list) : All of the found items in the
                         current path.
        """

        self.name = project['name']
        self.path = project['path']
        self.basename = Path(self.path).name
        self.repos = project['repos']
        self.run_command = project['run_command']
        self.item_bases = []

    def save_project(self, commit_msg):
        """
        ~ Push the updates to the repo with an optional
          message. ~

        Arguments:
            - commit_msg
                (str) : The message to send with the push
                        command.

        Returns:
            str : The response from the git attempt.
        """

        # ~ Attempt to push to the repo via `git`. ~ #
        try:
            repo = git.Repo(self.path)
            repo.git.add(A=True)

            # ~ Check if there are any changes to push. ~ #
            if repo.is_dirty(untracked_files=True):
                msg = commit_msg or "MaSH Auto-Save!"
                repo.index.commit(msg)
            else:
                return "No changes to save!"

            origin = repo.remote(name='origin')
            info = origin.push()
        
            return f"Push successful: {info[0].summary}"
            
        except Exception as e:
            return f"Git Error: {e}"

    def display_items(self):
        """
        ~ Display all of the item in the current path. ~
       """

        items = Path(self.path).iterdir()
        self.item_bases = [item.name for item in items]

        for i, item in enumerate(self.item_bases, 1):
            print(item, end='\t')

            if i % 3 == 0:
                print("\n")

    def edit_menu(self):
        """
        ~ Edit the selected projects information. ~
        """

        # ~ Information message. ~ #
        print("Editing the project settings...")
        print(f"Name: {self.name}")
        print(f"Path: {self.path}")
        print(f"Repos: {self.repos}")
        print(f"Run Command: {self.run_command}")
        print("What do you want to edit?")
        print("\n\n\tname\tpath\trepo\trun")

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

        # ~ Change the repo link for saving th e project. ~ #
        elif user_input == 'repo':
            repos = str(ProjectRepos())
            update_database(
                'projects', self.name,
                {'repos': repos}
            )

        # ~ Run the project with the set rule. ~ #
        elif user_input == 'run':
            run_command = input("Run Command >>> ")
            update_database(
                'projects', self.name,
                {'run_command': run_command}
            )

    def process_cmd(self, user_input):
        """
        ~ Process the users input to manage the project
          or navigate through the file structure. ~

        Arguments:
            - user_input
                (list) : A list of the command pieces.
        """

        # ~ Go back a directory within the structure. ~
        if user_input[0] == '..':
            basename = Path(self.path).name

            if basename != self.basename:
                length = len("/" + basename)
                self.path = self.path[:-length]
            else:
                print("Cannot leave the base directory.")

        # ~ Handle a file or enter a folder ~ #
        # ~ that is in the current path,    ~ #
        elif user_input[0] in self.item_bases:
            new_path = self.path + '/' + user_input[0]
            if os.path.isdir(new_path):
                self.path = new_path

        # ~ Edit teh selected project values. ~
        elif user_input[0] == '@>edit':
            self.edit_menu()

        # ~ Push the changes to the repo. ~
        elif user_input[0] == "@>save":
            msg = input("Commit Message >>> ")

            print(self.save_project(msg))

        # ~ Run the project as intended. ~ #
        elif user_input[0] == '@>run':
            subprocess.call(self.run_command, shell=True)

        # ~ Exit the project viewer. ~ #
        elif user_input[0] == '@>exit':
            return False

        return True

    def display(self):
        """
        ~ Display the selected project. ~
        """

        clear()

        while True:
            self.display_items()

            print("\n\n\nAvailable Commands:")
            print("\n@>run\t@>save\t@>edit\t@>exit")
            
            user_input = input("\n\n >>> ").split(" ")

            if not self.process_cmd(user_input):
                break


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
