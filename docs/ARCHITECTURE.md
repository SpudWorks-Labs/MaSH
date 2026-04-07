# MaSH: Architecture (M.V.P.)

MaSH is a productivity terminal designed for simple
customization and seamless tool integration.

---

## Program Model
MaSH operates as a standard terminal shell but monitors for
a unique trigger: the `@>` prefix. These commands invoke
the "Workforce" tools for project management, Git, AI
assistance, and other productivity tools.

### Primary Command Triggers:
* `@>ai`: Access AI assistants and their specialized tools.
* `@>projects`: Launch the project management menu.

---

## Development Phases
1. **The Terminal Emulator**: Establish a functional,
    customizable shell environment.
2. **The Workforce**: Integrate productivity boosters
    including Project Management, Git automation, and
    Local AI.
3. **Mashed Together**: Transition to a standalone binary
    (Rust or C/C++) for maximum performance and portability.


## Project Structure
To ensure that adding new "Workforce" tools doesn't clutter
the core terminal logic, we use a modulated file-structure.


```plaintext
MaSH/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── CHANGELOG.md
│   ├── DEV_LOG.md
│   └── ROADMAP.md
├── src/
│   ├── core/           # Shell and terminal logic.
│   │   ├── mash_config.py
│   │   └── proc_commands.py
│   ├── menus/          # Logic for the menus.
│   │   ├── assistans_menu.py
│   │   ├── mash_menu.py
│   │   ├── plugin_menu_template.py
│   │   └── projects_menu.py
│   └── main.py
├── tests/              # Random tests.
│   ├── ...
│   ...
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```
