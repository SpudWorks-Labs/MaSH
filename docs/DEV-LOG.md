# MaSH; Developer Log

**NOTE:** All time is in ***UTC***

---

## Developer Logs
### 2026/03/24
* 15:38
    - Revived the project.

* 17:16
    - Created the projects skeleton.
    - Now creating and pushing to a public repo.

* 20:56
    - The ROADMAP for the first phase has been mapped out.
    - Starting to write the codes boilerplate.

* 21:11
    - Phase 1A has been completed (Interactive Prompt Loop)
      now moving on to Phase 1B.
    - `prompt_toolkit` was added to the requirements.

---

### 2026/03/25
* 05:00
    - Phase 1B has been finished and I might want to change
      how the paths are handled withing the program.
    - I also might want to make the command section a bit
      more modulated.
    - Now moving onto Phase 1C for a customization script.

---

### 2026/03/26
* 15:10
    - The README has been updated to include the venv
      initialization and dependency installation.

* 15:34
    - Modulated the `Mash.process_commands()` for smaller
      methods and easier to read code.

* 16:07
    - Basic configuration from a `.mash` file is now
      available, and Phase 1C is technically finished.
    - Custom color is needed next before this phase
      is completed.

* 16:23
    - Custom colors are available and this marks the
      basic completion of this phase.

* 20:31
    - The welcome screen was created.
    - Next I need to create place holder menus for the
      SpudCommands.

---

### 2026/03/27
* 15:08
    - Implemented a "help" SpudCommand.

* 15:33
    - Moved the command processing logic into its own file
      found wihin `src/core/` as well as the `.mash` config
      logic.

* 16:45
    - Modulated the code more with a `src/core/mash_screens.py`
      file for displaying the menu screens.

* 17:00
    - Moved the welcome message method into
      `src/core/mash_screens.py` to keep the main method small.

* 17:20
    - Created the [CHANGELOG](CHANGELOG.md) and updated to
      version 0.6.0-2026.03.27 to document the weeks work.
    - This can change later today, but a change is marked
      in-case it becomes unavailable later.

* 17:50
    - The paths are now handled using `pathlib.Path` for
      cleaner and simpler code.

* 21:03
    - The `repos` SpudCommand was removed since that will
      be a feature in the projects manager.
    - Renamed 'screens' to 'menus' for clarity.

* 21:30
    - The placeholder menus for the AI and Project
      Management tools have been created.
    - Phase 1D has pretty much been finished, the only
      thing left to do is polishing the code.

---

### 2026/03/28
* 05:02
    - Updated to the Nightly build and V1.0.0-2026.03.28
      and created the menu placeholders.
    - A refactoring is needed for the codebase, especially
      for the menu handling.

* 05:26
    - Created a menu template method for SpudCommands.
  
---

### 2026/03/30
* 18:00
    - Added a settings SpudCommand to the `proc_commands.py`
      file.
    - Next need to make it class-based.

---

### 2026/03/31
* 07:00
    - Finished the first little tests of the updated
      menus.
    - Need to finish the look and ensure scrolling the
      projects is possible.

* 17:57
    - Made more progress in the menu screen tests.

---

### 2026/04/01
* 06:50
    - I have almost finished the projects menu.
   - I just need to make the projects allow for a scrolling
      window kind of feature.

* 21:40
    - The prototyped new menus have been finished.
    - I need to create updated wmenus for the other screens.

---

### 2026/04/02
* 18:56
    - Finished the menu tests, and ready to start the
      official implementation.

---

### 2026/04/03
* 16:58
    - Decided to finally listen to Gemini and stop focusing
      on the UI and implementing features.

* 18:21
    - The menus are now class based and more structured.
    - Next I need to make the a template for the existing
      menus for common attributes and methods.

* 20:04
    - Renamed the file to `mash_menu.py` and made it
      class-based.
    - Made `proc_commands.py` also class-based.
    - I need to clean up the code and remove unnecessary
      code and add documentation comments.

* 20:20
  - Updated the codebase to version 1.3.0-2026.03.04
    Matutinal build.

---

### 2026/04/06
* 16:19
  - Created a Menu Template Class for `plugin_menus.py`
    and did some code clean up.
  - Need to make `Menu.render()` cleaner.

* 17:20
  - Updated the the Menu Template to be more robust and
    included a remove item method.
  - Also, some minor code improvements have been made.

* 17:38 (ay)
  - Cleaned up `Menu.render()` with new methods to make the
    code concise and maintainable.
  - I now need to add the custom prompt to the SpudMenus.
  - I also need to add comments and doc-strings.

* 18:23
  - Implemented the custom prompt for the SpudMenus.

* 20:52
  - Added comments and doc-strings.
  - Not in the right mind-space, so I left out some type
    declarations and other things.
  - A full codebase sweep would be beneficial before moving on.

---

## TO-DO
**[!!!!!!]** Do a codebase sweep for comment and code
clarity.
**[!!!!!]** Clean up and make sure the code is ready for
phase 2.
