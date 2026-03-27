# MaSH; Developer Log

**NOTE:** All time is in ***UTC***


## Developer Logs
*2026/03/24*
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

*2026/03/25*
* 05:00
    - Phase 1B has been finished and I might want to change
      how the paths are handled withing the program.
    - I also might want to make the command section a bit
      more modulated.
    - Now moving onto Phase 1C for a customization script.

*2026/03/26*
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

*2026/03/27*
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


## TO-DO
[!!!] Create placeholder menus for each command. ~~ [IN-PROGRESS]
[.] Look into handling the paths in a more robust way. ~
