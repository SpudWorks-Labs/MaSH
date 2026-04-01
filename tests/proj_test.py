import shutil
from prompt_toolkit.application import Application, get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout.containers import HSplit, VSplit, Window, WindowAlign, DynamicContainer
from prompt_toolkit.layout import ScrollablePane, Dimension
from prompt_toolkit.layout.controls import FormattedTextControl, BufferControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.widgets import Frame, Box, TextArea
from prompt_toolkit.buffer import Buffer

# Assuming this exists globally or is passed in
PROJECTS = [
    {"name": "MaSH", "path": "/home/bruhtato/mash"},
    {"name": "SpudNet", "path": "/home/bruhtato/spudnet"},
    {"name": "SpudScout", "path": "/home/bruhtato/spudscout"}
]

class CommandWindow(Frame):
    def __init__(self, command_list):
        self.command_list = command_list
        self.command_list.append('exit')
        self.window_title = "Commands"
        super().__init__(
            title=self.window_title,
            body=DynamicContainer(self.get_dynamic_command_layout)
        )

    def get_dynamic_command_layout(self):
        # 1. Get width and calculate responsive spacing
        w, _ = shutil.get_terminal_size()
        space_len = max(2, w // 10) 
        space = " " * space_len
        
        lines = []
        current_line = space
        row_count = 1

        # 2. Build the command grid string
        for i, cmd in enumerate(self.command_list, 1):
            current_line += f"{cmd}{space}"
            # Every 3 items, push the current line to our list and reset
            if i % 3 == 0 or i == len(self.command_list):
                lines.append(current_line)
                current_line = space
                if i != len(self.command_list):
                    row_count += 1

        # 3. Return a simple Window. 
        # By avoiding ScrollablePane here, we stop the "Window too small" panic.
        return Window(
            content=FormattedTextControl("\n".join(lines)),
            height=row_count,
            align=WindowAlign.CENTER
        )

class ProjectWindow(Frame):
    def __init__(self):
        self.window_title = "Projects"
        self.selected_index = 0
        # 1. We initialize the Frame with a DynamicContainer as its body.
        # This makes the Frame itself the "Main_Window" object.
        super().__init__(
            title=self.window_title,
            body=DynamicContainer(self.get_dynamic_content)
        )

    def get_dynamic_content(self):
        # 2. Build the list of frames for each project
        frames = []
        for i, proj in enumerate(PROJECTS):
            name = proj['name']
            path = proj['path']

            if i == self.selected_index:
                name = "> " + name

            frames.append(
                Frame(
                    title=name,
                    body=Window(height=1, content=FormattedTextControl(path))
                )
            )
        
        # 3. CRITICAL: You must return the HSplit so DynamicContainer can show it.
        final_frames = HSplit(frames)

        return ScrollablePane(
            content=final_frames,
            height=6,
            show_scrollbar=True
        )

class PromptWindow(VSplit):
    def __init__(self, commands):
        self.command_list = commands
        self.event = None
        self.run = False
        self.buffer = Buffer(
            accept_handler=self.handle_command,
            multiline=False
        )
        super().__init__([
            Window(
                width=6,
                content=FormattedTextControl(" >>> ")
            ),
            Window(
                content=BufferControl(buffer=self.buffer)
            )
        ])

    def handle_command(self, buffer):
        command = buffer.text.strip().lower()
        buffer.text = ""
        
        if command == 'exit':
            get_app().exit()
            return False


        return False


class Menu:
    def __init__(self, title, commands):
        self.title = title
        self.command_list = commands
        self.projects = ProjectWindow()
        self.commands = CommandWindow(self.command_list)
        self.prompt = PromptWindow(self.command_list)

    def display(self):
        # 4. Now MainWindow behaves like any other prompt_toolkit widget.
        root_container = Frame(
            title=self.title,
            body=HSplit([
                self.projects,
                self.commands,
                self.prompt
            ])
        )
        return root_container

menu = Menu("Project Manager", ["create", "remove"])
kb = KeyBindings()
kb.add('tab')(focus_next)
@kb.add('up')
def _(event):
    if menu.projects.selected_index == 0:
        menu.projects.selected_index = len(PROJECTS)
    else:
        menu.projects.selected_index -= 1

@kb.add('down')
def _(event):
    if menu.projects.selected_index == len(PROJECTS):
        menu.projects.selected_index = 0
    else:
        menu.projects.selected_index += 1

@kb.add('c-c')
def _(event):
    event.app.exit()


container = menu.display()
layout = Layout(container=container, focused_element=menu.prompt.buffer)
# Create and run application.
application = Application(layout=layout, key_bindings=kb, full_screen=True)
application.run()