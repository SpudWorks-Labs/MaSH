"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
              File: mash_screens.py
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


# ~ Import System Module. ~ #
import os
import time
    
# ~ Import Third-Party Modules. ~ #
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from prompt_toolkit import print_formatted_text, HTML

# ~ Import Local Modules. ~ #
from core.proc_commands import process_command
from core.mash_config import load_config
from plugins.plugin_menus import copy_config


config = None
cwd = None
style = None


def init_menus():
    """
    ~ Initialize the data used for the screens. ~
    """

    global config, cwd, style

    config = load_config()
    cwd = os.getcwd()
    style = Style.from_dict({
        "": config["style"]
    })

    copy_config(config, cwd, style)


def welcome_message():
    """
    ~ Display the welcome banner to the user. ~ #
    """

    os.system("clear" if os.name != 'nt' else "cls")
    msg = "Welcome to MaSH: The Productive Terminal"
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
    msg = "Type your command or <b>exit</b> to leave MaSH"
    print_formatted_text(
        HTML(f"<ansigreen>{msg}</ansigreen>"), end='\n\n')
    time.sleep(0.2)


def prompt_menu():
    """
    ~ Display the prompt menu. ~
    """
    
    global cwd

    while True:
        user_input = prompt(config["prompt"], style=style)

        # ~ Exit the terminal. ~ #
        if user_input.lower() == 'exit':
            break

        # ~ Check the current directoy. ~ #
        elif user_input.lower() == 'cwd':
            print(cwd)
            continue

        # ~ Process the command. ~ #
        current_path = process_command(user_input)

        if current_path:
            cwd = current_path
