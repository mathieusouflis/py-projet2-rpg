class Entity:
    def __init__(self, name: str, description: str, level: int, xp: float, stats: array, attack_list: array):
        self.name = name
        self.description = description
        self.level = level
        self.xp = xp
        self.stats = stats
        self.attack_list = attack_list
        self.status = None

    def attack():
        pass

    def take_damage():
        pass

class Pnj(Entity):
    def __init__(self, dialog: array):
        self.dialog = dialog

    def interact():
        pass

class Player(Entity):
    def __init__(self, name: str, description: str, level: int, xp: float, stats: array, attack_list: array):
        super().__init__(name, description, level, xp, stats, attack_list)
        self.inventory = []
        self.coord = []

    def show_inventory():
        pass

    def use_item():
        pass

    def move():
        pass

    def add_xp():
        pass

class Monster(Entity):
    def __init__(self, name: str, description: str, level: int, stats: array, attack_list: array, dropable_items: array):
        super().__init__(name, description, level, 0, stats, attack_list)
        self.dropable_items = dropable_items

    def attack():
        pass

    def calculate_drops():
        pass

class Item:
    def __init__(self, name: str, description: str, effect: str):
        self.name = name
        self.descritpion = description
        self.effect = effect

class Equipable(Item):
    def __init__(self, name: str, description: str, effect: array):
        self.equiped = False

    def equip():
        pass

class Consomable(Item):
    def __init__(self, name: str, description: str, effect: array, durability: int):
        self.active = False
        self.durability = durability

    def use():
        pass

class Attack:
    def __init__(self, name: str, description: str, AHHHHHH: str, durability: int, effect: dict):
        self.name = name
        self.description = description
        self.AHHHHHH = AHHHHHH
        self.durability = durability
        self.effect = effect # {stat : dégats}

class Game:
    def __init__(self, name: str, main_player: Player):
        self.name = name,
        self.main_player = main_player

    def start():
        pass

    def save():
        pass

    def load():
        pass

class Combat:
    def __init__(self, player: Player, target: Monster):
        self.turn = 0
        self.player = player
        self.target = target

    def start():
        pass

    def turn():
        pass

    def end():
        pass

    def escape():
        pass

class Place:
    def __init__(self, name: str, description: str, monsters: Monster):
        self.name = name
        self.description = description
        self.monsters = monsters
        self.exploration = False

    def interact():
        pass
