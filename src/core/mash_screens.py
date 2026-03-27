"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: mash_screens.py
                 Date: 2026/03/24
            Version: 0.1.0-2026.03.24
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


# ~ Import System Module. ~ #
import os

# ~ Import Third-Party Modules. ~ #
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style

# ~ Import Local Modules. ~ #
from core.proc_commands import process_command
from core.mash_config import load_config


config = None
cwd = None


def init_screens():
    config = load_config()
    cwd = os.getcwd()


def prompt_screen():
    """
    ~ Display the prompt menu. ~
    """
    print(config)
    exit(0)
    style = Style.from_dict({
                "": config["style"]
        })

    while self._is_running:
        user_input = prompt(config["prompt"], style=config["style"])

        # ~ Exit the terminal. ~ #
        if user_input.lower() == 'exit':
            self._is_running = False
            continue

        # ~ Check the current directoy. ~ #
        elif user_input.lower() == 'cwd':
            print(cwd)
            continue

        # ~ Process the command. ~ #
        current_path = process_command(user_input)

        if current_path:
            cwd = current_path