# MaSH; RoadMap

Here is the planned road for this project.

---

## Phase 1: The Terminal Emulator:
This is the foundation of the program and allows the rest
to exist and fall into place.
* **Tech:** Using `prompt_toolkit` for the TUI rendering
and `subprocess` for executing the commands.
* **Feature:** A simple customizable terminal with hooks
for the tools.
* **Goal:** An interactive loop that can be `exit`ed,
intercept SpudCommands and return a placeholder message or
attempt to execute the command and allows for customization
with a `mash` file.

### 1.A: The Interactive Loop
Introduces a prompt menu using `prompt_toolkit` that runs
in an infinite loop until the user types `exit`.

### 1.B: The SpudHead Interceptor
This add the "Logic Gate" of the terminal with a simple
python method that checks if the input starts with the
PotatoHead (`@>`) and outputs a placeholder message based
on the command. If there was no SpudCommand, then execute
the command with `subprocess.run(shell=True)` to allow for
paid features and productivity tools.

**NOTE:** Intercept `cd` and use `os.chdir()` to make the command functional.

### 1.C: The Configurations
A simple configuration file `.mash` that allows to change
the prompt and the color of it, with extra capabilities in
the future.

### 1.D: The TUI & Visuals
The full terminal experience. Create a "Welcome Header"
that displays when MaSH starts. Has menus for the config
settings and the tools.

### 1.E: The Polishing
Clean up this phase and ensure the code is clean and functional.

---

## Phase 2; The Workforce:
    ***Need to complete Phase 1!***

## Phase 3; Mashed Together:
    ***Need to complete Phase 2!***
