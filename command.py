from colors import Color

class Command:
    NONE = "none"
    UNKNOWN = "-1"

    def __init__(self, input):
        splitted = input.split()
        self.type = self.getType(splitted)
        self.args = splitted[1:]

    def getType(self, input):
        if (len(input) < 1):
            return Command.NONE
        word = input[0].lower()
        if (word in ["execute", "__init__"]):
            return Command.UNKNOWN
        return word

    def execute(self, context):
        method = getattr(self, self.type, None)
        if (not callable(method)):
            return self.unknown(context)
        return method(context)

    def test(self, e):
        for index, row in e.classroom.iterrows():
            print(row['github_username'])
    
    def repos(self, e):
        print(", ".join(e.repoFolders()))

    def clone(self, e):
        existing = e.repoFolders()
        for index, row in e.classroom.iterrows():
            if row['github_username'] not in existing:
                e.clone(row)

    def exit(self, e):
        print("Closing....")
        e.close()
        print(Color.fg.green + "Thank you for using CTShell" + Color.reset)
        return True

    def none(self, e):
        print(Color.fg.orange + "Type a command" + Color.reset)
        return False

    def unknown(self, e):
        print(Color.fg.red + Color.bold + self.type + Color.reset + Color.fg.red + " is not a valid command!" + Color.reset)
        return False

