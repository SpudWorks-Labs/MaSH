"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: proc_commands.py
                 Date: 2026/03/24
            Version: 1.0.0-2026.03.28
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


# ~ Import Standard Modules. ~ #
import os
import shlex
import subprocess
from pathlib import Path

# ~ Import Local Modules. ~ #
from plugins.plugin_menus import (
    ai_menu, projects_menu, help_menu
)


def process_command(user_input: str):
    """
    ~ Process and execute the users command. ~ #

    Arguments:
        - user_input (str) : The command received.
    """

    # ~ A SpudCommand was issued. ~ #
    if user_input.startswith('@>'):
        command = user_input.replace("@>", "")

        process_spudcommand(command)

    # ~ System command was issued. ~ #
    else:
        return process_syscommand(user_input)

def process_syscommand(command: str):
    """
    ~ Try to process the system command from user. ~

    Arguments:
        - command (str) : System command to execute.
    """

    # ~ Handle Change Directory command seperately. ~ #
    try:
        parts = shlex.split(command)
    except ValueError:
        parts = command.split()

    if parts and parts[0] == 'cd':
        return change_directory(parts[1:])

    # ~ Attempt to run the command. ~ #
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"MaSH Error: {e}")

def change_directory(path: list):
    """
    ~ Change the current working directory to the path ~

    Arguments:
        path (list) : The path the user wants to travel to.
    """

    try:
        # ~ Empty path returns the home directory. ~ #
        target = Path.home()

        # ~ Expand the given path. ~ #
        if path:
            target = Path(path[0]).expanduser()

        # ~ Change the directory. ~ #
        os.chdir(target)

        return os.getcwd()

    except Exception as e:
        print(f"MaSH cd Error: {e}")

def process_spudcommand(command: str):
    """
    ~ Process the SpudCommand and display the menu. ~

    Arguments:
        - command (str) : The command to execute.
    """

    # ~ The AI menu. ~ #
    if command.lower() == 'ai':
        menu_template("AI", ["chat", "train"])
    
    # ~ The project management menu. ~ #
    elif command.lower() == 'projects':
        menu_template("Projects Manager", ["create", "new"])
    
    # ~ Display the help menu. ~ #
    elif command.lower() == 'help':
        help_menu()

    else:
        print(f"Error: The SpudCommand '{command}' does not exist!")
