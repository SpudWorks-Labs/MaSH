"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: proc_commands.py
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


import os
import subprocess


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
    if command.startswith('cd'):
        path = command.split(maxsplit=2)[1:]
        return change_directory(path)

    # ~ Attempt to run the command. ~ #
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        print(f"MaSH Error: {e}")

def change_directory(path: list):
    # ~ Empty `cd` returns the home directory. ~ #
    path = path[0].strip()
    
    if path == '~' or path == "":
        path = os.path.expanduser('~')
    # ~ Expand the given path. ~ #
    else:
        path = os.path.expanduser(path)

    # ~ Attempt to change the directory. ~ #
    try:
        os.chdir(path)
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
        print("AI menu in progress...")
    
    # ~ The project management menu. ~ #
    elif command.lower() == 'projects':
        print("Projects menu in progress...")

    # ~ The project repo menu. ~ #
    elif command.lower() == 'repos':
        print("Repos menu in progress...")
    
    # ~ Display the help menu. ~ #
    elif command.lower() == 'help':
        print("\nHere are the available SpudCommands:")
        print("\n\t@>ai : AI Assistant settings menu.")
        print("\t@>projects : Project manager menu.")
        print("\t@>repos : Display project repo menu.")
        print("\t@>help : Display this message\n\n")

    else:
        print(f"Error: The SpudCommand '{command}' does not exist!")
