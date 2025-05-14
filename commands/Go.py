import commands
from zorldofwuul import Room

class Go(commands.AbstractCommand):
    """
    Example custom command
    """
    
    def __init__(self, args):
        super().__init__(args)
        self.is_undoable = True


    def print_help(self, context):
        print("Move through the exit in the specified direction")
        print(f"Possible arguments: {', '.join(Room.possible_exits)}")
       

    def execute(self, context):
        if len(self.args) == 0:
            raise ValueError("Go where?")
        # Store the current room for undo
        self.previous_room = context.current_room
        context.go_room(self.args[0].lower())
        return False


    def undo(self, context):
        context.set_current_room(self.previous_room)
        return False
