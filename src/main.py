"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
                  File: main.py
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


# ~ Import System Modules. ~ #
import os
import subprocess
import json

from prompt_toolkit.application import get_app, Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout.containers import DynamicContainer
from prompt_toolkit.layout.layout import Layout

# ~ Import Local Modules. ~ #
from core.mash_menus import (
    prompt_menu, welcome_message, init_menus
)


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
        """

        welcome_message()
        init_menus()

    def execute(self):
        """
        ~ Execute the main program loop. ~
        """

        prompt_menu()


if __name__ == '__main__':
    mash = Mash()
    mash.execute()
