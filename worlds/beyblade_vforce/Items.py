from typing import NamedTuple, Optional

from BaseClasses import Item, ItemClassification as IC

from .Constants.Names import item_names as ItemName
from .Constants.world_constants import GAME_NAME
from .Helpers_Function import RamData


class  BVFUBJItemData(NamedTuple):
    item_groups: list[str]
    classification: IC
    ram_data: RamData = None


class  BVFUBJItem(Item):
    game: str = GAME_NAME
    data:  BVFUBJItemData

    def __init__(self, name: str, classification: IC, code: Optional[int], player: int):
        super( BVFUBJItem, self).__init__(name, classification, code, player)
        self.data = all_items_table[name]
        self.code = ITEM_NAME_TO_ID["item"] if "item" in ITEM_NAME_TO_ID else None

base_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.ULTIMATE_DRAGOON: BVFUBJItemData(["BeyBlade Collectibles"], IC.filler),
    ItemName.ULTIMATE_SAIZO: BVFUBJItemData(["Ultimate Saizo"], IC.filler),
    ItemName.ULTIMATE_FROSTIC_DRANZER: BVFUBJItemData(["Ultimate Frostic Dranzer"], IC.filler),
    ItemName.GEKIRYU_OH: BVFUBJItemData(["Gekiryu-oh"], IC.filler),
    ItemName.MEGARO_ARM: BVFUBJItemData(["Megaro Arm"], IC.filler),
    ItemName.SPARK_KNIGHT: BVFUBJItemData(["Spark Knight"], IC.filler),
    ItemName.POLTA: BVFUBJItemData(["Polta"], IC.filler),
    ItemName.PISTOL: BVFUBJItemData(["Pistol"], IC.filler),
    ItemName.MAKENDO: BVFUBJItemData(["Makendo"], IC.filler),
    ItemName.BAKUSHIN_OH: BVFUBJItemData(["Bakushin-oh"], IC.filler),
    ItemName.BUMP_KING: BVFUBJItemData(["Bump King"], IC.filler),
    ItemName.GRIP_ATTACKER: BVFUBJItemData(["Grip Attacker"], IC.filler),
    ItemName.BEARING_STINGER: BVFUBJItemData(["Bearing Stinger"], IC.filler),
    ItemName.BOUND_ATTACKER: BVFUBJItemData(["Bound Attacker"], IC.filler),
    ItemName.BOUND_DEFENDER: BVFUBJItemData(["Bound Defender"], IC.filler),
    ItemName.ROLLER_ATTACKER: BVFUBJItemData(["Roller Attacker"], IC.filler),
    ItemName.ROLLER_DEFENSER: BVFUBJItemData(["Roller Defenser"], IC.filler),
    ItemName.AUTO_CHANGE_BALANCER: BVFUBJItemData(["Auto Change Balancer"], IC.filler),
    ItemName.WING_ATTACKER: BVFUBJItemData(["Wing Attacker"], IC.filler),
    ItemName.WING_DEFENSER: BVFUBJItemData(["Gekiryu-oh"], IC.filler),
    ItemName.DRACIEL_METAL: BVFUBJItemData(["Draciel Metal"], IC.filler),
    ItemName.DRAGOON_STORM: BVFUBJItemData(["Dragoon Storm"], IC.filler),
    ItemName.DRIGER_S: BVFUBJItemData(["Driger S"], IC.filler),
    ItemName.DEATH_DRIGER: BVFUBJItemData(["Death Driger"], IC.filler),
    ItemName.KNIGHT_DRANZER: BVFUBJItemData(["Knight Dranzer"], IC.filler),
    ItemName.METAL_DRACIEL: BVFUBJItemData(["Metal Draciel"], IC.filler),
    ItemName.KID_DRAGOON: BVFUBJItemData(["King Dragoon"], IC.filler),
    ItemName.DRAGOON_S: BVFUBJItemData(["Dragoon S"], IC.filler),
    ItemName.DRANZER_S: BVFUBJItemData(["Dranzer S"], IC.filler),
    ItemName.GALEON_ATTACKER: BVFUBJItemData(["Galeon Attacker"], IC.filler),
    ItemName.GALZZLY: BVFUBJItemData(["Galzzly"], IC.filler),
    ItemName.GALMAN: BVFUBJItemData(["Galman"], IC.filler),
    ItemName.WOLBORG: BVFUBJItemData(["Wolborg"], IC.filler),
    ItemName.SEABORG: BVFUBJItemData(["Seaborg"], IC.filler),
    ItemName.DRACIEL_S: BVFUBJItemData(["Draciel S"], IC.filler),
    ItemName.TRYGLE: BVFUBJItemData(["Trygle"], IC.filler),
    ItemName.TRYPIO: BVFUBJItemData(["Trypio"], IC.filler),
    ItemName.DRIGER_F: BVFUBJItemData(["Driger F"], IC.filler),
    ItemName.DRAGOON_FIGHTER: BVFUBJItemData(["Dragoon Fighter"], IC.filler),
    ItemName.DRANZER_F: BVFUBJItemData(["Dranzer F"], IC.filler),
    ItemName.GRIFFOLYON: BVFUBJItemData(["Griffolyon"], IC.filler),
    ItemName.MASTER_DRAGOON: BVFUBJItemData(["Master Dragoon"], IC.filler),
    ItemName.MASTER_DRANZER: BVFUBJItemData(["Master Dranzer"], IC.filler),
    ItemName.MASTER_DRACIEL: BVFUBJItemData(["Master Draciel"], IC.filler),
    ItemName.DRACIEL_F: BVFUBJItemData(["Draciel F"], IC.filler),
    ItemName.WYBORG: BVFUBJItemData(["Wyborg"], IC.filler),
    ItemName.MASTER_DRIGER: BVFUBJItemData(["Master Driger"], IC.filler),
    ItemName.WOLBORG_2: BVFUBJItemData(["Wolborg 2"], IC.filler),
    ItemName.DRAGOON_V: BVFUBJItemData(["Dragoon V"], IC.filler),
    ItemName.METAL_DRANZER: BVFUBJItemData(["Metal Dranzer"], IC.filler),
    ItemName.FLASH_LEOPARD: BVFUBJItemData(["Flash Leopard"], IC.filler),
    ItemName.DRIGER_V: BVFUBJItemData(["Driger V"], IC.filler),
    ItemName.DRANZER_V: BVFUBJItemData(["Dranzer V"], IC.filler),
    ItemName.CYBER_DRAGOON: BVFUBJItemData(["Cyber Dragoon"], IC.filler),
    ItemName.DRACIEL_V: BVFUBJItemData(["Draciel V"], IC.filler),
    ItemName.HAYATE_HIDDEN_SPIRIT: BVFUBJItemData(["Hayate Hidden Spirit"], IC.filler),
    ItemName.ZINRAI_HIDDEN_SPIRIT: BVFUBJItemData(["Zinrai Hidden Spirit"], IC.filler),
    ItemName.CYBER_DRANZER: BVFUBJItemData(["Cyber Dranzer"], IC.filler),
    ItemName.CYBER_DRACIEL: BVFUBJItemData(["Cyber Draciel"], IC.filler),
    ItemName.CYBER_DRIGER: BVFUBJItemData(["Cyber Driger"], IC.filler),
    ItemName.FOX_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.SPIDER_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.SICKLE_WEASEL_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.TYRANNO_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.CLARKEN_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.DRAGOON_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.DRANZER_ICON: BVFUBJItemData(["Dranzer Icon"], IC.filler),
    ItemName.DRACIEL_ICON: BVFUBJItemData(["Draciel Icon"], IC.filler),
    ItemName.DRIGER_ICON: BVFUBJItemData(["Driger Icon"], IC.filler),
    ItemName.CEREBERUS_ICON: BVFUBJItemData(["Cereberus Icon"], IC.filler),
    ItemName.ORTHRUS_ICON: BVFUBJItemData(["Orthrus Icon"], IC.filler),
    ItemName.GABRIEL_ICON: BVFUBJItemData(["Gabriel Icon"], IC.filler),
    ItemName.ARIEL_ICON: BVFUBJItemData(["Ariel_Icon"], IC.filler),
    ItemName.CYBER_DRAGOON_ICON: BVFUBJItemData(["Cyber Dragoon Icon"], IC.filler),
    ItemName.CYBER_DRIGER_ICON: BVFUBJItemData(["Cyber Driger Icon"], IC.filler),
    ItemName.CYBER_DRANZER_ICON: BVFUBJItemData(["Cyber Dranzer Icon"], IC.filler),
    ItemName.CYBER_DRACIEL_ICON: BVFUBJItemData(["Cyber Draciel Icon"], IC.filler),
    ItemName.FLASH_LEOPARD_ICON: BVFUBJItemData(["Flash Leopard Icon"], IC.filler),
    ItemName.VORTEX_APE_ICON: BVFUBJItemData(["Vortex Ape Icon"], IC.filler),
    ItemName.SHARKRASH_ICON: BVFUBJItemData(["Sharkrash Icon"], IC.filler),
    ItemName.VANISHING_MOOT_ICON: BVFUBJItemData(["Vanishing Moot Icon"], IC.filler)
}

filler_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.STAMINA_REFILL: BVFUBJItemData(["Stamina Refills"], IC.filler)
}

upgrade_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.BOOST_UPGRADE: BVFUBJItemData(["Upgrade"], IC.progression),
    ItemName.BRAKE_UPGRADE: BVFUBJItemData(["Upgrade"], IC.progression),
    ItemName.ULTIMATE_UPGRADE: BVFUBJItemData(["Upgrade"], IC.useful)
}

pad_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.JUMP_PAD_UNLOCK: BVFUBJItemData(["Pad Items"], IC.progression),
    ItemName.BOOST_PAD_UNLOCK: BVFUBJItemData(["Pad Items"], IC.progression),
    ItemName.RECHARGE_PAD_UNLOCK: BVFUBJItemData(["Pad Items"], IC.progression)
}

stamina_upgrade_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.PROGRESSIVE_STAMINA_UPGRADE: BVFUBJItemData(["Progressive Stamina Upgrades"], IC.progression)
}

round_unlock_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.E1R1_UNLOCK: BVFUBJItemData(["Round Keys"], IC.progression),
    ItemName.E1R2_UNLOCK: BVFUBJItemData(["Episode 1 Round 2 Unlock"], IC.progression),
    ItemName.E1R3_UNLOCK: BVFUBJItemData(["Episode 1 3Round 3 Unlock"], IC.progression),
    ItemName.E1R4_UNLOCK: BVFUBJItemData(["Episode 1 Round 4 Unlock"], IC.progression),
    ItemName.E1R5_UNLOCK: BVFUBJItemData(["Episode 1 Round 5 Unlock"], IC.progression),
    ItemName.E1R6_UNLOCK: BVFUBJItemData(["Episode 1 Round 6 Unlock"], IC.progression),
    ItemName.E1R7_UNLOCK: BVFUBJItemData(["Episode 1 Round 7 Unlock"], IC.progression),
    ItemName.E1RB_UNLOCK: BVFUBJItemData(["Episode 1 Bonus Round Unlock"], IC.progression),
    ItemName.E2R1_UNLOCK: BVFUBJItemData(["Episode 2 Round 1 Unlock"], IC.progression),
    ItemName.E2R2_UNLOCK: BVFUBJItemData(["Episode 2 Round 2 Unlock"], IC.progression),
    ItemName.E2R3_UNLOCK: BVFUBJItemData(["Episode 2 Round 3 Unlock"], IC.progression),
    ItemName.E2R4_UNLOCK: BVFUBJItemData(["Episode 2 Round 4 Unlock"], IC.progression),
    ItemName.E2R5_UNLOCK: BVFUBJItemData(["Episode 2 Round 5 Unlock"], IC.progression),
    ItemName.E2R6_UNLOCK: BVFUBJItemData(["Episode 2 Round 6 Unlock"], IC.progression),
    ItemName.E2R7_UNLOCK: BVFUBJItemData(["Episode 2 Round 7 Unlock"], IC.progression),
    ItemName.E2RB_UNLOCK: BVFUBJItemData(["Episode 2 Bonus Round Unlock"], IC.progression),
    ItemName.E3R1_UNLOCK: BVFUBJItemData(["Episode 3 Round 1 Unlock"], IC.progression),
    ItemName.E3R2_UNLOCK: BVFUBJItemData(["Episode 3 Round 2 Unlock"], IC.progression),
    ItemName.E3R3_UNLOCK: BVFUBJItemData(["Episode 3 Round 3 Unlock"], IC.progression),
    ItemName.E3R4_UNLOCK: BVFUBJItemData(["Episode 3 Round 4 Unlock"], IC.progression),
    ItemName.E3R5_UNLOCK: BVFUBJItemData(["Episode 3 Round 5 Unlock"], IC.progression),
    ItemName.E3R6_UNLOCK: BVFUBJItemData(["Episode 3 Round 6 Unlock"], IC.progression),
    ItemName.E3R7_UNLOCK: BVFUBJItemData(["Episode 3 Round 7 Unlock"], IC.progression),
    ItemName.E3RB_UNLOCK: BVFUBJItemData(["Episode 3 Bonus Round Unlock"], IC.progression),
    ItemName.E4R1_UNLOCK: BVFUBJItemData(["Episode 4 Round 1 Unlock"], IC.progression),
    ItemName.E4R2_UNLOCK: BVFUBJItemData(["Episode 4 Round 2 Unlock"], IC.progression),
    ItemName.E4R3_UNLOCK: BVFUBJItemData(["Episode 4 Round 3 Unlock"], IC.progression),
    ItemName.E4R4_UNLOCK: BVFUBJItemData(["Episode 4 Round 4 Unlock"], IC.progression),
    ItemName.E4R5_UNLOCK: BVFUBJItemData(["Episode 4 Round 5 Unlock"], IC.progression),
    ItemName.E4R6_UNLOCK: BVFUBJItemData(["Episode 4 Round 6 Unlock"], IC.progression),
    ItemName.E4R7_UNLOCK: BVFUBJItemData(["Episode 4 Round 7 Unlock"], IC.progression),
    ItemName.E4RB_UNLOCK: BVFUBJItemData(["Episode 4 Bonus Round Unlock"], IC.progression),
    ItemName.E5R1_UNLOCK: BVFUBJItemData(["Episode 5 Round 1 Unlock"], IC.progression),
    ItemName.E5R2_UNLOCK: BVFUBJItemData(["Episode 5 Round 2 Unlock"], IC.progression),
    ItemName.E5R3_UNLOCK: BVFUBJItemData(["Episode 5 Round 3 Unlock"], IC.progression),
    ItemName.E5R4_UNLOCK: BVFUBJItemData(["Episode 5 Round 4 Unlock"], IC.progression),
    ItemName.E5R5_UNLOCK: BVFUBJItemData(["Episode 5 Round 5 Unlock"], IC.progression),
    ItemName.E5R6_UNLOCK: BVFUBJItemData(["Episode 5 Round 6 Unlock"], IC.progression),
    ItemName.E5R7_UNLOCK: BVFUBJItemData(["Episode 5 Round 7 Unlock"], IC.progression),
    ItemName.E5RB_UNLOCK: BVFUBJItemData(["Episode 5 Bonus Round Unlock"], IC.progression),
    ItemName.E6R1_UNLOCK: BVFUBJItemData(["Episode 6 Round 1 Unlock"], IC.progression),
    ItemName.E6R2_UNLOCK: BVFUBJItemData(["Episode 6 Round 2 Unlock"], IC.progression),
    ItemName.E6R3_UNLOCK: BVFUBJItemData(["Episode 6 Round 3 Unlock"], IC.progression),
    ItemName.E6R4_UNLOCK: BVFUBJItemData(["Episode 6 Round 4 Unlock"], IC.progression),
    ItemName.E6R5_UNLOCK: BVFUBJItemData(["Episode 6 Round 5 Unlock"], IC.progression),
    ItemName.E6R6_UNLOCK: BVFUBJItemData(["Episode 6 Round 6 Unlock"], IC.progression),
    ItemName.E6R7_UNLOCK: BVFUBJItemData(["Episode 6 Round 7 Unlock"], IC.progression),
    ItemName.E6RB_UNLOCK: BVFUBJItemData(["Episode 6 Bonus Round Unlock"], IC.progression),
    ItemName.E7R1_UNLOCK: BVFUBJItemData(["Episode 7 Round 1 Unlock"], IC.progression),
    ItemName.E7R2_UNLOCK: BVFUBJItemData(["Episode 7 Round 2 Unlock"], IC.progression),
    ItemName.E7R3_UNLOCK: BVFUBJItemData(["Episode 7 Round 3 Unlock"], IC.progression),
    ItemName.E7R4_UNLOCK: BVFUBJItemData(["Episode 7 Round 4 Unlock"], IC.progression),
    ItemName.E7R5_UNLOCK: BVFUBJItemData(["Episode 7 Round 5 Unlock"], IC.progression),
    ItemName.E7R6_UNLOCK: BVFUBJItemData(["Episode 7 Round 6 Unlock"], IC.progression),
    ItemName.E7R7_UNLOCK: BVFUBJItemData(["Episode 7 Round 7 Unlock"], IC.progression),
    ItemName.E7RB_UNLOCK: BVFUBJItemData(["Episode 7 Bonus Round Unlock"], IC.progression),
}

progressive_round_unlock_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.PROGRESSIVE_ROUND_UNLOCK: BVFUBJItemData(["Progressive Round Unlock"], IC.progression)
}

character_unlock_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.BAT: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.BUS_DRIVER: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.CHAMELEON: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.DARYL: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.DIZZI: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.DOCTOR_B: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.FUNGA: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.FIGEL: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.GOKI: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.GERRY: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.GRANDPA: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.GIDEON: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.HILARY: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.JIM: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.JOSEPH: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.KANE: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.KAI: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.KENNY: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.MARIAM: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.MAX: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.MEN_IN_BLACK: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.MR_DICKINSON: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.OZUMA: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.RAY: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.SALIMA: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.SNAKEY: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.THE_ROBOT: BVFUBJItemData(["Characters"], IC.filler),
    ItemName.TYSON: BVFUBJItemData(["Characters"], IC.filler)
}

all_items_table: dict[str, BVFUBJItemData] = {**base_item_table, **filler_item_table, **upgrade_item_table, **pad_item_table, **stamina_upgrade_item_table, **round_unlock_item_table, **progressive_round_unlock_item_table, **character_unlock_item_table}

def get_items_name_to_id() -> dict[str, int]:
    dict_locs: dict[str, int] = {}
    for name, data in all_items_table.items():
        dict_locs.update({name: len(dict_locs) + 1})
    return dict_locs

def get_item_names_per_category() -> dict[str, set[str]]:
    categories: dict[str, set[str]] = {}

    for name, data in all_items_table.items():
        for category in data.item_groups:
            categories.setdefault(category, set()).add(name)

    return categories

ITEM_NAME_TO_ID: dict[str, int] = get_items_name_to_id()