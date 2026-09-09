from typing import Optional, NamedTuple, Any, TYPE_CHECKING

from BaseClasses import Location, Region
from rule_builder.rules import Rule, True_

from . import Helpers_Function
from .Constants.Names import location_names as LocationName, region_names as RegionName
from .Constants.world_constants import GAME_NAME
from .Items import BVFUBJItem

if TYPE_CHECKING:
    from .world import BVFUBJWorld

class BVFUBJOptionData(NamedTuple):
    option_list: dict[str, list[Any]]
    combine: bool = True

class  BVFUBJLocationData(NamedTuple):
    region: str
    location_groups: list[str]  # one or more groups that this location belongs to
    access: Optional[Rule[Any]] = None
    req_options: Optional[BVFUBJOptionData] = None
    ram_data: Optional[Helpers_Function.RamData] = None


class  BVFUBJLocation(Location):
    game: str = GAME_NAME
    data: BVFUBJLocationData

    def __init__(self, player: int, name: str, address: Optional[int], parent: Optional[Region]):
        super(BVFUBJLocation, self).__init__(player, name, address, parent)
        self.data = all_location_table[name]
        self.address = LOCATION_NAME_TO_ID["item"] if "item" in LOCATION_NAME_TO_ID else None


base_location_table: dict[str, BVFUBJLocationData] = {
    LocationName.E1R1_COMPLETION: BVFUBJLocationData(RegionName.E1R1, ["Round Completion"]),
    LocationName.E1R2_COMPLETION: BVFUBJLocationData(RegionName.E1R2, ["Round Completion"]),
    LocationName.E1R3_COMPLETION: BVFUBJLocationData(RegionName.E1R3, ["Round Completion"]),
    LocationName.E1R4_COMPLETION: BVFUBJLocationData(RegionName.E1R4, ["Round Completion"]),
    LocationName.E1R5_COMPLETION: BVFUBJLocationData(RegionName.E1R5, ["Round Completion"]),
    LocationName.E1R6_COMPLETION: BVFUBJLocationData(RegionName.E1R6, ["Round Completion"]),
    LocationName.E1R7_COMPLETION: BVFUBJLocationData(RegionName.E1R7, ["Round Completion"]),
    LocationName.E1RB_COMPLETION: BVFUBJLocationData(RegionName.E1RB, ["Round Completion"]),
    LocationName.E2R1_COMPLETION: BVFUBJLocationData(RegionName.E2R1, ["Round Completion"]),
    LocationName.E2R2_COMPLETION: BVFUBJLocationData(RegionName.E2R2, ["Round Completion"]),
    LocationName.E2R3_COMPLETION: BVFUBJLocationData(RegionName.E2R3, ["Round Completion"]),
    LocationName.E2R4_COMPLETION: BVFUBJLocationData(RegionName.E2R4, ["Round Completion"]),
    LocationName.E2R5_COMPLETION: BVFUBJLocationData(RegionName.E2R5, ["Round Completion"]),
    LocationName.E2R6_COMPLETION: BVFUBJLocationData(RegionName.E2R6, ["Round Completion"]),
    LocationName.E2R7_COMPLETION: BVFUBJLocationData(RegionName.E2R7, ["Round Completion"]),
    LocationName.E2RB_COMPLETION: BVFUBJLocationData(RegionName.E2RB, ["Round Completion"]),
    LocationName.E3R1_COMPLETION: BVFUBJLocationData(RegionName.E3R1, ["Round Completion"]),
    LocationName.E3R2_COMPLETION: BVFUBJLocationData(RegionName.E3R2, ["Round Completion"]),
    LocationName.E3R3_COMPLETION: BVFUBJLocationData(RegionName.E3R3, ["Round Completion"]),
    LocationName.E3R4_COMPLETION: BVFUBJLocationData(RegionName.E3R4, ["Round Completion"]),
    LocationName.E3R5_COMPLETION: BVFUBJLocationData(RegionName.E3R5, ["Round Completion"]),
    LocationName.E3R6_COMPLETION: BVFUBJLocationData(RegionName.E3R6, ["Round Completion"]),
    LocationName.E3R7_COMPLETION: BVFUBJLocationData(RegionName.E3R7, ["Round Completion"]),
    LocationName.E3RB_COMPLETION: BVFUBJLocationData(RegionName.E3RB, ["Round Completion"]),
    LocationName.E4R1_COMPLETION: BVFUBJLocationData(RegionName.E4R1, ["Round Completion"]),
    LocationName.E4R2_COMPLETION: BVFUBJLocationData(RegionName.E4R2, ["Round Completion"]),
    LocationName.E4R3_COMPLETION: BVFUBJLocationData(RegionName.E4R3, ["Round Completion"]),
    LocationName.E4R4_COMPLETION: BVFUBJLocationData(RegionName.E4R4, ["Round Completion"]),
    LocationName.E4R5_COMPLETION: BVFUBJLocationData(RegionName.E4R5, ["Round Completion"]),
    LocationName.E4R6_COMPLETION: BVFUBJLocationData(RegionName.E4R6, ["Round Completion"]),
    LocationName.E4R7_COMPLETION: BVFUBJLocationData(RegionName.E4R7, ["Round Completion"]),
    LocationName.E4RB_COMPLETION: BVFUBJLocationData(RegionName.E4RB, ["Round Completion"]),
    LocationName.E5R1_COMPLETION: BVFUBJLocationData(RegionName.E5R1, ["Round Completion"]),
    LocationName.E5R2_COMPLETION: BVFUBJLocationData(RegionName.E5R2, ["Round Completion"]),
    LocationName.E5R3_COMPLETION: BVFUBJLocationData(RegionName.E5R3, ["Round Completion"]),
    LocationName.E5R4_COMPLETION: BVFUBJLocationData(RegionName.E5R4, ["Round Completion"]),
    LocationName.E5R5_COMPLETION: BVFUBJLocationData(RegionName.E5R5, ["Round Completion"]),
    LocationName.E5R6_COMPLETION: BVFUBJLocationData(RegionName.E5R6, ["Round Completion"]),
    LocationName.E5R7_COMPLETION: BVFUBJLocationData(RegionName.E5R7, ["Round Completion"]),
    LocationName.E5RB_COMPLETION: BVFUBJLocationData(RegionName.E5RB, ["Round Completion"]),
    LocationName.E6R1_COMPLETION: BVFUBJLocationData(RegionName.E6R1, ["Round Completion"]),
    LocationName.E6R2_COMPLETION: BVFUBJLocationData(RegionName.E6R2, ["Round Completion"]),
    LocationName.E6R3_COMPLETION: BVFUBJLocationData(RegionName.E6R3, ["Round Completion"]),
    LocationName.E6R4_COMPLETION: BVFUBJLocationData(RegionName.E6R4, ["Round Completion"]),
    LocationName.E6R5_COMPLETION: BVFUBJLocationData(RegionName.E6R5, ["Round Completion"]),
    LocationName.E6R6_COMPLETION: BVFUBJLocationData(RegionName.E6R6, ["Round Completion"]),
    LocationName.E6R7_COMPLETION: BVFUBJLocationData(RegionName.E6R7, ["Round Completion"]),
    LocationName.E6RB_COMPLETION: BVFUBJLocationData(RegionName.E6RB, ["Round Completion"]),
    LocationName.E7R1_COMPLETION: BVFUBJLocationData(RegionName.E7R1, ["Round Completion"]),
    LocationName.E7R2_COMPLETION: BVFUBJLocationData(RegionName.E7R2, ["Round Completion"]),
    LocationName.E7R3_COMPLETION: BVFUBJLocationData(RegionName.E7R3, ["Round Completion"]),
    LocationName.E7R4_COMPLETION: BVFUBJLocationData(RegionName.E7R4, ["Round Completion"]),
    LocationName.E7R5_COMPLETION: BVFUBJLocationData(RegionName.E7R5, ["Round Completion"]),
    LocationName.E7R6_COMPLETION: BVFUBJLocationData(RegionName.E7R6, ["Round Completion"]),
    LocationName.E7R7_COMPLETION: BVFUBJLocationData(RegionName.E7R7, ["Round Completion"]),
    LocationName.E7RB_COMPLETION: BVFUBJLocationData(RegionName.E7RB, ["Round Completion"]),
    LocationName.ULTIMATE_DRAGOON_CAN: BVFUBJLocationData(RegionName.E1R1, ["Beyblade Collectibles"]),
    LocationName.ULTIMATE_SAIZO_CAN: BVFUBJLocationData(RegionName.E2R2, ["Beyblade Collectibles"]),
    LocationName.ULTIMATE_FROSTIC_DRANZER_CAN: BVFUBJLocationData(RegionName.E7R4, ["Beyblade Collectibles"]),
    LocationName.GEKIRYU_OH_CAN: BVFUBJLocationData(RegionName.E6R2, ["Beyblade Collectibles"]),
    LocationName.MEGARO_ARM_CAN: BVFUBJLocationData(RegionName.E6R1, ["Beyblade Collectibles"]),
    LocationName.SPARK_KNIGHT_CAN: BVFUBJLocationData(RegionName.E1R2, ["Beyblade Collectibles"]),
    LocationName.POLTA_CAN: BVFUBJLocationData(RegionName.E4R5, ["Beyblade Collectibles"]),
    LocationName.PISTOL_CAN: BVFUBJLocationData(RegionName.E2R1, ["Beyblade Collectibles"]),
    LocationName.MAKENDO_CAN: BVFUBJLocationData(RegionName.E6R6, ["Beyblade Collectibles"]),
    LocationName.BAKUSHIN_OH_CAN: BVFUBJLocationData(RegionName.E5R2, ["Beyblade Collectibles"]),
    LocationName.BUMP_KING_CAN: BVFUBJLocationData(RegionName.E1R4, ["Beyblade Collectibles"]), #Unknown - enemy
    LocationName.GRIP_ATTACKER_CAN: BVFUBJLocationData(RegionName.E5R5, ["Beyblade Collectibles"]),
    LocationName.BEARING_STINGER_CAN: BVFUBJLocationData(RegionName.E6R3, ["Beyblade Collectibles"]),
    LocationName.BOUND_ATTACKER_CAN: BVFUBJLocationData(RegionName.E3R5, ["Beyblade Collectibles"]),
    LocationName.BOUND_DEFENDER_CAN: BVFUBJLocationData(RegionName.E6R1, ["Beyblade Collectibles"]),
    LocationName.ROLLER_ATTACKER_CAN: BVFUBJLocationData(RegionName.E6R2, ["Beyblade Collectibles"]),
    LocationName.ROLLER_DEFENSER_CAN: BVFUBJLocationData(RegionName.E6R1, ["Beyblade Collectibles"]), #Unknown - enemy
    LocationName.AUTO_CHANGE_BALANCER_CAN: BVFUBJLocationData(RegionName.E7R5, ["Beyblade Collectibles"]),
    LocationName.WING_ATTACKER_CAN: BVFUBJLocationData(RegionName.E6R5, ["Beyblade Collectibles"]),
    LocationName.WING_DEFENSER_CAN: BVFUBJLocationData(RegionName.E6R1, ["Beyblade Collectibles"]),
    LocationName.DRACIEL_METAL_CAN: BVFUBJLocationData(RegionName.E2R3, ["Beyblade Collectibles"]),
    LocationName.DRAGOON_STORM_CAN: BVFUBJLocationData(RegionName.E4R6, ["Beyblade Collectibles"]),
    LocationName.DRIGER_S_CAN: BVFUBJLocationData(RegionName.E4R6, ["Beyblade Collectibles"]),
    LocationName.DEATH_DRIGER_CAN: BVFUBJLocationData(RegionName.E4R2, ["Beyblade Collectibles"]),
    LocationName.KNIGHT_DRANZER_CAN: BVFUBJLocationData(RegionName.E7R2, ["Beyblade Collectibles"]),
    LocationName.METAL_DRACIEL_CAN: BVFUBJLocationData(RegionName.E3R1, ["Beyblade Collectibles"]),
    LocationName.KID_DRAGOON_CAN: BVFUBJLocationData(RegionName.E7R3, ["Beyblade Collectibles"]),
    LocationName.DRAGOON_S_CAN: BVFUBJLocationData(RegionName.E5RB, ["Beyblade Collectibles"]),
    LocationName.DRANZER_S_CAN: BVFUBJLocationData(RegionName.E5R6, ["Beyblade Collectibles"]),
    LocationName.GALEON_ATTACKER_CAN: BVFUBJLocationData(RegionName.E7R1, ["Beyblade Collectibles"]),
    LocationName.GALZZLY_CAN: BVFUBJLocationData(RegionName.E1R3, ["Beyblade Collectibles"]),
    LocationName.GALMAN_CAN: BVFUBJLocationData(RegionName.E7R2, ["Beyblade Collectibles"]),
    LocationName.WOLBORG_CAN: BVFUBJLocationData(RegionName.E6R6, ["Beyblade Collectibles"]),
    LocationName.SEABORG_CAN: BVFUBJLocationData(RegionName.E3R7, ["Beyblade Collectibles"]),
    LocationName.DRACIEL_S_CAN: BVFUBJLocationData(RegionName.MENU, ["Beyblade Collectibles"]),
    LocationName.TRYGLE_CAN: BVFUBJLocationData(RegionName.E4R1, ["Beyblade Collectibles"]),
    LocationName.TRYPIO_CAN: BVFUBJLocationData(RegionName.E3R2, ["Beyblade Collectibles"]),
    LocationName.DRIGER_F_CAN: BVFUBJLocationData(RegionName.MENU, ["Beyblade Collectibles"]),
    LocationName.DRAGOON_FIGHTER_CAN: BVFUBJLocationData(RegionName.MENU, ["Beyblade Collectibles"]),
    LocationName.DRANZER_F_CAN: BVFUBJLocationData(RegionName.MENU, ["Beyblade Collectibles"]),
    LocationName.GRIFFOLYON_CAN: BVFUBJLocationData(RegionName.E3R1, ["Beyblade Collectibles"]), #Unknown - green top thing
    LocationName.MASTER_DRAGOON_CAN: BVFUBJLocationData(RegionName.E5R7, ["Beyblade Collectibles"]),
    LocationName.MASTER_DRANZER_CAN: BVFUBJLocationData(RegionName.E6R2, ["Beyblade Collectibles"]),
    LocationName.MASTER_DRACIEL_CAN: BVFUBJLocationData(RegionName.E6R4, ["Beyblade Collectibles"]),
    LocationName.DRACIEL_F_CAN: BVFUBJLocationData(RegionName.E7R6, ["Beyblade Collectibles"]),
    LocationName.WYBORG_CAN: BVFUBJLocationData(RegionName.E4R4, ["Beyblade Collectibles"]),
    LocationName.MASTER_DRIGER_CAN: BVFUBJLocationData(RegionName.E4R3, ["Beyblade Collectibles"]),
    LocationName.WOLBORG_2_CAN: BVFUBJLocationData(RegionName.E5R4, ["Beyblade Collectibles"]),
    LocationName.DRAGOON_V_CAN: BVFUBJLocationData(RegionName.E5R3, ["Beyblade Collectibles"]),
    LocationName.METAL_DRANZER_CAN: BVFUBJLocationData(RegionName.E6R4, ["Beyblade Collectibles"]),
    LocationName.FLASH_LEOPARD_CAN: BVFUBJLocationData(RegionName.E6RB, ["Beyblade Collectibles"]),
    LocationName.DRIGER_V_CAN: BVFUBJLocationData(RegionName.E5R5, ["Beyblade Collectibles"]),
    LocationName.DRANZER_V_CAN: BVFUBJLocationData(RegionName.E4R7, ["Beyblade Collectibles"]),
    LocationName.CYBER_DRAGOON_CAN: BVFUBJLocationData(RegionName.E5R7, ["Beyblade Collectibles"]),
    LocationName.DRACIEL_V_CAN: BVFUBJLocationData(RegionName.E7R1, ["Beyblade Collectibles"]),
    LocationName.HAYATE_HIDDEN_SPIRIT_CAN: BVFUBJLocationData(RegionName.E2R7, ["Beyblade Collectibles"]),
    LocationName.ZINRAI_HIDDEN_SPIRIT_CAN: BVFUBJLocationData(RegionName.E4R4, ["Beyblade Collectibles"]),
    LocationName.CYBER_DRANZER_CAN: BVFUBJLocationData(RegionName.E2R5, ["Beyblade Collectibles"]),
    LocationName.CYBER_DRACIEL_CAN: BVFUBJLocationData(RegionName.E3RB, ["Beyblade Collectibles"]),
    LocationName.CYBER_DRIGER_CAN: BVFUBJLocationData(RegionName.E1RB, ["Beyblade Collectibles"]),
    LocationName.FOX_ICON_CAN: BVFUBJLocationData(RegionName.E2R7, ["Bit Beast Icons"]),
    LocationName.SPIDER_ICON_CAN: BVFUBJLocationData(RegionName.E2R1, ["Bit Beast Icons"]),
    LocationName.SICKLE_WEASEL_ICON_CAN: BVFUBJLocationData(RegionName.E7R2, ["Bit Beast Icons"]),
    LocationName.TYRANNO_ICON_CAN: BVFUBJLocationData(RegionName.E4R1, ["Bit Beast Icons"]),
    LocationName.CLARKEN_ICON_CAN: BVFUBJLocationData(RegionName.E7R1, ["Bit Beast Icons"]),
    LocationName.DRAGOON_ICON_CAN: BVFUBJLocationData(RegionName.E3RB, ["Bit Beast Icons"]),
    LocationName.DRANZER_ICON_CAN: BVFUBJLocationData(RegionName.E4R6, ["Bit Beast Icons"]), #Unknown - light blue enemy
    LocationName.DRACIEL_ICON_CAN: BVFUBJLocationData(RegionName.E5RB, ["Bit Beast Icons"]),
    LocationName.DRIGER_ICON_CAN: BVFUBJLocationData(RegionName.E1R6, ["Bit Beast Icons"]),
    LocationName.CEREBERUS_ICON_CAN: BVFUBJLocationData(RegionName.E5R1, ["Bit Beast Icons"]),
    LocationName.ORTHRUS_ICON_CAN: BVFUBJLocationData(RegionName.E4R4, ["Bit Beast Icons"]),
    LocationName.GABRIEL_ICON_CAN: BVFUBJLocationData(RegionName.E1R4, ["Bit Beast Icons"]),
    LocationName.ARIEL_ICON_CAN: BVFUBJLocationData(RegionName.E7RB, ["Bit Beast Icons"]),
    LocationName.CYBER_DRAGOON_ICON_CAN: BVFUBJLocationData(RegionName.E6R4, ["Bit Beast Icons"]),
    LocationName.CYBER_DRIGER_ICON_CAN: BVFUBJLocationData(RegionName.E2R1, ["Bit Beast Icons"]), # Clash - Pink enemy thing
    LocationName.CYBER_DRANZER_ICON_CAN: BVFUBJLocationData(RegionName.E6R5, ["Bit Beast Icons"]),
    LocationName.CYBER_DRACIEL_ICON_CAN: BVFUBJLocationData(RegionName.E6R2, ["Bit Beast Icons"]),
    LocationName.FLASH_LEOPARD_ICON_CAN: BVFUBJLocationData(RegionName.E7R2, ["Bit Beast Icons"]),
    LocationName.VORTEX_APE_CAN: BVFUBJLocationData(RegionName.E5R5, ["Bit Beast Icons"]),
    LocationName.SHARKRASH_ICON_CAN: BVFUBJLocationData(RegionName.E2RB, ["Bit Beast Icons"]),
    LocationName.VANISHING_MOOT_ICON_CAN: BVFUBJLocationData(RegionName.E6R6, ["Bit Beast Icons"]),
    LocationName.BAT_CAN: BVFUBJLocationData(RegionName.E5R4, ["Characters"]),
    LocationName.BUS_DRIVER_CAN: BVFUBJLocationData(RegionName.E3R2, ["Characters"]),
    LocationName.CHAMELEON_CAN: BVFUBJLocationData(RegionName.E3R7, ["Characters"]),
    LocationName.DARYL_CAN: BVFUBJLocationData(RegionName.E7R6, ["Characters"]),
    LocationName.DIZZI_CAN: BVFUBJLocationData(RegionName.E2R6, ["Characters"]),
    LocationName.DOCTOR_B_CAN: BVFUBJLocationData(RegionName.E4R4, ["Characters"]),
    LocationName.FUNGA_CAN: BVFUBJLocationData(RegionName.E5R6, ["Characters"]),
    LocationName.FIGEL_CAN: BVFUBJLocationData(RegionName.E4R5, ["Characters"]),
    LocationName.GOKI_CAN: BVFUBJLocationData(RegionName.E5R5, ["Characters"]),
    LocationName.GERRY_CAN: BVFUBJLocationData(RegionName.E6R2, ["Characters"]),
    LocationName.GRANDPA_CAN: BVFUBJLocationData(RegionName.E2R4, ["Characters"]),
    LocationName.GIDEON_CAN: BVFUBJLocationData(RegionName.E7R5, ["Characters"]),
    LocationName.HILARY_CAN: BVFUBJLocationData(RegionName.E1R5, ["Characters"]),
    LocationName.JIM_CAN: BVFUBJLocationData(RegionName.E6R1, ["Characters"]),
    LocationName.JOSEPH_CAN: BVFUBJLocationData(RegionName.E4R2, ["Characters"]),
    LocationName.KANE_CAN: BVFUBJLocationData(RegionName.E5R7, ["Characters"]),
    LocationName.KAI_CAN: BVFUBJLocationData(RegionName.E1RB, ["Characters"]),
    LocationName.KENNY_CAN: BVFUBJLocationData(RegionName.E6R4, ["Characters"]),
    LocationName.MARIAM_CAN: BVFUBJLocationData(RegionName.E3R4, ["Characters"]),
    LocationName.MAX_CAN: BVFUBJLocationData(RegionName.E2RB, ["Characters"]),
    LocationName.MEN_IN_BLACK_CAN: BVFUBJLocationData(RegionName.E5R2, ["Characters"]),
    LocationName.MR_DICKINSON_CAN: BVFUBJLocationData(RegionName.E7RB, ["Characters"]),
    LocationName.OZUMA_CAN: BVFUBJLocationData(RegionName.E7R2, ["Characters"]),
    LocationName.RAY_CAN: BVFUBJLocationData(RegionName.E1R2, ["Characters"]),
    LocationName.SALIMA_CAN: BVFUBJLocationData(RegionName.E4R5, ["Characters"]),
    LocationName.SNAKEY_CAN: BVFUBJLocationData(RegionName.E4RB, ["Characters"]),
    LocationName.THE_ROBOT_CAN: BVFUBJLocationData(RegionName.E1R7, ["Characters"]),
    LocationName.TYSON_CAN: BVFUBJLocationData(RegionName.E5R3, ["Characters"]),
}

par_location_table: dict[str, BVFUBJLocationData] = {
    LocationName.E1R1_PAR_TIME: BVFUBJLocationData(RegionName.E1R1, ["Par Times"]),
    LocationName.E1R2_PAR_TIME: BVFUBJLocationData(RegionName.E1R2, ["Par Times"]),
    LocationName.E1R3_PAR_TIME: BVFUBJLocationData(RegionName.E1R3, ["Par Times"]),
    LocationName.E1R4_PAR_TIME: BVFUBJLocationData(RegionName.E1R4, ["Par Times"]),
    LocationName.E1R5_PAR_TIME: BVFUBJLocationData(RegionName.E1R5, ["Par Times"]),
    LocationName.E1R6_PAR_TIME: BVFUBJLocationData(RegionName.E1R6, ["Par Times"]),
    LocationName.E1R7_PAR_TIME: BVFUBJLocationData(RegionName.E1R7, ["Par Times"]),
    LocationName.E1RB_PAR_TIME: BVFUBJLocationData(RegionName.E1RB, ["Par Times"]),
    LocationName.E2R1_PAR_TIME: BVFUBJLocationData(RegionName.E2R1, ["Par Times"]),
    LocationName.E2R2_PAR_TIME: BVFUBJLocationData(RegionName.E2R2, ["Par Times"]),
    LocationName.E2R3_PAR_TIME: BVFUBJLocationData(RegionName.E2R3, ["Par Times"]),
    LocationName.E2R4_PAR_TIME: BVFUBJLocationData(RegionName.E2R4, ["Par Times"]),
    LocationName.E2R5_PAR_TIME: BVFUBJLocationData(RegionName.E2R5, ["Par Times"]),
    LocationName.E2R6_PAR_TIME: BVFUBJLocationData(RegionName.E2R6, ["Par Times"]),
    LocationName.E2R7_PAR_TIME: BVFUBJLocationData(RegionName.E2R7, ["Par Times"]),
    LocationName.E2RB_PAR_TIME: BVFUBJLocationData(RegionName.E2RB, ["Par Times"]),
    LocationName.E3R1_PAR_TIME: BVFUBJLocationData(RegionName.E3R1, ["Par Times"]),
    LocationName.E3R2_PAR_TIME: BVFUBJLocationData(RegionName.E3R2, ["Par Times"]),
    LocationName.E3R3_PAR_TIME: BVFUBJLocationData(RegionName.E3R3, ["Par Times"]),
    LocationName.E3R4_PAR_TIME: BVFUBJLocationData(RegionName.E3R4, ["Par Times"]),
    LocationName.E3R5_PAR_TIME: BVFUBJLocationData(RegionName.E3R5, ["Par Times"]),
    LocationName.E3R6_PAR_TIME: BVFUBJLocationData(RegionName.E3R6, ["Par Times"]),
    LocationName.E3R7_PAR_TIME: BVFUBJLocationData(RegionName.E3R7, ["Par Times"]),
    LocationName.E3RB_PAR_TIME: BVFUBJLocationData(RegionName.E3RB, ["Par Times"]),
    LocationName.E4R1_PAR_TIME: BVFUBJLocationData(RegionName.E4R1, ["Par Times"]),
    LocationName.E4R2_PAR_TIME: BVFUBJLocationData(RegionName.E4R2, ["Par Times"]),
    LocationName.E4R3_PAR_TIME: BVFUBJLocationData(RegionName.E4R3, ["Par Times"]),
    LocationName.E4R4_PAR_TIME: BVFUBJLocationData(RegionName.E4R4, ["Par Times"]),
    LocationName.E4R5_PAR_TIME: BVFUBJLocationData(RegionName.E4R5, ["Par Times"]),
    LocationName.E4R6_PAR_TIME: BVFUBJLocationData(RegionName.E4R6, ["Par Times"]),
    LocationName.E4R7_PAR_TIME: BVFUBJLocationData(RegionName.E4R7, ["Par Times"]),
    LocationName.E4RB_PAR_TIME: BVFUBJLocationData(RegionName.E4RB, ["Par Times"]),
    LocationName.E5R1_PAR_TIME: BVFUBJLocationData(RegionName.E5R1, ["Par Times"]),
    LocationName.E5R2_PAR_TIME: BVFUBJLocationData(RegionName.E5R2, ["Par Times"]),
    LocationName.E5R3_PAR_TIME: BVFUBJLocationData(RegionName.E5R3, ["Par Times"]),
    LocationName.E5R4_PAR_TIME: BVFUBJLocationData(RegionName.E5R4, ["Par Times"]),
    LocationName.E5R5_PAR_TIME: BVFUBJLocationData(RegionName.E5R5, ["Par Times"]),
    LocationName.E5R6_PAR_TIME: BVFUBJLocationData(RegionName.E5R6, ["Par Times"]),
    LocationName.E5R7_PAR_TIME: BVFUBJLocationData(RegionName.E5R7, ["Par Times"]),
    LocationName.E5RB_PAR_TIME: BVFUBJLocationData(RegionName.E5RB, ["Par Times"]),
    LocationName.E6R1_PAR_TIME: BVFUBJLocationData(RegionName.E6R1, ["Par Times"]),
    LocationName.E6R2_PAR_TIME: BVFUBJLocationData(RegionName.E6R2, ["Par Times"]),
    LocationName.E6R3_PAR_TIME: BVFUBJLocationData(RegionName.E6R3, ["Par Times"]),
    LocationName.E6R4_PAR_TIME: BVFUBJLocationData(RegionName.E6R4, ["Par Times"]),
    LocationName.E6R5_PAR_TIME: BVFUBJLocationData(RegionName.E6R5, ["Par Times"]),
    LocationName.E6R6_PAR_TIME: BVFUBJLocationData(RegionName.E6R6, ["Par Times"]),
    LocationName.E6R7_PAR_TIME: BVFUBJLocationData(RegionName.E6R7, ["Par Times"]),
    LocationName.E6RB_PAR_TIME: BVFUBJLocationData(RegionName.E6RB, ["Par Times"]),
    LocationName.E7R1_PAR_TIME: BVFUBJLocationData(RegionName.E7R1, ["Par Times"]),
    LocationName.E7R2_PAR_TIME: BVFUBJLocationData(RegionName.E7R2, ["Par Times"]),
    LocationName.E7R3_PAR_TIME: BVFUBJLocationData(RegionName.E7R3, ["Par Times"]),
    LocationName.E7R4_PAR_TIME: BVFUBJLocationData(RegionName.E7R4, ["Par Times"]),
    LocationName.E7R5_PAR_TIME: BVFUBJLocationData(RegionName.E7R5, ["Par Times"]),
    LocationName.E7R6_PAR_TIME: BVFUBJLocationData(RegionName.E7R6, ["Par Times"]),
    LocationName.E7R7_PAR_TIME: BVFUBJLocationData(RegionName.E7R7, ["Par Times"]),
    LocationName.E7RB_PAR_TIME: BVFUBJLocationData(RegionName.E7RB, ["Par Times"]),
}

all_location_table: dict[str, BVFUBJLocationData] = {**base_location_table, **par_location_table}

def get_location_name_to_id() -> dict[str, int]:
    dict_locs: dict[str, int] = {}
    for name, data in all_location_table.items():
        dict_locs.update({name: len(dict_locs) + 1})
    return dict_locs

def get_location_names_per_category() -> dict[str, set[str]]:
    categories: dict[str, set[str]] = {}

    for name, data in all_location_table.items():
        for category in data.location_groups:
            categories.setdefault(category, set()).add(name)

    return categories

LOCATION_NAME_TO_ID: dict[str, int] = get_location_name_to_id()


def create_all_locations(world: "BVFUBJWorld"):
    for loc, data in base_location_table.items():
        if data.req_options:
            req_option_list: list = [getattr(world.options, x).value in y for (x,y) in data.req_options.option_list.items()]
            option_value: bool = all(req_option_list) if data.req_options.combine else any(req_option_list)
            if not option_value:
                continue

        reg = world.get_region(data.region)
        location = BVFUBJLocation(world.player, loc, list(all_location_table.keys()).index(loc), reg)
        if data.access is not None:
            world.set_rule(location, data.access)

        reg.locations += [location]

    for loc, data in par_location_table.items():
        if world.options.par_checks:
            reg = world.get_region(data.region)
            location = BVFUBJLocation(world.player, loc, list(all_location_table.keys()).index(loc), reg)
            if data.access is not None:
                world.set_rule(location, data.access)

            reg.locations += [location]
        else:
            da_rule = data.access if data.access else True_()
            world.get_region(data.region).add_event(loc, "Par Time", da_rule, BVFUBJLocation, BVFUBJItem, True)