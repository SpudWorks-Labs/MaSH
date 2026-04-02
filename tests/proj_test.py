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
from math import ceil

# Assuming this exists globally or is passed in
PROJECTS = [
    {"title": "MaSH", "body": "/home/bruhtato/mash"},
    {"title": "SpudNet", "body": "/home/bruhtato/spudnet"},
    {"title": "SpudScout", "body": "/home/bruhtato/spudscout"},
    {"title": "other", "body": "/home/bruhtato/other"},
    {"title": "tests", "body": "/home/bruhtato/tests"},
    {"title": "balls", "body": "/home/bruhtato/balls "},
    {"title": "spaghetti", "body": "/home/bruhtato/spaghetti"},
    {"title": "racoom", "body": "/home/bruhtato/racoom"},
    {"title": "worry", "body": "/home/bruhtato/worry"},
    {"title": "mcd", "body": "/home/bruhtato/mcd"},
    {"title": "burp", "body": "/home/bruhtato/burp"},
    {"title": "alive", "body": "/home/bruhtato/alive"}
]
MODELS = [
    {"title": "SpudNet", "body": "A simple smart model"},
    {"title": "SpudBrain", "body": "A high-end thinking model."}
]
COMMANDS = [

]

class CommandWindow(Frame):
    def __init__(self, command_list):
        self.command_list = command_list
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
        rows = 1

        # 2. Build the command grid string
        for i, cmd in enumerate(self.command_list, 1):
            current_line += f"{cmd}{space}"
            
            if i % 3 == 0:
                current_line += '\n'
                rows += 1

        # 3. Return a simple Window. 
        # By avoiding ScrollablePane here, we stop the "Window too small" panic.
        return Window(
            content=FormattedTextControl(current_line),
            height=rows,
            align=WindowAlign.CENTER
        )

class ListWindow(Frame):
    def __init__(self, title, item_list, id, height=3):
        self.window_title = title
        self.selected_index = 0
        self.top_index = 0
        self.item_list = item_list
        self.id = id
        self.height_denom = height
        # 1. We initialize the Frame with a DynamicContainer as its body.
        # This makes the Frame itself the "Main_Window" object.
        super().__init__(
            title=self.window_title,
            body=DynamicContainer(self.get_dynamic_content),
            height=Dimension(preferred=self.calculate_target_height())
        )

    def calculate_target_height(self):
        height = shutil.get_terminal_size()[1]
        return max(5, height // self.height_denom)

    def get_dynamic_content(self):
        height = shutil.get_terminal_size()[1]
        
        # 1. Intent: Use roughly 2/3 of the screen (as per your current math)
        # But we set a MINIMUM height to prevent the crash
        parent_target_height = self.calculate_target_height()
        inner_space = parent_target_height - 2

        # 2. Safety Check: How many 3-line frames can actually fit?
        # If the answer is 0, we shouldn't try to render frames.
        visible_count = max(1, ceil(inner_space // 2.5))

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
                if self.id != 'cmd':
                    title = ("> " + item['title']) if actual_index == self.selected_index else item['title']
                    body = item['body']
                else:
                    title = item['role']
                    body = item['content']

                frames.append(
                    Frame(
                        title=title,
                        body=Window(height=1, content=FormattedTextControl(body))
                    )
                )
        
        # 4. Always add the spacer to soak up extra room
        frames.append(Window())

        if not visible_items and visible_count > 0:
            return Window(content=FormattedTextControl(" Nothing to display."))
        elif visible_count <= 0:
            return Window(content=FormattedTextControl(" Terminal too small!"))

        # 5. Use Dimension for the height. This is more flexible than a raw int.
        return HSplit(frames)#, height=Dimension(preferred=parent_target_height, min=3))
        
        # return ScrollablePane(
        #     content=final_frames,
        #     height=6,
        #     show_scrollbar=True
        # )

class PromptWindow(VSplit):
    def __init__(self, commands, id, methods=None):
        self.id = id
        self.command_list = commands
        self.methods = methods
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
            self.methods['exit']()
            # return False

        if self.id == 'cmd':
            COMMANDS.append({
                'role': "user",
                'content': command
            })

        if command == '@>pm':
            self.methods['switch']('pm')
        elif command == '@>ai':
            self.methods['switch']('ai')

        return False


# class ConsoleWindows:
#     def __init__(self):


class Menu:
    def __init__(self, id, title, content, menu_type, commands=[], methods=None):
        self.id = id
        self.title = title
        
        if 'exit' not in commands:
            commands.append('exit')

        self.command_list = commands
        self.type = menu_type
        self.content = content
        self.methods = methods
        
        if self.type == 'list':
            self.main = [
                ListWindow(self.content["name"], self.content['data'], self.id, height=2),
                CommandWindow(self.command_list)
            ]

        elif self.type == 'console':
            self.main = ListWindow(self.content['name'], self.content['data'], self.id, height=1)
            
        self.prompt = PromptWindow(self.command_list, self.id, self.methods)

    def display(self):
        # 4. Now MainWindow behaves like any other prompt_toolkit widget.
        body_elements = self.main if isinstance(self.main, list) else [self.main]
        root_container = Frame(
            title=self.title,
            body=HSplit([
                *body_elements,
                Window(),
                self.prompt
            ])
        )

        return root_container


class Test:
    def __init__(self):
        methods = {
            'switch': self.switch_menu,
            'exit': self.exit_menu
        }
        self.main = Menu("cmd", "MaSH", {'name': "Terminal", 'data': COMMANDS}, 'console', methods=methods)
        self.projects = Menu('pm', "Project Manager", {'name': "Projects", 'data': PROJECTS}, 'list', methods=methods)
        self.ai_menu = Menu('ai', "AI Assistants", {'name': "Models", 'data': MODELS}, 'list', methods=methods)
        self.curr_menu = self.main
        self.last_menu = self.main
        self.kb = KeyBindings()
        self.setup_keybindings()

    def switch_menu(self, menu_id):
        not_same_id = None

        if self.last_menu is not None:
            not_same_id = (self.curr_menu.id != self.last_menu.id)

        if not_same_id is None or self.last_menu and not_same_id:
            self.last_menu = self.curr_menu

        if menu_id == 'pm':
            self.curr_menu = self.projects
        elif menu_id == 'cmd':
            self.curr_menu = self.main
        elif menu_id == 'ai':
            self.curr_menu = self.ai_menu
        
        get_app().layout.focus(self.curr_menu.prompt.buffer)

    def exit_menu(self):
        if self.last_menu is not None and self.last_menu.id != self.curr_menu.id:
            self.switch_menu(self.last_menu.id)
            self.last_menu = None
        else:    
            get_app().exit()

    def setup_keybindings(self):
        self.kb.add('tab')(focus_next)
        @self.kb.add('up')
        def _(event):
            if self.curr_menu.main[0].selected_index == 0:
                self.curr_menu.main[0].selected_index = len(self.curr_menu.content['data']) - 1
            else:
                self.curr_menu.main[0].selected_index -= 1

        @self.kb.add('down')
        def _(event):
            if self.curr_menu.main[0].selected_index == len(self.curr_menu.content['data']) - 1:
                self.curr_menu.main[0].selected_index = 0
            else:
                self.curr_menu.main[0].selected_index += 1

        # @self.kb.add('right')
        # @self.kb.add('left')
        # def _(event):
        #     if self.curr_menu.id == 'pm':
        #         self.curr_menu = self.ai
        #     elif self.curr_menu.id == 'ai':
        #         self.curr_menu = self.projects

        #     event.app.layout.focus(self.curr_menu.prompt.buffer)

        @self.kb.add('escape')
        @self.kb.add('c-c')
        def _(event):
            self.exit_menu()

    def get_layout_container(self):
        return self.curr_menu.display()

    def execute(self):
        container = DynamicContainer(self.get_layout_container)
        layout = Layout(container=container, focused_element=self.curr_menu.prompt.buffer)
        app = Application(layout=layout, key_bindings=self.kb, full_screen=True)
        app.run()


test = Test()
test.execute()
