"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
               File: mash_config.py
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


# ~ Import System Module. ~ #
import json
import os

# ~ Import Third-Party Modules. ~ #
from prompt_toolkit.styles import Style


def create_config(config_file: str):
    """
    ~ Create the config file if not found. ~

    Argments:
        - config_file (str) : The path of the config file. 
    """
    stock_info = {
        "prompt": ">>>",
        "style": "#FF69B4"
    }

    with open(config_file, 'w') as cfg_file:
        json.dump(stock_info, cfg_file, indent=4)
        cfg_file.write('\n')

def load_config():
    """
    ~ Load the config file create it if non-existant. ~

    Returns:
        - dict : The configuration information.
    """

    config_file = os.path.expanduser('~') + '/.mash'

    if not os.path.exists(config_file):
        create_config(config_file)

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