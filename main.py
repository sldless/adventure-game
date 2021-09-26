from game import Inventory, Map, Mobile, Engine


def get_engine():
    inventory = Inventory()
    main_map = Map()

    player = Mobile(inventory, main_map.all_rooms['tube_room'])
    return Engine(main_map, player).move_into(player.location.label)


def main():
    main_engine = get_engine()

    while not main_engine.player.victory:
        main_engine.parse(main_engine.prompt())

    main_engine.victory()


if __name__ == '__main__':
    main()
