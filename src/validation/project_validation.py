"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
               File: validation.py
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


from pathlib import Path
from pathvalidate import is_valid_filepath
import validators

from utilities.database import read_database


class ProjectName:
    def __init__(self):
        while True:
            try:
                self.name = self.get_name()

                break

            except Exception as e:
                print(e)

    def check_name(self, name):
        projects = [
            project for project in read_database('projects')
        ]

        if name in projects:
            raise ValueError("Name already exists!")

    def check_length(self, name):
        length = len(name)

        if length == 0:
            raise ValueError("Name cannot be empty!")

        elif length > 15:
            raise ValueError("Name cannot exceed 15 characters!")

    def get_name(self):
        name = input("Project Name >>> ")

        self.check_length(name)
        self.check_name(name)

        return name

    def __str__(self):
        return self.name


class ProjectPath:
    def __init__(self):
        while True:
            try:
                self.path = self.get_path()

                break

            except Exception as e:
                print(e)

    def get_path(self):
        path = input("Project Path >>> ")

        if len(path) == 0:
            raise ValueError("Path cannot be empty!")

        if not Path(path).exists():
            raise FileNotFoundError("The given path does not exist!")

        return path

    def __str__(self):
        return self.path


class ProjectRepos:
    def __init__(self):
        while True:
            try:
                self.repos = self.get_repos()

                break

            except Exception as e:
                print(e)

    def get_repos(self):
        repo = input("Repo Link >>> ")

        if not validators.url(repo):
            raise ValueError("Link is not valid!")

        return repo

    def __str__(self):
        return self.repos


class Project:
    def __init__(self):
        self.name = str(ProjectName())
        self.path = str(ProjectPath())
        self.repos = str(ProjectRepos())
        self.run_command = input("Run Command >>> ")
