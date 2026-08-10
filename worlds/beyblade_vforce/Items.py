from typing import NamedTuple, Optional, Any

from BaseClasses import Item, ItemClassification as IC

from .Constants.Names import item_names as ItemName
from .Constants.world_constants import GAME_NAME

class  BVFUBJItemData(NamedTuple):
    item_groups: list[str]
    classification: IC
    other_variable: Optional[int] = None


class  BVFUBJItem(Item):
    game: str = GAME_NAME
    data:  BVFUBJItemData

    def __init__(self, name: str, classification: IC, code: Optional[int], player: int):
        super( BVFUBJItem, self).__init__(name, classification, code, player)
        self.data = all_items_table[name]
        self.code = ITEM_NAME_TO_ID["item"] if "item" in ITEM_NAME_TO_ID else None

base_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.ULTIMATE_DRAGOON: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.ULTIMATE_SAIZO: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.ULTIMATE_FROSTIC_DRANZER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.GEKIRYU_OH: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.MEGARO_ARM: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.SPARK_KNIGHT: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.POLTA: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.PISTOL: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.MAKENDO: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.BAKUSHIN_OH: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.BUMP_KING: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.GRIP_ATTACKER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.BEARING_STINGER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.BOUND_ATTACKER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.BOUND_DEFENDER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.ROLLER_ATTACKER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.ROLLER_DEFENSER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.AUTO_CHANGE_BALANCER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.WING_ATTACKER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.WING_DEFENSER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRACIEL_METAL: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRAGOON_STORM: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRIGER_S: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DEATH_DRIGER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.KNIGHT_DRANZER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.METAL_DRACIEL: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.KID_DRAGOON: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRAGOON_S: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRANZER_S: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.GALEON_ATTACKER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.GALZZLY: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.GALMAN: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.WOLBORG: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.SEABORG: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRACIEL_S: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.TRYGLE: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.TRYPIO: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRIGER_F: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRAGOON_FIGHTER: BVFUBJItemData(["Beyblade Collectiblesr"], IC.filler),
    ItemName.DRANZER_F: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.GRIFFOLYON: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.MASTER_DRAGOON: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.MASTER_DRANZER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.MASTER_DRACIEL: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRACIEL_F: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.WYBORG: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.MASTER_DRIGER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.WOLBORG_2: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRAGOON_V: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.METAL_DRANZER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.FLASH_LEOPARD: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRIGER_V: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRANZER_V: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.CYBER_DRAGOON: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.DRACIEL_V: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.HAYATE_HIDDEN_SPIRIT: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.ZINRAI_HIDDEN_SPIRIT: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.CYBER_DRANZER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.CYBER_DRACIEL: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.CYBER_DRIGER: BVFUBJItemData(["Beyblade Collectibles"], IC.filler),
    ItemName.FOX_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.SPIDER_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.SICKLE_WEASEL_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.TYRANNO_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.CLARKEN_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.DRAGOON_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.DRANZER_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.DRACIEL_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.DRIGER_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.CEREBERUS_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.ORTHRUS_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.GABRIEL_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.ARIEL_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.CYBER_DRAGOON_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.CYBER_DRIGER_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.CYBER_DRANZER_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.CYBER_DRACIEL_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.FLASH_LEOPARD_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.VORTEX_APE_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.SHARKRASH_ICON: BVFUBJItemData(["Bit Beast Icon"], IC.filler),
    ItemName.VANISHING_MOOT_ICON: BVFUBJItemData(["Beagr45tybklligtruekjhbnaerfs"], IC.filler)
}

filler_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.STAMINA_REFILL: BVFUBJItemData(["Stamina Refill"], IC.filler)
}

upgrade_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.BOOST_UPGRADE: BVFUBJItemData(["Boost Upgrade"], IC.progression),
    ItemName.BRAKE_UPGRADE: BVFUBJItemData(["Brake Upgrade"], IC.progression),
    ItemName.ULTIMATE_UPGRADE: BVFUBJItemData(["Ultimate Upgrade"], IC.useful)
}

pad_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.JUMP_PAD_UNLOCK: BVFUBJItemData(["Jump Pad"], IC.progression),
    ItemName.BOOST_PAD_UNLOCK: BVFUBJItemData(["Boost Pad"], IC.progression),
    ItemName.RECHARGE_PAD_UNLOCK: BVFUBJItemData(["Recharge Pad"], IC.progression)
}

stamina_upgrade_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.PROGRESSIVE_STAMINA_UPGRADE: BVFUBJItemData(["Progressive Stamina Upgrade"], IC.progression)
}

round_unlock_item_table: dict[str,  BVFUBJItemData] = {
    ItemName.E1R1_UNLOCK: BVFUBJItemData(["Episode 1 Round 1 Unlock"], IC.progression),
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
    ItemName.BAT: BVFUBJItemData(["Bat"], IC.filler),
    ItemName.BUS_DRIVER: BVFUBJItemData(["Bus Driver"], IC.filler),
    ItemName.CHAMELEON: BVFUBJItemData(["Chameleon"], IC.filler),
    ItemName.DARYL: BVFUBJItemData(["Daryl"], IC.filler),
    ItemName.DIZZI: BVFUBJItemData(["Dizzi"], IC.filler),
    ItemName.DOCTOR_B: BVFUBJItemData(["Doctor B"], IC.filler),
    ItemName.FUNGA: BVFUBJItemData(["Funga"], IC.filler),
    ItemName.FIGEL: BVFUBJItemData(["Figel"], IC.filler),
    ItemName.GOKI: BVFUBJItemData(["Goki"], IC.filler),
    ItemName.GERRY: BVFUBJItemData(["Gerry"], IC.filler),
    ItemName.GRANDPA: BVFUBJItemData(["Grandpa"], IC.filler),
    ItemName.GIDEON: BVFUBJItemData(["Gideon"], IC.filler),
    ItemName.HILARY: BVFUBJItemData(["Hilary"], IC.filler),
    ItemName.JIM: BVFUBJItemData(["Jim"], IC.filler),
    ItemName.JOSEPH: BVFUBJItemData(["Joseph"], IC.filler),
    ItemName.KANE: BVFUBJItemData(["Kane"], IC.filler),
    ItemName.KAI: BVFUBJItemData(["Kai"], IC.filler),
    ItemName.KENNY: BVFUBJItemData(["Kenny"], IC.filler),
    ItemName.MARIAM: BVFUBJItemData(["Mariam"], IC.filler),
    ItemName.MAX: BVFUBJItemData(["Max"], IC.filler),
    ItemName.MEN_IN_BLACK: BVFUBJItemData(["Men in Black"], IC.filler),
    ItemName.MR_DICKINSON: BVFUBJItemData(["Mr. Dickinson"], IC.filler),
    ItemName.OZUMA: BVFUBJItemData(["Ozuma/Mister X"], IC.filler),
    ItemName.RAY: BVFUBJItemData(["Ray"], IC.filler),
    ItemName.SALIMA: BVFUBJItemData(["Salima"], IC.filler),
    ItemName.SNAKEY: BVFUBJItemData(["Snakey"], IC.filler),
    ItemName.THE_ROBOT: BVFUBJItemData(["The Robot"], IC.filler),
    ItemName.TYSON: BVFUBJItemData(["Tyson"], IC.filler)
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