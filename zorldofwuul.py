import framework
from framework.AbstractContext import AbstractContext
from colorama import Fore, Back, Style

zow_data = {
    "outside" : {
        "description" : "outside the main entrance of the university",
        "exits" : [None, "theater", "lab", "pub"]
    },
    "theater" : {
        "description" : "in a lecture theater",
        "exits" : [None, None, None, "outside"]
    },
    "pub" : {
        "description" : "in the campus pub",
        "exits" : [None, "outside", None, None]
    },
    "lab" : {
        "description" : "in a computing lab",
        "exits" : ["outside", "office", None, None]
    },
    "office" : {
        "description" : "in the computing admin office",
        "exits" : [None, None, None, "lab"]
    },
}


class WoZContext(AbstractContext):
    welcome_text = f"""{Fore.GREEN}
__________           .__       .___         _____   __      __            .__   
\____    /___________|  |    __| _/   _____/ ____\ /  \    /  \__ __ __ __|  |  
  /     //  _ \_  __ \  |   / __ |   /  _ \   __\  \   \/\/   /  |  \  |  \  |  
 /     /(  <_> )  | \/  |__/ /_/ |  (  <_> )  |     \        /|  |  /  |  /  |__
/_______ \____/|__|  |____/\____ |   \____/|__|      \__/\  / |____/|____/|____/
        \/                      \/                        \/                    
{Style.RESET_ALL}
{Fore.CYAN}Welcome to the Zorld of Wuul!{Style.RESET_ALL}
Zorld of Wuul is a new, incredibly boring adventure game.

"""
    current_room = None

    def __init__(self):
        super().__init__()
        world = {}
        # Add the key of each room as its name
        for key, roominfo in zow_data.items():
            world[key] = Room(key, **roominfo)
        # replace references to real rooms in the exits
        for key, room in world.items():
            room.exits = [world[exit] if exit is not None else None for exit in room.exits]
        # Set the current room        
        self.current_room = world['outside']


    def print_welcome(self):
        print(self.welcome_text)
        self.current_room.print_title()


    def print_help(self):
        print("You are lost. You are alone. You wander")
        print("around at the university.")


    def get_cursor(self):
        if self.current_room is None:
            return f"{Style.BRIGHT}> {Style.RESET_ALL}"
        return f"{Fore.MAGENTA}{Style.BRIGHT}[{self.current_room.name}]{Style.RESET_ALL}{Fore.WHITE}{Style.BRIGHT}> {Style.RESET_ALL}"
    

    def go_room(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        self.set_current_room(next_room)


    def set_current_room(self, new_room):
       self.current_room = new_room
       self.current_room.print_title()


class Room:
    possible_exits = ['north', 'east', 'south', 'west']
   
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits


    def print_title(self):
        print(f"You are {self.description}")


    def print_exits(self):
        exits = []
        for i in range(0, 4):
            if self.exits[i] is not None:
                exits.append(self.possible_exits[i])
        exit_string = ", ".join(exits)
        print(f"Exits are: {exit_string}")


    def get_index_of_direction(self, direction):
        # Find the array index of the given direction
        try:
          return self.possible_exits.index(direction)
        except Exception:
          raise ValueError(f'Unknown direction {direction}')


    def get_room_in_direction(self, direction):
        index = self.get_index_of_direction(direction)
        result = self.exits[index]
        if result is None:
            raise ValueError("There is no exit in that direction")
        return result


def configure_command_line_arguments(parser):
  # Add command line arguments, see: https://docs.python.org/3/library/argparse.html
  pass


if __name__ == '__main__':
    framework.run(WoZContext(), 
                  argparse_initialize_func=configure_command_line_arguments)