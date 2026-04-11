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


# ~ Import System Modules. ~ #
from pathlib import Path
from pathvalidate import is_valid_filepath
import validators

# ~ Import Local Modules. ~ #
from utilities.database import read_database


class ProjectName:
    """
    ~ Handle validation of user input for obtaining
      the Project Name. ~

    Function:
        - __init__     : Initialize the validator.
        - check_name   : Check if the name exists.
        - check_length : Check if the name is of proper
          length.
        - get_name     : Get the name from the user.
    """

    def __init__(self):
        """
        ~ Initialize the validator. ~

        Attributes:
            - name (str) : Obtain the name from the user
              and verify.
        """

        while True:
            try:
                self.name = self.get_name()

                break

            except Exception as e:
                print(e)

    def check_name(self, name):
        """
        ~ Check if the name exists in the database. ~

        Arguments:
            - name (str) : The given name of the project.

        Returns:
            str : The name of the project.
        """

        projects = [
            project for project in read_database('projects')
        ]

        if name in projects:
            raise ValueError("Name already exists!")

    def check_length(self, name):
        """
        ~ Check if the length is of viable size. ~

        Arguments:
            - name (str) : The name to check the size of.
        """
        
        length = len(name)

        if length == 0:
            raise ValueError("Name cannot be empty!")

        elif length > 15:
            raise ValueError("Name cannot exceed 15 characters!")

    def get_name(self):
        """
        ~ Obtain the name from the user. ~

        Returns:
            - str : The validated name of the project.
        """

        name = input("Project Name >>> ")

        self.check_length(name)
        self.check_name(name)

        return name

    def __str__(self):
        """
        ~ Return the name as a string, ~
        """

        return self.name


class ProjectPath:
    """
    ~ Class to handle validation of the Projects Path. ~

    Functions:
        - __init__ : Initialize the validator.
        - get_path: Obtain the path from the user.
        - validate_path : Validate if the path is usable.
    """

    def __init__(self):
        """
        ~ Initialize the path validator. ~

        Attributes:
            - path (str) : The path to the project.
        """

        while True:
            try:
                self.path = self.get_path()

                break

            except Exception as e:
                print(e)

    def validate_path(self, path):
        """
        ~ Validate if the path is not empty and if the path
          is an existing path. ~

        Arguments:
            - path (str) : The string of the projects path.
        """

        if len(path) == 0:
            raise ValueError("Path cannot be empty!")

        if not Path(path).exists():
            raise FileNotFoundError("The given path does not exist!")


    def get_path(self):
        """
        ~ Obtain the path from the user. ~

        Returns:
            - str : The validated path string.
        """

        path = input("Project Path >>> ")

        self.validate_path()

        return path

    def __str__(self):
        """
        ~ Returns the path as a string. ~
        """
        return self.path


class ProjectRepos:
    """
    ~ This hand;es the projects repo validation. ~

    Functions:
        - __init__ : Initialize the validator.
        - get_repos : Obtain the repos from the user.
    """

    def __init__(self):
        """
        ~ Initialize the validator. ~

        Attributes:
            - repos (str) : A string of the repos url.
        """

        while True:
            try:
                self.repos = self.get_repos()

                break

            except Exception as e:
                print(e)

    def get_repos(self):
        """
        ~ Obtain the repos link from the user, then
          validate if it is a valid url. ~

        Returns:
            str : The validated url of the projects repo.
        """

        repo = input("Repo Link >>> ")

        if not validators.url(repo):
            raise ValueError("Link is not valid!")

        return repo

    def __str__(self):
        """
        ~ Returns the repo as a string. ~
        """

        return self.repos


class Project:
    """
    ~ Class to validate the Project. ~

    Functions:
        - __init__ : Initialize the project validator.
    """

    def __init__(self):
        """
        ~ Initialize the validator. ~

        Attributes:
            - name (str)        : The name of the project.
            - path (str)        : The path of the project.
            - repos (str)       : The link to the repo.
            - run_command (str) : The command to execute to
              run the project.
        """

        self.name = str(ProjectName())
        self.path = str(ProjectPath())
        self.repos = str(ProjectRepos())
        self.run_command = input("Run Command >>> ")
