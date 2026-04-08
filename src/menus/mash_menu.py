"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: mash_screens.py
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


# ~ Import System Module. ~ #
from math import ceil
import os
import shutil
import time
    
# ~ Import Third-Party Modules. ~ #
from prompt_toolkit import HTML, print_formatted_text

# ~ Import Local Modules. ~ #
from core.proc_commands import (
    CommandProcessor, display_prompt
)
# Need to move this to a utilities file.
from utilities.utils import clear

MSG = "Welcome to MaSH: The Productive Terminal"
MASH_LOGO = [            
    r" ______   ______   _____   ________  ___   ___ ",
    r"|      | |      | / __  | /   _____)|   | |   |",
    r"|   ^   V   ^   ||_/  | |(   (_____ |   |_|   |",
    r"|  |  |   |  |  | ___/  |(______   )|    _    |",
    r"|  |   | |   |  |/ __   | ______)  )|   | |   |",
    r"|___|   V   |___||___/|_|(________/ |___| |___|",
    "",
    f"<b><style fg='#FF69B4'>{MSG}</style></b>"
]


class Terminal:
    """
    ~ Handle the Terminal logic. ~

    Functions:
        - __init__        : Initialize the terminal data.
        - welcome_message : Display the welcome message.
        - prompt_menu     : Run the prompt logic.
    """

    def __init__(self):
        """
        ~ Initialize the data used for the screens. ~

        Attributes:
            - cwd
                (str)               : The current working
                                      directory.
            - processor 
                (CommandProcessor) : The class that handles
                                     user input as command.
            - _running
                (bool)             : Holds the state of the
                                     terminal.
        """

        self.cwd = os.getcwd()
        self.processor = CommandProcessor()
        self._running = True

    def render_logo(self):
        # ~ Render the Logo. ~ #
        for line in MASH_LOGO:
            if line.startswith('<'):
                print_formatted_text(HTML(line))
            else:
                print_formatted_text(line)

            time.sleep(0.07)
            
        # ~ Render the seperator. ~ #
        print_formatted_text(
            HTML(f"<ansiblue>{'-' * 40}</ansiblue>")
        )
        time.sleep(0.1)

    def welcome_message(self):
        """
        ~ Display the welcome banner to the user. ~
        """

        clear()

        self.render_logo()

        # ~ Display command message. ~ #
        cmds_msg = "(`help` and `@>??`) or <b>exit</b>" 
        msg = f"Type a command {cmds_msg} to leave MaSH"

        print_formatted_text(
            HTML(
                f"<ansigreen>{msg}</ansigreen>"
            ),
            end='\n\n'
        )
        time.sleep(0.2)


    def prompt_menu(self):
        """
        ~ Display the prompt menu. ~
        """
        
        # ~ Prompt loop. ~ #
        while self._running:
            cmd = display_prompt()

            # ~ Exit the terminal. ~ #
            if cmd.lower() == 'exit':
                self._running = False
                continue

            # ~ Check the current directoy. ~ #
            elif cmd.lower() == 'cwd':
                print(self.cwd)
                continue

            # ~ Process the command. ~ #
            cwd = self.processor.process_command(cmd)

            if cwd:
                self.cwd = cwd
