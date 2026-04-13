"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                Company: SpudWorks.
                Program Name: MaSH.
Description: A terminal that is built for productivity and
                    efficiency.
                 File: display.py
                 Date: 2026/04/10
            Version: 1.6.1-2026.04.10
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


import subprocess
import os
from pathlib import Path

import git

from menus.project_manager.edit_menu import EditMenu
from utilities.database import update_database
from utilities.utils import clear


class ProjectDisplay:
   """
   ~ The class that handles the logic for displaying the
     selected menu. ~

   Function:
       - __init__      : Initialize the project displayer.
       - save_project  : Push the updated project to the
         repo.
       - display_items : Display all of the items in the
         current directory.
       - edit_menu     : Edit the prrojects variables.
       - process_cmd   : Process the command received from
         the user.
       - display       : Display the projects directory.
   """

   def __init__(self, project):
      """
      ~ Initialize the Project Displayer. ~

      Arguments:
          - project     (dict) : The dictionary of the
            projects information.

      Attributes:
          - name        (str)  : The name of the project.
          - path        (str)  : The path to the project.
          - basename    (str)  : The basename of the
            projects path.
          - repos       (str)  : The repo link for saving
            and pushing.
          - run_command (str)  : The command to run the
            project.
          - item_bases  (list) : All of the found items
            in the current path.
      """

      self.name = project['name']
      self.path = project['path']
      self.basename = Path(self.path).name
      self.repos = project['repos']
      self.run_command = project['run_command']
      self.item_bases = []
      self.edit_menu = EditMenu(project)

   def save_project(self, commit_msg):
      """
      ~ Push the updates to the repo with an optional
        message. ~

      Arguments:
          - commit_msg (str) : The message to send with
            the push command.

      Returns:
          str : The response from the git attempt.
      """

      # ~ Attempt to push to the repo via `git`. ~ #
      try:
         repo = git.Repo(self.path)
         repo.git.add(A=True)

         # ~ Check if there are any changes to push. ~ #
         if repo.is_dirty(untracked_files=True):
            msg = commit_msg or "MaSH Auto-Save!"
            repo.index.commit(msg)
         else:
            return "No changes to save!"

         origin = repo.remote(name='origin')
         info = origin.push()

         return f"Push successful: {info[0].summary}"

      except Exception as e:
         return f"Git Error: {e}"

   def display_items(self):
      """
      ~ Display all of the item in the current path. ~
     """

      items = Path(self.path).iterdir()
      self.item_bases = [item.name for item in items]

      for i, item in enumerate(self.item_bases, 1):
         print(item, end='\t')

         if i % 3 == 0:
            print("\n")

   def process_cmd(self, user_input):
      """
      ~ Process the users input to manage the project
        or navigate through the file structure. ~

      Arguments:
          - user_input (list) : A list of the command
            pieces.
      """

      # ~ Go back a directory within the structure. ~
      if user_input[0] == '..':
         basename = Path(self.path).name

         if basename != self.basename:
            length = len("/" + basename)
            self.path = self.path[:-length]
         else:
            print("Cannot leave the base directory.")

      # ~ Handle a file or enter a folder ~ #
      # ~ that is in the current path,    ~ #
      elif user_input[0] in self.item_bases:
         new_path = self.path + '/' + user_input[0]
         if os.path.isdir(new_path):
            self.path = new_path

      # ~ Edit the selected project values. ~
      elif user_input[0] == '@>edit':
         self.edit_menu.display()

      # ~ Push the changes to the repo. ~
      elif user_input[0] == "@>push":
         msg = input("Commit Message >>> ")

         print(self.save_project(msg))

      # ~ Run the project as intended. ~ #
      elif user_input[0] == '@>run':
         subprocess.call(self.run_command, shell=True)

      # ~ Exit the project viewer. ~ #
      elif user_input[0] == '@>exit':
         return False

      return True

   def display(self):
      """
      ~ Display the selected project. ~
      """

      clear()

      while True:
         self.display_items()

         print("\n\n\nAvailable Commands:")
         print("\n@>run\t@>push\t@>edit\t@>exit")

         user_input = input("\n\n >>> ").split(" ")

         if not self.process_cmd(user_input):
            break
