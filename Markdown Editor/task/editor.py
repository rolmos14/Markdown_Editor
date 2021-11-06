class Markdown:

    def __init__(self):
        self.formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list",
                           "unordered-list", "new-line"]
        self.commands = ["!help", "!done"]

    def help(self):
        print("Available formatters: " + " ".join(self.formatters))
        print("Special commands: " + " ".join(self.commands))

    def done(self):
        pass

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


editor = Markdown()
editor.menu()
