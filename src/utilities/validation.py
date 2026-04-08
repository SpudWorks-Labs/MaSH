"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
               File: validation.py
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


from pathlib import Path
from pathvalidate import is_valid_filepath
import validators

from utilities.database import read_database


class Project:
    def __init__(self):
        try:
            self.name = self.get_project_name()
            self.path = self.get_project_path()
            self.repos = self.get_project_repos()
        except Exception as e:
            print(e)

    def get_project_name(self):
        while True:
            name = input("Project Name >>> ")
            length = len(name)

            if length == 0:
                print("Name cannot be empty!")
                continue

            if length > 15:
                print("Name cannot exceed 15 characters!")
                continue

            projects = read_database('projects')
            project_names = []

            for project in projects:
                project_names.append(project[0])

            if name in project_names:
                print("Name already exists!")
                continue

            break

        return name

    def get_project_path(self):
        while True:
            path = input("Project Path >>> ")

            if len(path) == 0:
                print("Path cannot be empty!")
                continue

            # if not is_valid_filepath(path):
            #     print("Path is not valid!")
            #     continue

            if not Path(path).exists():
                # Introduce a path creator. 
                print("Path does not exist!")
                continue

            break

        return path

    def get_project_repos(self):
        while True:
            repo = input("Repo Link >>> ").strip()

            if not validators.url(repo):
                print("Link is not valid!")
                continue

            break

        return repo
