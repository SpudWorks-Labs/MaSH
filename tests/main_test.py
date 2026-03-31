
import shutil

from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout.containers import Window, DynamicContainer
from prompt_toolkit.layout import Dimension, HSplit, Layout, ScrollablePane
from prompt_toolkit.layout.controls import FormattedTextControl
from prompt_toolkit.widgets import Frame, TextArea


PROJECTS = [
    {"name": "MaSH Terminal", "path": "/home/bruhtato/Documents/SpudWorks/MaSH"},
    {"name": "SpudLang", "path": "/home/bruhtato/Documents/SpudWorks/Spud"},
    {"name": "SpudScout", "path": "/home/bruhtato/Documents/SpudWorks/SpudScout"},
]
COMMANDS = [
    "create", "delete", "exit"
]

class Test:
    def __init__(self):
        self.selected_index = 0
        self.kb = KeyBindings()
        self.setup_keybindings()

    def setup_keybindings(self):
        @self.kb.add('up')
        def _(event):
            focus_next
            if self.selected_index == 0:
                self.selected_index = len(PROJECTS)
            else:
                self.selected_index -= 1

        @self.kb.add('down')
        def _(event):
            focus_previous
            if self.selected_index == len(PROJECTS):
                self.selected_index = 0
            else:
                self.selected_index += 1

        @self.kb.add('c-c')
        def _(event):
            event.app.exit()


    @staticmethod
    def get_width():
        return shutil.get_terminal_size().columns

    def get_projects(self):
        for i, proj in enumerate(PROJECTS):
            name = proj['name']
            path = proj['path']

            if i == self.selected_index:
                name = "> " + name

            yield name, path

    # def get_project_frames(self):
    #     frames = []
    #     for i, proj in enumerate(PROJECTS):
    #         name = proj['name']
    #         path = proj['path']

    #         if i == self.selected_index:
    #             name = "> " + name

    #         frames.append(Frame(
    #             title=name,
    #             body=
    #         ))

    #     return frames

    def get_dynamic_projects(self):
        project_list = HSplit([
            Frame(
                title=proj_name, 
                body=TextArea(height=1, text=proj_path)
            ) for proj_name, proj_path in self.get_projects()
        ])

        return ScrollablePane(
            content=project_list,
            height=6,
            show_scrollbar=True 
        )

    def get_commands(self):
        w = self.get_width()
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
        commands, rows = self.get_commands()
        root_container = Frame(
            title="Project Manager",
            body=HSplit([
                DynamicContainer(self.get_dynamic_projects),
                Frame(
                    title="Commands",
                    body=Window(
                        height=rows,
                        content=FormattedTextControl(commands)
                    )
                )
            ])
        )

        layout = Layout(container=root_container)

        # Create and run application.
        application = Application(layout=layout, key_bindings=self.kb, full_screen=True)
        application.run()


if __name__ == '__main__':
    test = Test()
    test.display()
