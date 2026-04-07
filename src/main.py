"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
                  File: main.py
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


# ~ Import System Modules. ~ #
import json
import os
import subprocess

# ~ Import Local Modules. ~ #
from menus.mash_menu import Terminal


class Mash:
    """
    ~ Handles the main terminal program. ~

    Functions:
        __init__ : Initilaize the terminal program.
        execute  : Execute the main terminal loop.
    """

    def __init__(self):
        """
        ~ Initialize the terminal program. ~

        Attributes:
            - terminal
                (Terminal) : An instance of the class that
                             handles the terminal logic.
        """

        self.terminal = Terminal()
        self.terminal.welcome_message()

    def execute(self):
        """
        ~ Execute the main program loop. ~
        """

        self.terminal.prompt_menu()


# ~ Ran as the main file. ~ #
if __name__ == '__main__':
    mash = Mash()
    mash.execute()
