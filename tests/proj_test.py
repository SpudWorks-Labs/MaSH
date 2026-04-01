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
    {"title": "MaSH", "body": "/home/bruhtato/mash"},
    {"title": "SpudNet", "body": "/home/bruhtato/spudnet"},
    {"title": "SpudScout", "body": "/home/bruhtato/spudscout"}
]
MODELS = [
    {"title": "SpudNet", "body": "A simple smart model"},
    {"title": "SpudBrain", "body": "A high-end thinking model."}
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

class ListWindow(Frame):
    def __init__(self, title, item_list):
        self.window_title = title
        self.selected_index = 0
        self.top_index = 0
        self.item_list = item_list
        # 1. We initialize the Frame with a DynamicContainer as its body.
        # This makes the Frame itself the "Main_Window" object.
        super().__init__(
            title=self.window_title,
            body=DynamicContainer(self.get_dynamic_content)
        )

    def get_dynamic_content(self):
        _, term_height = shutil.get_terminal_size()
        
        # 1. Intent: Use roughly 2/3 of the screen (as per your current math)
        # But we set a MINIMUM height to prevent the crash
        parent_target_height = max(5, term_height - (term_height // 3))
        inner_space = parent_target_height - 2

        # 2. Safety Check: How many 3-line frames can actually fit?
        # If the answer is 0, we shouldn't try to render frames.
        visible_count = inner_space // 3

        if self.selected_index < self.top_index:
            self.top_index = self.selected_index
        elif self.selected_index >= self.top_index + visible_count:
            self.top_index = self.selected_index - visible_count + 1

        frames = []
        
        # 3. Only attempt to render if visible_count > 0
        if visible_count > 0:
            visible_items = self.item_list[self.top_index : self.top_index + visible_count]
            for i, item in enumerate(visible_items):
                actual_index = self.top_index + i
                title = ("> " + item['title']) if actual_index == self.selected_index else item['title']
                
                frames.append(
                    Frame(
                        title=title,
                        body=Window(height=1, content=FormattedTextControl(item['body']))
                    )
                )
        
        # 4. Always add the spacer to soak up extra room
        frames.append(Window())

        if not visible_items and visible_count > 0:
            return Window(content=FormattedTextControl(" No projects found."))
        elif visible_count <= 0:
            return Window(content=FormattedTextControl(" Terminal too small!"))

        # 5. Use Dimension for the height. This is more flexible than a raw int.
        return HSplit(frames, height=Dimension(preferred=parent_target_height, min=3))
        
        # return ScrollablePane(
        #     content=final_frames,
        #     height=6,
        #     show_scrollbar=True
        # )

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
    def __init__(self, id, title, commands, content=None):
        self.id = id
        self.title = title
        self.command_list = commands
        self.content = content
        self.projects = ListWindow(self.content["name"], self.content['data'])
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


class Test:
    def __init__(self):
        self.projects = Menu("pm", "Project Manager", ["create", "remove"], {"name": "Projects", "data": PROJECTS})
        self.ai = Menu("ai", "AI Assistants", ["chat", "train"], {"name": "Models", "data": MODELS})

        self.curr_menu = self.projects
        self.kb = KeyBindings()
        self.setup_keybindings()

    def setup_keybindings(self):
        self.kb.add('tab')(focus_next)
        @self.kb.add('up')
        def _(event):
            if self.curr_menu.projects.selected_index == 0:
                self.curr_menu.projects.selected_index = len(self.curr_menu.content['data']) - 1
            else:
                self.curr_menu.projects.selected_index -= 1

        @self.kb.add('down')
        def _(event):
            if self.curr_menu.projects.selected_index == len(self.curr_menu.content['data']) - 1:
                self.curr_menu.projects.selected_index = 0
            else:
                self.curr_menu.projects.selected_index += 1

        @self.kb.add('right')
        @self.kb.add('left')
        def _(event):
            if self.curr_menu.id == 'pm':
                self.curr_menu = self.ai
            elif self.curr_menu.id == 'ai':
                self.curr_menu = self.projects

            event.app.layout.focus(self.curr_menu.prompt.buffer)

        @self.kb.add('c-c')
        def _(event):
            event.app.exit()

    def get_layout_container(self):
        return self.curr_menu.display()

    def execute(self):
        container = DynamicContainer(self.get_layout_container)
        layout = Layout(container=container, focused_element=self.curr_menu.prompt.buffer)
        app = Application(layout=layout, key_bindings=self.kb, full_screen=True)
        app.run()


test = Test()
test.execute()
