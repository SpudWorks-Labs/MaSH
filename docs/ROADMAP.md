# MaSH; RoadMap

Here is the planned road for this project.

---

## Phase 1: The Terminal Emulator: (COMPLETED)
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

---

### 1.A: The Interactive Loop (COMPLETED)
Introduces a prompt menu using `prompt_toolkit` that runs
in an infinite loop until the user types `exit`.

### 1.B: The SpudHead Interceptor (COMPLETED)
This adds the "Logic Gate" of the terminal with a simple
python method that checks if the input starts with the
PotatoHead (`@>`) and outputs a placeholder message based
on the command. If there was no SpudCommand, then execute
the command with `subprocess.run(shell=True)` to allow for
paid features and productivity tools.

**NOTE:** Intercept `cd` and use `os.chdir()` to make the command functional.

### 1.C: The Configurations (COMPLETED)
A simple configuration file `.mash` that allows to change
the prompt and the color of it, with extra capabilities in
the future.

### 1.D: The TUI & Visuals (COMPLETED)
The full terminal experience. Create a "Welcome Header"
that displays when MaSH starts. Has menus for the config
settings and the tools.

### 1.E: The Polishing (COMPLETED)
Clean up this phase and ensure the code is clean and functional.

---

## Phase 2; The Workforce: (IN-PROGRESS)
These are the tools that are integrated with the terminal.
The first tool that takes focus will be the Project Manager
and then the Assistant Menu with be implemented after the
first plugin.

---

### Project Menu (IN-PROGRESS)
This menu helps the user create and maintain their projects
in a simple menu.

#### 2.A1: Project Creation (COMPLETE)
This menu allows the user to create a new project with the
required settings and configurations for provided features.

The information that is obtained are as follows:
* Name:
    - Cannot exist in the Projects list.
    - Cannot be greater than 15 characters.
    - Cannot be empty.

* Path:
    - Cannot be empty.
    - Has to be valid path format.

* Repo Link: (optional)
    - Is a valid link.
    - Cannot be empty.

#### 2.A2: Project Selection
A menu for managing the selected project from; repo
handling, quick tests, folder traversal with future plans
of system commands for easy folder manipulations.

##### 2.A2.1: Edit Menu
Allows the user to edit the projects information that was
gathered on creation.

##### 2.A2.2: Save Command
This command pushes the new changes to the repo
(if provided) and allows for the user to add a custom
message. Since `git push` requires a login, that will
be handled with a login section in a future version.

##### 2.A2.3: Run Command
This command runs the project with a set rule that the user
can set on first usage. This is ran in a `subprocess.Popen`
and allow for killing the run.

#### 2.A3: Polishing
Polish this Menu so that there will be no issues in the
future.

---

### Assistants Menu
This menu allows to create specific LLM models and chat
with them. They are able to have knowledge of projects by
getting a project path from the user and learning the
information via RAG.

#### 2.B1: Model Creator
This menu helps the user create a perfect Modelfile that
can be used with the chatting feature. The information that
is needed from the user is the following:

* Name
* Description
* Model
* System Prompt
* Temperture

Future version will allow for custom file creation and 
model editing, as well as RAG based data reading.

#### 2.B2: Model Chatting
This menu allows you to chat with the selected model
using a local inference model that is CPU optimized
like llama.cpp or something along those lines.

#### 2.B3: Polshing
Ensure this menu is also clean and hopefully not causing
any future issues.

#### 2.C: Final Checks
A final check and polishing to ensure code is clean and not
going to cause issues.

---

## Phase 3; Mashed Together:
    ***Need to complete Phase 2!***
