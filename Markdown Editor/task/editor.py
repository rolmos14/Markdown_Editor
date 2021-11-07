class Markdown:

    def __init__(self):
        self.formatters = ["plain", "bold", "italic", "header", "link", "inline-code",
                           "new-line"]  # "ordered-list", "unordered-list",
        self.commands = ["!help", "!done"]
        self.text = ''

    def help(self):
        print("Available formatters: " + " ".join(self.formatters))
        print("Special commands: " + " ".join(self.commands))

    def done(self):
        pass

    def plain(self):
        self.text += self.input_text()

    def bold(self):
        self.text += f"**{self.input_text()}**"

    def italic(self):
        self.text += f"*{self.input_text()}*"

    def header(self):
        while True:
            level = int(input("Level: "))
            if level in range(1, 7):
                self.text += level * "#" + " " + self.input_text() + "\n"
                break
            print("The level should be within the range of 1 to 6.")

    def link(self):
        self.text += f"[{input('Label: ')}]"
        self.text += f"({input('URL: ')})"

    def inline_code(self):
        self.text += f"`{self.input_text()}`"

    def new_line(self):
        self.text += "\n"

    def input_text(self):
        return input("Text: ")

    def menu(self):
        while True:
            command = input("Choose a formatter: ")
            if command == "!done":
                self.done()
                break
            if command == "!help":
                self.help()
            elif command not in self.formatters:
                print("Unknown formatting type or command")
            else:
                # Substitute '-' by '_' for inline-code and new-line commands
                command = command.replace('-', '_')
                # Call method indirectly
                getattr(self, command)()
                # Print accumulated formatted text
                print(self.text)


editor = Markdown()
editor.menu()
