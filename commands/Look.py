import commands

class Look(commands.AbstractCommand):
    """
    Example custom command.
    """

    def print_help(self, context):
        print(f"Look around and see details of the current room.")


    def execute(self, context):
        room = context.current_room
        room.print_title()
        print("")
        room.print_exits()
        return False
