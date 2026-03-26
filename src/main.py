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

# ~ Import Third-Party Modules. ~ #
from prompt_toolkit import prompt
from prompt_toolkit.styles import Style


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

        self.welcome_message()
        self.config = self.load_config()
        self.cwd = os.getcwd()
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

    def create_config(self, config_file: str):
        stock_info = {
            "prompt": ">>>",
            "style": "#FF69B4"
        }

        with open(config_file, 'w') as cfg_file:
            json.dump(stock_info, cfg_file, indent=4)
            cfg_file.write('\n')

    def load_config(self):
        """
        ~ Load the config file create it if non-existant. ~

        Returns:
            - dict : The configuration information.
        """
        config_file = os.path.expanduser('~') + '/.mash'

        if not os.path.exists(config_file):
            self.create_config(config_file)

        with open (config_file, 'r') as cfg_file:
            config = json.loads(cfg_file.read())
            
            try:
                if not config["prompt"].endswith(" "):
                    config["prompt"] += " "

                config["style"] = Style.from_dict({
                    "": config["style"]
                })

            except KeyError as ke:
                error_msg = f"Primary Key not found: {ke}"
                print("MaSH Error: {error_msg}")

            return config


    def process_spudcommand(self, command: str):
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

        else:
            print(f"Error: The SpudCommand '{command}' does not exist!")

    def change_directory(self, path: list):
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
            self.cwd = os.getcwd()

        except Exception as e:
            print(f"MaSH cd Error: {e}")

    def process_syscommand(self, command: str):
        """
        ~ Try to process the system command from user. ~

        Arguments:
            - command (str) : System command to execute.
        """

        # ~ Handle Change Directory command seperately. ~ #
        if command.startswith('cd'):
            path = command.split(maxsplit=2)[1:]
            self.change_directory(path)
            return

        # ~ Attempt to run the command. ~ #
        try:
            subprocess.run(command, shell=True)
        except Exception as e:
            print(f"MaSH Error: {e}")

    def process_command(self, user_input: str):
        """
        ~ Process and execute the users command. ~ #

        Arguments:
            - user_input (str) : The command received.
        """

        # ~ A SpudCommand was issued. ~ #
        if user_input.startswith('@>'):
            command = user_input.replace("@>", "")

            self.process_spudcommand(command)

        # ~ System command was issued. ~ #
        else:
            self.process_syscommand(user_input)

    def execute(self):
        """
        ~ Execute the main program loop. ~
        """

        # ~ Main program loop. ~ #
        while self._is_running:
            user_input = prompt(self.config["prompt"], style=self.config["style"])

            # ~ Check the command. ~ #
            if user_input.lower() == 'exit':
                self._is_running = False
                continue

            # ~ Process the command. ~ #
            self.process_command(user_input)


if __name__ == '__main__':
    mash = Mash()
    mash.execute()
