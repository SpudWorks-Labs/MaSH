# MaSH - The Productive Terminal

MaSH is a simple and efficient terminal designed to boost
productivity by integrating essential developer tools; Git,
project management, and AI, directly into your command line.

---

## Why MaSH?
Context-switching is a "flow-state" killer. Developers
lose hours every week jumping between their terminal,
browser-based AI chats, and project management dashboards.

MaSH keeps you in the zone. By using the `@>` command
prefix, you access a suite of workforce tools without
ever leaving your terminal.

### Features (The MVP)
* **@>ai**: Integrated AI assistants with tool-calling
capabilities.
* **@>projects**: A built-in manager to track and pivot
between projects.
* **@>repos**: Seamless Git integration to handle code
versioning.

---

## Installation & Quickstart
```bash
# ~ First, clone the repo and enter that directory. ~ #
git clone https://github.com/SpudWorks-Labs/MaSH
cd MaSH

# ~ Next, create a virtual environment. ~ #
python -m venv .name_of_env
source .name_of_env/bin/activate

# ~ Then, install the required dependencies. ~ #
pip install -r requirements.txt

# ~ Finally, run the program. ~ #
python src/main.py
```

---

## Phase Roadmap
**Phase 1; The Terminal Emulator:**
    A customizable terminal prototype built in Python.

**Phase 2; The Workforce:**
    Implementation of the AI, Project and Git integration
    tools.

**Phase 3; Mashed Together:**
    Standalone, high-performance version of *MaSH Terminal*
    using Rust.

For more info, check [ARCHITECTURE](docs/ARCHITECTURE.md)

---

## Important Acknowledgements
Created by Human Developers using AI Assistance.
