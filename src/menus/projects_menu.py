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
import subprocess
import sys

import git
from prompt_toolkit.application import run_in_terminal

from menus.plugin_menu_template import Menu
from utilities.database import insert_database, read_database, update_database
from utilities.utils import clear
from utilities.validation import Project, ProjectName, ProjectPath, ProjectRepos


class ProjectDisplay:
    def __init__(self, project):
        self.name = project['name']
        self.path = project['path']
        self.basename = Path(self.path).name
        self.repos = project['repos']
        self.run_command = project['run_command']

    def save_project(self, commit_msg):
        try:
            print(self.repos)
            repo = git.Repo(self.path)
            repo.git.add(A=True)

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

    def run(self):
        subprocess.call(self.run_command, shell=True)

    def display(self):
        while True:
            items = Path(self.path).iterdir()
            item_bases = [item.name for item in items]

            for i, item in enumerate(item_bases, 1):
                print(item, end='\t')

                if i % 3 == 0:
                    print("\n")
                
            # This will be replaced by the command processor.
            user_input = input("\n\n >>> ").split(" ")

            if user_input[0] == '..':
                basename = Path(self.path).name

                if basename != self.basename:
                    length = len("/" + basename)
                    self.path = self.path[:-length]
                else:
                    print("Cannot leave the projects directory.")

            elif user_input[0] in item_bases:
                new_path = self.path + '/' + user_input[0]
                if os.path.isdir(new_path):
                    self.path = new_path

            elif user_input[0] == 'edit':
                print("Editing the project settings...")
                print(f"Name: {self.name}")
                print(f"Path: {self.path}")
                print(f"Repos: {self.repos}")
                print(f"Run Command: {self.run_command}")

                print("What do you want to edit?\n\n\tname\tpath\trepo\trun")

                user_input = input(" >>> ")

                if user_input == 'name':
                    name = str(ProjectName())
                    update_database('projects', self.name, {'name': name})

                elif user_input == 'path':
                    path = str(ProjectPath())
                    update_database('projects', self.name, {'path': path})

                elif user_input == 'repo':
                    repos = str(ProjectRepos())
                    update_database('projects', self.name, {'repos': repos})

                elif user_input == 'run':
                    run_command = input("Run Command >>> ")
                    update_database('projects', self.name, {'run_command': run_command})

            elif user_input[0] == "save":
                # Update this to be more robust.
                msg = input("Commit Message >>> ")

                print(self.save_project(msg))

            elif user_input[0] == 'run':
                self.run()

            elif user_input[0] == 'exit':
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
