"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
                  File: main.py
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


# ~ Import System Modules. ~ #
import os
import subprocess
import json


# ~ Import Local Modules. ~ #
from core.mash_screens import init_screens, prompt_screen


class Mash:
    """
    ~ Handles the main terminal program. ~

    Functions:
        __init__ : Initilaize the terminal program.
        execute  : Execute the main terminal loop.
        welcome_message : Display the welcome message.
    """

    def __init__(self):
        """
        ~ Initialize the terminal program. ~

        Attributes:
            prompt : The prompt to display.
            _is_running : The state of the terminal.
        """

        self.welcome_message()
        init_screens()
        self._is_running = True

    def welcome_message(self):
        import time
        from prompt_toolkit import print_formatted_text, HTML

        os.system("clear" if os.name != 'nt' else "cls")

        # Animated MaSH Welcome Screen using prompt_toolkit
        mash_logo_lines = [            
            r" ______   ______   _____   ________  ___   ___ ",
            r"|      | |      | / __  | /   _____)|   | |   |",
            r"|   ^   V   ^   ||_/  | |(   (_____ |   |_|   |",
            r"|  |  |   |  |  | ___/  |(______   )|    _    |",
            r"|  |   | |   |  |/ __   | ______)  )|   | |   |",
            r"|___|   V   |___||___/|_|(________/ |___| |___|",
            "",
            "<b><style fg='#FF69B4'>Welcome to MaSH: The Productive Terminal</style></b>"
        ]

        for line in mash_logo_lines:
            if line.startswith('<'):
                print_formatted_text(HTML(line))
            else:
                print_formatted_text(line)
            time.sleep(0.07)
            
        print_formatted_text(HTML("<ansiblue>------------------------------------------</ansiblue>"))
        time.sleep(0.1)
        print_formatted_text(HTML("<ansigreen>Type your command or <b>exit</b> to leave MaSH</ansigreen>"), end='\n\n')
        time.sleep(0.2)


    def execute(self):
        """
        ~ Execute the main program loop. ~
        """

        # ~ Main program loop. ~ #
        prompt_screen()


if __name__ == '__main__':
    mash = Mash()
    mash.execute()
