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

# ~ Import Third-Party Modules. ~ #
from prompt_toolkit import prompt


class Mash:
    """
    ~ Handles the main terminal program. ~

    Functions:
        __init__ : Initilaize the terminal program.
        execute  : Execute the main terminal loop.
        process_command : Process the users command.
    """

    def __init__(self):
        """
        ~ Initialize the terminal program. ~

        Attributes:
            prompt : The prompt to display.
            _is_running : The state of the terminal.
        """

        self.prompt = ">>> "
        self.cwd = os.getcwd()
        self._is_running = True

    def process_command(self, user_input: str):
        """
        ~ Process and execute the users command. ~ #

        Arguments:
            - user_input (str) : The command received.
        """

        # ~ A SpudCommand was issued. ~ #
        if user_input.startswith('@>'):
            # ~ The AI menu. ~ #
            if user_input.lower() == '@>ai':
                print("AI menu in progress...")
            
            # ~ The project management menu. ~ #
            elif user_input.lower() == '@>projects':
                print("Projects menu in progress...")

            # ~ The project repo menu. ~ #
            elif user_input.lower() == '@>repos':
                print("Repos menu in progress...")

        # ~ System command was issued. ~ #
        else:
            # ~ Handle Change Directory ~ #
            # ~ command seperately.     ~ #
            if user_input.startswith('cd'):
                parts = user_input.split(maxsplit=1)

                # ~ An empty `cd` points to the ~ #
                # ~ home directory.             ~ #
                strip_parts = parts[1].strip()
                if len(parts) == 1 or strip_parts == "":
                    path = os.path.expanduser('~')
                # ~ Expand the given path. ~ #
                else:
                    path = os.path.expanduser(strip_parts)

                # ~ Attempt to change the directory ~ #
                # ~ to the given path.              ~ #
                try:
                    os.chdir(path)
                    self.cwd = os.getcwd()
                except Exception as e:
                    print(f"MaSH cd Error: {e}")

            # ~ Attempt to run the user ~ #
            # ~ input as a command.     ~ #
            try:
                subprocess.run(user_input, shell=True)
            except Exception as e:
                print(f"MaSH Error: {e}")

    def execute(self):
        """
        ~ Execute the main program loop. ~
        """

        # ~ Main program loop. ~ #
        while self._is_running:
            user_input = prompt(self.prompt)

            # ~ Check the command. ~ #
            if user_input.lower() == 'exit':
                self._is_running = False
                continue

            # ~ Process the command. ~ #
            self.process_command(user_input)


if __name__ == '__main__':
    mash = Mash()
    mash.execute()
