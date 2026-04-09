"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: proc_commands.py
                 Date: 2026/03/24
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


# ~ Import Standard Modules. ~ #
import os
from pathlib import Path
import shlex
import subprocess

# ~ Import Third-Party Modules. ~ #
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

# ~ Import Local Modules. ~ #
from core.mash_config import load_config
from menus.assistants_menu import AssistantMenu
from menus.projects_menu import ProjectMenu


def display_prompt():
    """
    ~ Display the custom prompt in a callable method. ~

    Returns:
        - prompt
            (function) : The prompt_toolkit prompt with
                         custom prompt and color.
    """

    config = load_config()
    style = Style.from_dict({
            '': config['style']
        })

    return prompt(
        '\n\n' + config['prompt'],
        style=style
    )


class CommandProcessor:
    """
    ~ Class that handles the user input as a command. ~

    Functions:
        - __init__            : Initialize the processor.
        - spud_help           : Display the SpudCommands.
        - process_spudcommand : Process a known
                                SpudCommand.
        - process_syscommand  : Process a system command.
        - change_directory    : Properly change the
                                directory.
        - process_command     : Process the command as
                                system or SpudCommand
    """

    def __init__(self):
        """
        ~ Initialize the processor info. ~

        Attributes:
            - assistant_menu
                (AssistantMenu) : Class that handles the AI
                                  Assistant Menu.
            - project_menu
                (ProjectMenu)   : Class that handles the
                                  Project Management Menu.
            - spud_commands
                (dict)          : A dictionary of all of the
                                  available commands.
        """

        self.assistant_menu = AssistantMenu(display_prompt)
        self.project_menu = ProjectMenu(display_prompt)
        self.spud_commands = {
            'ai': self.assistant_menu.start,
            'pm': self.project_menu.start,
            '??': self.spud_help
        }

    def spud_help(self):
        """
        ~ Display all of the SpudCommands. ~
        """

        print("Here are all of the available commnads:\n")
        print("@>ai : Create and manage AI Models.")
        print("@>pm : Create an manage Projects.")
        print("@>?? : Display this message.")

    def process_spudcommand(self, command: str):
        """
        ~ Process the SpudCommand and display the menu. ~

        Arguments:
            - command
                (str) : The command to execute.
        """

        # ~ The AI menu. ~ #
        if command in list(self.spud_commands.keys()):
            self.spud_commands[command]()

    def process_syscommand(self, command: str):
        """
        ~ Try to process the system command from user. ~

        Arguments:
            - command
                (str) : System command to execute.
        """

        # ~ Handle change directory command seperately. ~ #
        try:
            parts = shlex.split(command)
        except ValueError:
            parts = command.split()

        if parts and parts[0] == 'cd':
            return self.change_directory(parts[1:])

        # ~ Attempt to run the command. ~ #
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"MaSH Error: {e}")

    def change_directory(self, path: list):
        """
        ~ Change current working directory to the path ~

        Arguments:
            path
                (list) : The path to travel to.
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

    def process_command(self, user_input: str):
        """
        ~ Process and execute the users command. ~ #

        Arguments:
            - user_input
                (str) : The command received.
        """

        # ~ A SpudCommand was issued. ~ #
        if user_input.startswith('@>'):
            command = user_input.replace("@>", "")

            self.process_spudcommand(command)

        # ~ System command was issued. ~ #
        else:
            return self.process_syscommand(user_input)
