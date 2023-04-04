from envparse import env
from command import Command
from context import Context
import readline
COMMANDS = ['extra', 'extension', 'stuff', 'errors',
            'email', 'foobar', 'foo']

def complete(text, state):
    for cmd in COMMANDS:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1

# This recurses up the directory tree until a file called '.env' is found.
env.read_envfile()

def init():
    c = Context()
    return c

if __name__ == '__main__':
    context = init()
    readline.parse_and_bind("tab: complete")
    readline.set_completer(complete)
    try:
        while True:
            command = Command(input('> '))
            if (command.execute(context)):
                break
    except KeyboardInterrupt:
        Command('exit').execute(context)    
