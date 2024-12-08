from rich.console import Console
from rich.prompt import Prompt
from os import system

console = Console()

class Game:
    def __init__(self, name: str):
        self.name = name
        self.main_player = None

        def spawn_interaction(place):
            naration = [
                ("-", "Vous vous réveillez lentement, déboussolé vous entendez des bruits peu reconnaissables…"),
                ("-", "Vos yeux s'ouvrent lentement..."),
                ("Vous dans vos pensées", "Ou suis-je…? Quels sont ces bruits...?"),
                ("...", f"... ? ... !? {self.main_player.name} !!!?"),
                ("Vous, déboussolé", "Ou.. Ou suis-je..? Et qui êtes vous..?"),
                ("...", "Ah ! J'ai bien cru que vous étiez morte !"),
                ("Vous, lentement", "Mais qui..."),
                ("...", "Chut ! Laissez moi me présenter, je me nome Loic et je serais ton guide tout au long de cette aventure !"),
                ("Vous, encore confus", "Une aventure ? Mais de quoi parlez-vous ?"),
                ("Loic, avec un sourir énigmatique", f"Ah, {self.main_player.name} ! Vous avez tant à découvrir. Vous vous trouvez dans un monde extraordinaire, rempli de magie et de mystères."),
                ("Vous, en vous redressant lentement", "Je ne comprends pas... Comment suis-je arrivée ici ?"),
                ("Loic", "C'est une excellente question, mais malheureusement, je n'ai pas la réponse. Ce que je sais, c'est que vous avez un rôle crucial à jouer dans ce monde."),
                ("Vous, en regardant autour de vous", "Et quel est ce rôle exactement ?"),
                ("Loic", f"Cela, {self.main_player.name}, c'est à vous de le découvrir. Mais ne vous inquiétez pas, je serai là pour vous guider à chaque étape."),
                ("-", "Soudain, un bruit étrange résonne au loin. Loic se tourne brusquement."),
                ("Loic, d'un ton urgent", "Nous devons partir. Ce monde peut être dangereux pour ceux qui ne le connaissent pas. Suivez-moi !"),
                ("-", "Vous hésitez un instant, puis décidez de suivre Loic. Après tout, il semble être votre seul allié dans ce monde étrange."),
                ("-", "Alors que vous vous mettez en route, vous ne pouvez vous empêcher de vous demander ce qui vous attend dans cette mystérieuse aventure...")
            ]

            dialog.dialog(naration)
            self.main_player.move(self.places["Souflis Forest"])

        def souflis_forest_interaction(place):
            pass

        def ici_tout_le_monde_perd_interaction(place):
            pass

        def domaine_des_souflis_interaction(place):
            pass

        def le_casino_du_cartier_des_plaisirs_interaction(place):
            pass

        def le_temple_des_1000_moines_interaction(place):
            pass

        def hetic_interaction(place):
            pass

        # Initialisation des places sans les connexions
        spawn = Place(name="Spawn", description="Le point de départ du joueur", monsters=[], interaction=spawn_interaction)
        souflis_forest = Place(name="Souflis Forest", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=souflis_forest_interaction)
        ici_tout_le_monde_perd = Place(name="Ici tout le monde perd", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=ici_tout_le_monde_perd_interaction)
        domaine_des_souflis = Place(name="Domaine des Souflis", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=domaine_des_souflis_interaction)
        casino = Place(name="Le casino du cartier des plaisirs", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=le_casino_du_cartier_des_plaisirs_interaction)
        temple = Place(name="Le temple des 1 000 moines", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=le_temple_des_1000_moines_interaction)
        hetic = Place(name="Hetic", description="Un endroit où vous pouvez trouver des ressources", monsters=[], interaction=hetic_interaction)
        # Connexions entre les places
        spawn.places_around = {"east": souflis_forest}
        souflis_forest.places_around = {
            "west": spawn,
            "north": ici_tout_le_monde_perd,
            "north-east": domaine_des_souflis,
            "east": hetic,
            "south-east": casino,
            "south": temple,
        }
        ici_tout_le_monde_perd.places_around = {"south": souflis_forest}
        domaine_des_souflis.places_around = {"south-west": souflis_forest}
        casino.places_around = {"west": souflis_forest}
        temple.places_around = {"north-west": souflis_forest}
        hetic.places_around = {"west": souflis_forest}

        # Stockage des places
        self.places = {
            "Spawn": spawn,
            "Souflis Forest": souflis_forest,
            "Ici tout le monde perd": ici_tout_le_monde_perd,
            "Domaine des Souflis": domaine_des_souflis,
            "Le casino du cartier des plaisirs": casino,
            "Le temple des 1 000 moines": temple,
            "Hetic": hetic,
        }

        self.attacks = {
            "Bois de boulogne": Attack(name="Bois de boulogne", description="", battle_cry="", durability=100, effect={"damage": 10} ),
            "Course rapide": Attack(name="Course rapide", description="", battle_cry="", durability=100, effect={"damage": 10} ),
            "Souplesse du judoka": Attack(name="Souplesse du judoka", description="", battle_cry="Go muscu", durability=100, effect={"damage": 10} ),
            "Poing de feu": Attack(name="Poing de feu", description="", battle_cry="Brule en enfer", durability=100, effect={"damage": 10} ),
            "Coup de tonerre": Attack(name="Coup de tonerre", description="", battle_cry="Ça va piquer", durability=100, effect={"damage": 10} ),
            "Grattage du délégué": Attack(name="Grattage du délégué", description="", battle_cry="Donne moi tes hp", durability=100, effect={"damage": 10} ),
            "Lancé de talon": Attack(name="Lancé de talon", description="", battle_cry="Prend toi mon talon", durability=100, effect={"damage": 10} ),
            "Griffure": Attack(name="Griffure", description="", battle_cry="Roarrrr", durability=100, effect={"damage": 10} ),
            "Explosion": Attack(name="Explosion", description="", battle_cry="Araaaaa", durability=100, effect={"damage": 10} ),
            "Vol rapide": Attack(name="Vol rapide", description="", battle_cry="Bismilah", durability=100, effect={"damage": 10} ),
            "Charme": Attack(name="Charme", description="", battle_cry="Mouah 💋", durability=100, effect={"damage": 10} ),
            "Chant brutal": Attack(name="Chant brutal", description="", battle_cry="Dès que je chanterais tu deviendras sourd.", durability=100, effect={"damage": 10} ),
            "Kamehameha": Attack(name="Kamehameha", description="", battle_cry="Redonne mon couscous", durability=100, effect={"damage": 10} ),
            "Malaka": Attack(name="Malaka", description="", battle_cry="Mange mon grec", durability=100, effect={"damage": 10} ),
            "Control Mental": Attack(name="Control Mental", description="", battle_cry="Au hazard", durability=100, effect={"damage": 10} ),
            "Gear 5": Attack(name="Gear 5", description="", battle_cry="Youhouu", durability=100, effect={"damage": 10} ),
            "Fara 1": Attack(name="Fara 1", description="", battle_cry="", durability=100, effect={"damage": 10} ),
            "Fara 2": Attack(name="Fara 2", description="", battle_cry="", durability=100, effect={"damage": 10} ),
            "Amel 1": Attack(name="Amel 1", description="", battle_cry="", durability=100, effect={"damage": 10} ),
            "Amel 2": Attack(name="Amel 2", description="", battle_cry="", durability=100, effect={"damage": 10} ),
            "Marteau du Forain": Attack(name="Marteau du Forain", description="", battle_cry="Kévin abat son marteau avec fracas, déclenchant une onde de choc qui fait vibrer les miroirs autour de vous.", durability=100, effect={"damage": 100}),
            "Billes de Loterie Explosives": Attack(name="Billes de Loterie Explosives", description="", battle_cry="Il lance une poignée de billes colorées qui explosent en gerbes de lumière aveuglante.", durability=100, effect={"damage": 100}),
            "Claque de la Poigne Gigantesque": Attack(name="Claque de la Poigne Gigantesque", description="", battle_cry="Il prépare une claque chargée, des veines lumineuses pulsent sur la main, et un bruit sourd de tension monte dans l’air. L’impact crée une onde de choc qui soulève poussière et débris tout autour.", durability=1, effect={"damage": 100}),
            "Le Lasso de Soie": Attack(name="Le Lasso de Soie", description="Anjaro utilise un lasso en soie fine, qu'il fait briller comme une étoile. Il l’envoie avec élégance pour attraper ses ennemis et les ramener vers lui avec un mouvement fluide et gracieux.", battle_cry="TU M'ES ACCROCHÉ… ET J'AI UN CRÂNE À PRÉSERVER !", durability=100, effect={"damage": 100}),
            "La Roulade du Gentleman": Attack(name="La Roulade du Gentleman", description="Anjaro effectue une roulade parfaitement chorégraphiée, évitant les attaques ennemies tout en décochant un coup de pied agile, comme un maître de danse.", battle_cry="UNE DANSE AU RYTHME DU STYLE !", durability=100, effect={"damage": 100}),
            "Le Vent du Chapeau": Attack(name="Le Vent du Chapeau", description="Anjaro effectue un mouvement rapide, et son chapeau élégant se transforme en un projecteur de lumière qui éblouit temporairement les ennemis autour de lui.", battle_cry="MON STYLE, MA PUISSANCE !", durability=100, effect={"damage": 100}),
            "Le Crâne de Lumière": Attack(name="Le Crâne de Lumière", description="Anjaro se tient droit, prend une pause pour s'assurer que son crâne est parfaitement poli, puis libère une lumière aveuglante depuis son crâne chauve, envoyant une onde d'énergie brillante dans toute la zone. L'onde déstabilise ses ennemis, tout en rétablissant l’éclat de son apparence avec une touche de perfection.", battle_cry="VOUS NE POUVEZ PAS FAIRE CONCURRENCE AVEC LE CRÂNE DU MAÎTRE !", durability=1, effect={"damage": 100}),
            "Le Marteau de la Banque": Attack(name="Le Marteau de la Banque", description="Mathieu fait apparaître un énorme marteau doré en forme de lingot et le balance violemment sur le sol, créant une onde de choc étincelante.", battle_cry="TA BOURSE NE VA PAS AIMER ÇA !", durability=100, effect={"damage": 100}),
            "Le Lancer de Pièce Fétiche": Attack(name="Le Lancer de Pièce Fétiche", description="Il saisit une pièce dorée et la propulse à une vitesse fulgurante, frappant l’ennemi directement entre les yeux.", battle_cry="C’EST À MOI QUE TU LA DOIS, LA MONNAIE !", durability=100, effect={"damage": 100}),
            "Le Coup du Pantalon Traître": Attack(name="Le Coup du Pantalon Traître", description="Mathieu arrache un pan de ses vêtements et le fait tournoyer, créant un vent si puissant qu’il emporte ses adversaires.", battle_cry="CES FRINGUES NE SONT PAS JUSTE POUR LE STYLE !", durability=100, effect={"damage": 100}),
            "L’Écran Noir de la Dette": Attack(name="L’Écran Noir de la Dette", description="Mathieu tend les bras, et un immense écran translucide apparaît au-dessus de l’arène, projetant une lumière éblouissante. Sur cet écran, une facture gigantesque s’affiche avec des chiffres astronomiques qui clignotent, plongeant ses ennemis dans une terreur indescriptible.", battle_cry="ET SI TU PAYAIS TES IMPÔTS ?!", durability=1, effect={"damage": 100}),
            "Low Kick du Kangourou": Attack(name="Low Kick du Kangourou", description="", battle_cry="", durability=100, effect={"damage": 100}),
            "Bouclier du lémurien": Attack(name="Bouclier du lémurien", description="", battle_cry="", durability=100, effect={"damage": 100}),
            "Déferlante de la jungle": Attack(name="Déferlante de la jungle", description="", battle_cry="", durability=1, effect={"damage": 100}),
            "Coup du Lotus Brisé": Attack(name="Coup du Lotus Brisé", description="Un coup puissant et ciblé, imitant l’éclosion brutale d’un lotus.", battle_cry="", durability=100, effect={"damage": 100}),
            "Sillage d’Encens": Attack(name="Sillage d’Encens", description="Une série de mouvements fluides libérant une fumée toxique qui entrave les adversaires.", battle_cry="", durability=100, effect={"damage": 100}),
            "Colère des 1000 Âmes": Attack(name="Colère des 1000 Âmes", description="Le boss invoque les esprits des moines qui l’entourent pour déchaîner une tempête spirituelle dévastatrice.", battle_cry="", durability=1, effect={"damage": 100}),
        }

        self.items = {
            "Clé du casino" : Item(name="Clé du casino", description="Cette clé t'aidera a acceder au boss final !", effect={}),
            "Clé de la fête foraine" : Item(name="Clé de la fête foraine", description="Cette clé t'aidera a acceder au boss final !", effect={}),
            "Clé du temple" : Item(name="Clé du temple", description="Cette clé t'aidera a acceder au boss final !", effect={}),
            "Clé du Domaine" : Item(name="Clé du casino", description="Cette clé t'aidera a acceder au boss final !", effect={}),
            "Petite potion rouge": Consomable(name="Petite potion rouge", description="Potion donné par la déesse Gaïa (soigne)", effect={"hp": 5}, durability=1)
        }

        self.artefact = {
            "Ecran du mac": Equipable(name="Ecran du Mac", description="Utilisé comme bouclier, c'est le fameu écran du Mac de Mathieu", effect={"defense": 10}),
            "Maxi Phô Boeuf": Equipable(name="Maxi Phô Boeuf", description="", effect={"damage": 10}),
            "Jeu de cartes": Equipable(name="Jeu de cartes", description="", effect={})
        }

        self.monsters = {
            "Amelie": Monster(name="Amelie", description="", level=2, stats={}, attack_list=[self.attacks["Amel 1"], self.attacks["Amel 2"]], dropable_items=[self.items["Petite potion rouge"]]),
            "Fara": Monster(name="Fara", description="", level=2, stats={}, attack_list=[self.attacks["Fara 1"], self.attacks["Fara 2"]], dropable_items=[self.items["Petite potion rouge"]]),
            "Imen": Monster(name="Imen", description="", level=2, stats={}, attack_list=[self.attacks["Control Mental"], self.attacks["Gear 5"]], dropable_items=[self.items["Petite potion rouge"]]),
            "Nazim": Monster(name="Nazim", description="", level=2, stats={}, attack_list=[self.attacks["Kamehameha"], self.attacks["Malaka"]], dropable_items=[self.items["Petite potion rouge"]]),
            "Nana la renarde": Monster(name="Nana la renarde", description="", level=2, stats={}, attack_list=[self.attacks["Charme"], self.attacks["Chant brutal"]], dropable_items=[self.items["Petite potion rouge"]]),
            "Youva": Monster(name="Youva", description="", level=2, stats={}, attack_list=[self.attacks["Explosion"], self.attacks["Vol rapide"]], dropable_items=[self.items["Petite potion rouge"]]),
            "Carglass": Monster(name="Carglass", description="", level=2, stats={}, attack_list=[self.attacks["Lancé de talon"], self.attacks["Griffure"]], dropable_items=[self.items["Petite potion rouge"]]),
            "Cherif": Monster(name="Cherif", description="", level=2, stats={}, attack_list=[self.attacks["Coup de tonerre"], self.attacks["Grattage du délégué"]], dropable_items=[self.items["Petite potion rouge"]]),
            "Noa": Monster(name="Noa", description="", level=2, stats={}, attack_list=[self.attacks["Souplesse du judoka"], self.attacks["Poing de feu"]], dropable_items=[self.items["Petite potion rouge"]]),
            "Hamid": Monster(name="Hamid", description="", level=2, stats={}, attack_list=[self.attacks["Bois de boulogne"], self.attacks["Course rapide"]], dropable_items=[self.items["Petite potion rouge"]]),
            "Kevin": Monster(name="Kevin", description="Souverain des rires perdus", level=1000, stats={}, attack_list=[self.attacks["Marteau du Forain"], self.attacks["Billes de Loterie Explosives"], self.attacks["Claque de la Poigne Gigantesque"]], dropable_items=[self.items["Clé de la fête foraine"]]),
            "Anjaro": Monster(name="Anjaro", description="Fils du Roi Singe", level=1000, stats={}, attack_list=[self.attacks["Le Lasso de Soie"], self.attacks["La Roulade du Gentleman"], self.attacks["Le Vent du Chapeau"], self.attacks["Le Crâne de Lumière"]], dropable_items=[]),
            "Mathieu": Monster(name="Mathieu", description="Riche investisseur", level=1000, stats={}, attack_list=[self.attacks["Le Marteau de la Banque"], self.attacks["Le Lancer de Pièce Fétiche"], self.attacks["Le Coup du Pantalon Traître"], self.attacks["L’Écran Noir de la Dette"]], dropable_items=[self.items["Clé du Domaine"]]),
            "Le Roi Singe": Monster(name="Le Roi Singe", description="Dirigeant de la confrérie singeresque", level=1000, stats={}, attack_list=[self.attacks["Low Kick du Kangourou"], self.attacks["Bouclier du lémurien"], self.attacks["Déferlante de la jungle"]], dropable_items=[self.items["Clé du casino"]]),
            "Lao-ren": Monster(name="Lao-ren", description="Maître Shaolin", level=1000, stats={}, attack_list=[self.attacks["Coup du Lotus Brisé"], self.attacks["Sillage d’Encens"], self.attacks["Colère des 1000 Âmes"]], dropable_items=[self.items["Clé du temple"]]),

        }

    def start(self):
        console.print(f"[bold blue]Bienvenue dans {self.name}[/bold blue]")
        choice = Prompt.ask(
            "Faites un choix :\n0 - Créer un monde\n1 - Charger un monde\n",
            choices=["0", "1"]
        )

        system("clear")

        if choice == "0":
            console.print("[green]Création du personnage...[/green]")
            player_name = Prompt.ask("Quel nom souhaitez-vous donner à votre personnage ?")
            system("clear")
            self.main_player = Player(
                name=player_name,
                level=1,
                xp=0,
                stats={"health": 100, "attack": 10, "defense": 5},
                attack_list=[],
                place= self.places["Spawn"]
            )

            self.main_player.place.interact()



    def save(self):
        pass

    def load(self):
        pass


class Entity:
    def __init__(self, name: str, description: str, level: int, xp: float, stats: dict, attack_list: list):
        self.name = name
        self.description = description
        self.level = level
        self.xp = xp
        self.stats = stats or {}
        self.max_hp = stats["health"]
        self.attack_list = attack_list or []
        self.status = []


    def attack(self, target: 'Entity') -> None:
        """Effectue une attaque sur la cible"""
        pass

    def take_damage(self, amount: int, damage_type: str) -> None:
        """Reçoit des dégâts d'un certain type"""
        pass

class Pnj(Entity):
    def __init__(self, dialog: list):
        self.dialog = dialog

    def interact(self):
        pass

class Monster(Entity):
    def __init__(self, name: str, description: str, level: int, stats: dict, attack_list: list, dropable_items: list):
        super().__init__(name, description, level, 0, stats, attack_list)
        self.dropable_items = dropable_items

    def calculate_drops(self):
        pass

class Place:
    def __init__(self, name: str, description: str, monsters: list, interaction, places_around=None):
        self.name = name
        self.description = description
        self.places_around = places_around or {}
        self.monsters = monsters
        self.exploration = False
        self.interaction = interaction

    def interact(self):
        self.interaction(self)

class Player(Entity):
    def __init__(self, name: str, level: int, xp: float, stats: dict, attack_list: list, place: Place ):
        super().__init__(name, "", level, xp, stats, attack_list)
        self.inventory = []
        self.place = place

    def show_inventory(self):
        pass

    def use_item(self):
        pass

    def move(self, place):
        pass

    def add_xp(self):
        pass

class Combat:
    def __init__(self, player: Player, target: Monster):
        self.turn = 1
        self.player = player
        self.target = target
        self.is_active = True

    def start(self) -> None:
        """Démarre le combat"""
        console.print(f"[red]Combat contre {self.target.name} commencé ![/red]")

    def process_turn(self) -> None:
        """Gère un tour de combat"""
        pass

    def end(self):
        pass

    def escape(self):
        pass

class Item:
    def __init__(self, name: str, description: str, effect: dict):
        self.name = name
        self.descritpion = description
        self.effect = effect
        effect = {
            "health": 10
        }
        effect = {
            "attack": 10,
            "defense": 10
        }

class Equipable(Item):
    def __init__(self, name: str, description: str, effect: dict):
        super().__init__(name, description, effect)
        self.equiped = False



class Consomable(Item):
    def __init__(self, name: str, description: str, effect: dict, durability: int):
        super().__init__(name, description, effect)
        self.active = False
        self.durability = durability

    def use(self, target):
        if "health" in self.effect and target.max_health > target.stats["health"]:
               if self.effect["health"] < target.max_health - target.stats["health"] :
                   target.stats["health"] += self.effect["health"]
               else :
                   target.stats["health"] = target.max_health
        elif "attack" in self.effect:
            target.stats["attack"] += self.effect["attack"]
        else :
            target.stats["defense"] += self.effect["defense"]






class Attack:
    def __init__(self, name: str, description: str, battle_cry: str, durability: int, effect: dict):
        self.name = name
        self.description = description
        self.battle_cry = battle_cry
        self.durability = durability
        self.effect = effect

class Dialog:
    def dialog(self, dialog: list):
        for speaker, text in dialog:
            if speaker == "-":
                self.naration(text)
            else:
                self.talk(speaker, text)

    def place_changement(self, new_place: str):
        system("clear")
        Prompt.ask(f"[bold][green]Vous changez d'endroit...\nBienvenue dans [underline]{new_place}[/underline][/green][/bold]")

    def talk(self, speaker:str, text: str):
        system("clear")
        Prompt.ask(f"[blue]{speaker} >[/blue] {text}\n\nAppuyez sur enter pour continuer..")

    def naration(self, text):
        system("clear")
        Prompt.ask(f"[yellow]VOIX OFF >[/yellow] {text}\n\nAppuyez sur enter pour continuer..")


if __name__ == "__main__":
    dialog = Dialog()
    game = Game("Mon RPG")

    game.start()
