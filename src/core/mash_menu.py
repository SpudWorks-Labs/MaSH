"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: mash_screens.py
                 Date: 2026/03/24
            Version: 1.3.0-2026.04.03
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
import time
from math import ceil
import shutil
    
# ~ Import Third-Party Modules. ~ #
from prompt_toolkit import print_formatted_text, HTML

# ~ Import Local Modules. ~ #
from core.proc_commands import CommandProcessor, display_prompt


class Terminal:
    def __init__(self):
        """
        ~ Initialize the data used for the screens. ~
        """

        self.cwd = os.getcwd()
        self.processor = CommandProcessor()
        self._is_running = True

    def welcome_message(self):
        """
        ~ Display the welcome banner to the user. ~ #
        """

        os.system("clear" if os.name != 'nt' else "cls")
        msg = "Welcome to MaSH: The Productive Terminal"
        # Make this obtain from a file or something.
        mash_logo_lines = [            
            r" ______   ______   _____   ________  ___   ___ ",
            r"|      | |      | / __  | /   _____)|   | |   |",
            r"|   ^   V   ^   ||_/  | |(   (_____ |   |_|   |",
            r"|  |  |   |  |  | ___/  |(______   )|    _    |",
            r"|  |   | |   |  |/ __   | ______)  )|   | |   |",
            r"|___|   V   |___||___/|_|(________/ |___| |___|",
            "",
            f"<b><style fg='#FF69B4'>{msg}</style></b>"
        ]

        for line in mash_logo_lines:
            if line.startswith('<'):
                print_formatted_text(HTML(line))
            else:
                print_formatted_text(line)

            time.sleep(0.07)
            
        print_formatted_text(
            HTML(f"<ansiblue>{'-' * 40}</ansiblue>")
        )
        time.sleep(0.1)

        msg = "Type a command or <b>exit</b> to leave MaSH"

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
        
        while self._is_running:
            cmd = display_prompt()

            # ~ Exit the terminal. ~ #
            if cmd.lower() == 'exit':
                self._is_running = False
                continue

            # ~ Check the current directoy. ~ #
            elif cmd.lower() == 'cwd':
                print(self.cwd)
                continue

            # ~ Process the command. ~ #
            cwd = self.processor.process_command(cmd)

            if cwd:
                self.cwd = cwd
