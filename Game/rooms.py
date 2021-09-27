import csv


class Room:
    """Organizes and manipulates rooms."""

    def __init__(self, config):
        self.visits = 0

        self.config = None
        self.label = None
        self.verbose_description = None
        self.terse_description = None
        self.items = None
        self.item_list = None
        self.exit_list = None
        self.exits = None

        self.config = config

        self.label = config['label']
        self.verbose_description = config['verbose_description']
        self.terse_description = config['terse_description']

    def extra_description(self):
        print('\n')
        # prints description of items and exits
        for i, item in self.items.items():
            if item.type != 'hidden':
                print("There is a %s here." % item.name)
        for i, _exit in self.exits.items():
            print("There is a %s to the %s." % (_exit.name, _exit.direction))

    def describe_verbose(self):
        """Prints the verbose room description."""
        print("\n%s" % self.verbose_description)
        self.extra_description()

    def describe_terse(self):
        """prints the terse room description."""
        print("\n%s" % self.terse_description)
        self.extra_description()

    def describe(self):
        """The main description printing function:
            - checks to see if the player has been here before
            - prints the verbose description on the first visits
            and the terse description on all others.
            Always prints descriptions of items and exits.
        """
        if self.visits == 0:
            self.describe_verbose()
            self.visits += 1
        else:
            self.describe_terse()

    def add_items(self, item_list):
        """Iterates through the item dictionary and makes a new dictionary
            of items whose location matches the room.
        """
        self.item_list = item_list
        self.items = {}

        for key, item in self.item_list.items():
            if item.location == self.label:
                self.items[item.label] = item

    def add_exits(self, exit_list):
        self.exit_list = exit_list
        self.exits = {}

        for key, _exit in self.exit_list.items():
            if _exit.location == self.label:
                self.exits[_exit.label] = _exit


def populate():
    all_rooms = {}

    with open("data/rooms.csv", "r") as f:
        for config in csv.DictReader(f):
            new_room = Room(config)
            all_rooms[new_room.label] = new_room

    return all_rooms
