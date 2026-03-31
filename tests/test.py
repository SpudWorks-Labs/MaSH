import shutil
from prompt_toolkit.application import Application
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout.containers import HSplit, VSplit, Window, WindowAlign, DynamicContainer
from prompt_toolkit.layout import ScrollablePane, Dimension
from prompt_toolkit.layout.controls import FormattedTextControl, BufferControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import Frame, Box, TextArea
from prompt_toolkit.buffer import Buffer

# --- Mock Data ---
PROJECTS = [
    {"name": "MaSH Terminal", "path": "/home/bruhtato/Documents/SpudWorks/MaSH"},
    {"name": "Project Phoenix", "path": "/home/bruhtato/Documents/SpudWorks/Phoenix"},
    {"name": "SpudLang Parser", "path": "/home/bruhtato/Documents/SpudWorks/SpudLang"},
    {"name": "Web Scraper", "path": "/home/bruhtato/Documents/Tools/Scraper"},
]

COMMANDS = [
    "create", "delete", "exit"
]

# --- Reactive Helpers ---
def get_width():
    return shutil.get_terminal_size().columns

def get_dynamic_border():
    return "_" * get_width()

def get_dynamic_header():
    w = get_width()
    title = "Project Manager"
    padding = (w - len(title) - 2) // 2
    return f"|{'_' * padding}{title}{'_' * (w - len(title) - padding - 2)}|"

class ProjectManager:
    def __init__(self):
        self.selected_index = 0
        self.kb = KeyBindings()
        self.setup_keybindings()

    def get_project_content(self):
        """
        This generates the text for the Projects box.
        It uses the current width to ensure the ASCII bars scale.
        """
        w = get_width()
        # Calculate bar length based on current width (approx 25% of screen)
        bar_len = max(5, w // 6)
        bar = "_" * bar_len
        
        lines = []
        for i, proj in enumerate(PROJECTS):
            if i == self.selected_index:
                lines.append(f"        > {bar}{proj['name']}{bar}\n")
                lines.append(f"         |{bar}{proj['path']}|\n\n")
            else:
                lines.append(f"          {bar}{proj['name']}{bar}\n")
                lines.append(f"          {proj['path']}\n\n")
        return "".join(lines)

    def setup_keybindings(self):
        # @self.kb.add('up')
        # def _(event):
        #     self.selected_index = max(0, self.selected_index - 1)
        # @self.kb.add('down')
        # def _(event):
        #     self.selected_index = min(len(PROJECTS) - 1, self.selected_index + 1)
        # @self.kb.add('left')
        @self.kb.add('tab')(focus_next)
        @self.kb.add('s-tab')(focus_previous)
        @self.kb.add('c-c')
        def _(event):
            event.app.exit()

    def run(self):
        # We use a Window with a callable 'content' to make it reactive
        project_display = Window(
            content=FormattedTextControl(self.get_project_content),
            align=WindowAlign.CENTER  # This centers the whole block in the Frame
        )

        root_container = HSplit([
            # Reactive Top Border
            Window(height=1, content=FormattedTextControl(get_dynamic_border)),
            # Reactive Header
            Window(height=1, content=FormattedTextControl(get_dynamic_header)),
            
            # The Main Container
            Frame(
                title="Projects",
                body=Box(project_display, padding=1),
            ),
            
            Frame(
                title="Commands",
                body=Window(
                    height=1, 
                    content=FormattedTextControl("create             delete"), 
                    align=WindowAlign.CENTER
                ),
            ),

            # Prompt Area
            VSplit([
                Window(width=6, content=FormattedTextControl("|   >>> ")),
                Window(content=BufferControl(buffer=Buffer())),
                Window(width=1, content=FormattedTextControl("|")),
            ]),
            
            # Reactive Bottom Border
            Window(height=1, content=FormattedTextControl(get_dynamic_header)),
        ])

        layout = Layout(root_container)
        # full_screen=True is vital for the dynamic resizing to work properly
        app = Application(layout=layout, key_bindings=self.kb, full_screen=True)
        app.run()

class PM:
    def __init__(self):
        self.kb = KeyBindings()
        self.selected_index = 0
        self.setup_keybindings()

    def setup_keybindings(self):
        @self.kb.add('up')
        def _(event):
            self.selected_index = max(0, self.selected_index - 1)
        @self.kb.add('down')
        def _(event):
            self.selected_index = min(len(PROJECTS) - 1, self.selected_index + 1)
        @self.kb.add('left')
        @self.kb.add('c-c')
        def _(event):
            event.app.exit()

    def get_projects(self):
        w = get_width()
        bar_len = max(5, w // 6)
        space_len = max(3, w // 6)
        bar = "_" * bar_len
        space = " " * space_len
        lines = []

        for i, proj in enumerate(PROJECTS):
            if i == self.selected_index:
                lines.append(f"{space}> {bar} {proj['name']}{bar}\n")
                lines.append(f"{space}|{bar} {proj['path']}|\n\n")
            else:
                lines.append(f"{space}{bar} {proj['name']}{bar}\n")
                lines.append(f"{space}{proj['path']}\n\n")

        return "".join(lines)

    def get_project_frames(self):
        frames = []
        w = get_width()
        bar_len = max(5, w // 6)
        space_len = max(3, w // 6)
        bar = "_" * bar_len
        space = " " * space_len

        for i, proj in enumerate(PROJECTS):
            title = proj['name']
            body = proj['path']

            if i == self.selected_index:
                title = "> " + title
                # title = f"{space}> {bar} {proj['name']}{bar}"
                # body = f"{space}| {bar} {proj['path']}|"
            # else:
                # title = f"{space}| {bar} {proj['name']}{bar}"
                # body = f"{space}| {bar} {proj['path']}|"

            # print(title)
            # print(body)
            frames.append(Frame(
                title=FormattedTextControl(title),
                body=FormattedTextControl(body))
            )

        return frames

    def get_commands(self):
        w = get_width()
        space_len = max(3, w // 6)
        space = " " * space_len
        commands = space

        for i, command in enumerate(COMMANDS):
            i += 1
            commands += command

            if i % 3 == 0:
                commands += "\n"
            else:
                commands += space

        return commands

    def get_proj(self):
        for i, proj in enumerate(PROJECTS):
            title = proj['name']
            body = proj['path']

            if i == self.selected_index:
                title = "> " + title
            
            yield title, body

    def render_project(self):
        project_display = Window(
            content=FormattedTextControl(self.get_projects),
            align=WindowAlign.CENTER
        )
        root_container = HSplit([
            Window(height=1, content=FormattedTextControl(get_dynamic_border)),
            Window(height=1, content=FormattedTextControl(get_dynamic_header)),
            Frame(
                title="Projects",
                body=Window(
                    height=6,
                    content=FormattedTextControl(self.get_projects)
                )
            ),
            Frame(
                title="Commands",
                body=Window(
                    height=1,
                    content=FormattedTextControl(self.get_commands)
                )
            ),
            VSplit([
                Window(width=6, content=FormattedTextControl("|   >>> ")),
                Window(content=BufferControl(buffer=Buffer())),
                Window(width=1, content=FormattedTextControl("|")),
            ]),
            Window(height=5, content=FormattedTextControl(get_dynamic_border))
        ])

        projs = []
        for title, body in self.get_proj():
            projs.append(Frame(title=title, body=body))
        
        # root_container = Frame(
        #     title="Project Manager",
        #     body=Frame(
        #         title=PROJECTS[0]['name'],
        #         body=PROJECTS[0]['path']
        #     )
        # )

        root_container = Window(content=FormattedTextControl("Project Manager"))

        layout = Layout(root_container)

        app = Application(layout=layout, key_bindings=self.kb, full_screen=True)
        app.run()


class Test:
    def __init__(self):
        self.selected_index = 0
        self.kb = KeyBindings()
        self.setup_keybindings()

    def setup_keybindings(self):
        @self.kb.add('up')
        def _(event):
            self.selected_index -= 1
        @self.kb.add('down')
        def _(event):
            self.selected_index += 1
        @self.kb.add('left')
        @self.kb.add('c-c')
        def _(event):
            event.app.exit()

    def get_project_frames(self):
        frames = []
        w = get_width()
        bar_len = max(5, w // 6)
        space_len = max(3, w // 6)
        bar = "_" * bar_len
        space = " " * space_len

        for i, proj in enumerate(PROJECTS):
            title = proj['name']
            if i == self.selected_index:
                title = "> " + title  # This will now update on every keypress
            
            frames.append(
                Window(
                    content=FormattedTextControl(title)
                )
            )

    def get_commands(self):
        w = get_width()
        space_len = max(3, w // 6)
        space = " " * space_len
        commands = space
        rows = 0

        for i, command in enumerate(COMMANDS):
            i += 1
            commands += command

            if i % 3 == 0:
                commands += "\n"
                rows += 1
            else:
                commands += space

        return commands, rows
    
    def display(self):
        # Instead of calling it once, we pass the function name to DynamicContainer
        # Note: We remove the () so we pass the 'callable'
        # project_manager_body = DynamicContainer(self.get_project_frames)
        commands, rows = self.get_commands()

        root_container = Frame(
            ScrollablePane(
                HSplit(
                    [
                        Frame(TextArea(text=f"label-{i}"), width=Dimension())
                        for i in range(20)
                    ]
                )
            )
        # ScrollablePane(HSplit([TextArea(text=f"label-{i}") for i in range(20)]))
        )

        layout = Layout(root_container)

        app = Application(layout=layout, key_bindings=self.kb, full_screen=True)
        app.run()

if __name__ == "__main__":
    test = Test()
    test.display()
    