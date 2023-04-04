from envparse import env
from command import Command
from context import Context

# This recurses up the directory tree until a file called '.env' is found.
env.read_envfile()

def init():
    c = Context()
    return c

if __name__ == '__main__':
    context = init()
    try:
        while True:
            command = Command(input('> '))
            if (command.execute(context)):
                break
    except KeyboardInterrupt:
        Command('exit').execute(context)    
