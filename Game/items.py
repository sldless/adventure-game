import csv


class Item:
    """Properties of all items"""

    def __init__(self, config):
        self.config = None
        self.label = None
        self.name = None
        self.description = None
        self.location = None
        self.keywords = None
        self.type = None
        self.look_special = None
        self.use_words = None

        # Takes in a dictionary and assigns item properties according to labels
        self.config = config
        self.label = config['label']
        # one word, serves as key in dictionary and shortest name
        self.name = config['name']
        # short descriptive phrase
        self.description = config['description']
        # full detailed descriptive text
        self.location = config['location']
        # string matching label of starting room
        self.keywords = config['keywords'] + config['use_words']
        # a list of synonyms and other words that would help identify it
        # the use words are added to keywords list, so use words are a
        # subset of keywords, which allows them to be searched at the
        # same time
        self.type = config['type']
        # possible values: "carryable", "exit", "scenery", "hidden"
        self.look_special = config['look_special']
        # change this flag to true to trigger special room-specific
        # events when the item is examined
        self.use_words = config['use_words']


def populate():
    """
    Sets up item objects by creating a config dictionary for each one

    Sample config dictionary (can be copied for each new item):

    .. code-block:: python

        >>> config = {
        ...  'label':'LABEL',
        ...  'name':'NAME',
        ...  'description':'DESCRIPTION',
        ...  'location':'LOCATION',
        ...  'keywords':['KEYWORD1'],
        ...  'type':'TYPE'
        ...  'look_special': False
        ... }

    'label' :
        a single word string used as an internal id

    'name':
        the user-facing name of the item

    'description':
        the full verbose description

    'location':
        the label of the starting room
    'keywords':
        a list of keywords that the player might refer to the item as

    'type':
        a flag that determines properties.
        Possible values: "carryable", "scenery", "exit", "hidden"

    'look_special":
        set to True to trigger room-specific events when the item is examined
    """

    # runs each of the item creation functions
    # and returns a dictionary of all the items
    all_items = {}

    f = open('data/items.csv', 'r')
    reader = csv.DictReader(f)

    for row in reader:
        row['keywords'] = row['keywords'].split()
        row['use_words'] = row['use_words'].split()
        new_item = Item(row)

        all_items[new_item.label] = new_item

    return all_items
