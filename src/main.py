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


# ~ Import Third-Party Modules. ~ #
from prompt_toolkit import prompt


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
            prompt : The prompt to display.
            _is_running : The state of the terminal.
        """

        self.prompt = ">>> "
        self._is_running = True

    def execute(self):
        """
        ~ Execute the main program loop. ~
        """

        # ~ Main program loop. ~ #
        while self._is_running:
            user_input = prompt(self.prompt).lower()

            # ~ Check the command. ~ #
            if user_input == 'exit':
                self._is_running = False
                continue

            print(user_input)


if __name__ == '__main__':
    mash = Mash()
    mash.execute()
