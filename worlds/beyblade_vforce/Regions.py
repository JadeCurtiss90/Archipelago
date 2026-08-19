from typing import NamedTuple, Optional, List, TYPE_CHECKING
from BaseClasses import Region, MultiWorld
from rule_builder.rules import Has, True_
from .Constants.Names import region_names as RegionName, item_names as itemname
from . import Rules

if TYPE_CHECKING:
    from .world import BVFUBJWorld

class BVFUBJRegionData(NamedTuple):
    address = 1

class BVFUBJRegion(Region):
    game: str = "Game"
    region_data: BVFUBJRegionData

    def __init__(self, region_name: str, region_data: BVFUBJRegionData, player: int, multiworld: MultiWorld):
        super().__init__(region_name, player, multiworld)
        self.region_data = region_data

region_list: dict[str, BVFUBJRegionData] = {
    RegionName.ADVENTUREMODE: BVFUBJRegionData(),
    RegionName.MENU: BVFUBJRegionData(),
    RegionName.E1: BVFUBJRegionData(),
    RegionName.E1R1: BVFUBJRegionData(),
    RegionName.E1R2: BVFUBJRegionData(),
    RegionName.E1R3: BVFUBJRegionData(),
    RegionName.E1R4: BVFUBJRegionData(),
    RegionName.E1R5: BVFUBJRegionData(),
    RegionName.E1R6: BVFUBJRegionData(),
    RegionName.E1R7: BVFUBJRegionData(),
    RegionName.E1RB: BVFUBJRegionData(),
    RegionName.E2: BVFUBJRegionData(),
    RegionName.E2R1: BVFUBJRegionData(),
    RegionName.E2R2: BVFUBJRegionData(),
    RegionName.E2R3: BVFUBJRegionData(),
    RegionName.E2R4: BVFUBJRegionData(),
    RegionName.E2R5: BVFUBJRegionData(),
    RegionName.E2R6: BVFUBJRegionData(),
    RegionName.E2R7: BVFUBJRegionData(),
    RegionName.E2RB: BVFUBJRegionData(),
    RegionName.E3: BVFUBJRegionData(),
    RegionName.E3R1: BVFUBJRegionData(),
    RegionName.E3R2: BVFUBJRegionData(),
    RegionName.E3R3: BVFUBJRegionData(),
    RegionName.E3R4: BVFUBJRegionData(),
    RegionName.E3R5: BVFUBJRegionData(),
    RegionName.E3R6: BVFUBJRegionData(),
    RegionName.E3R7: BVFUBJRegionData(),
    RegionName.E3RB: BVFUBJRegionData(),
    RegionName.E4: BVFUBJRegionData(),
    RegionName.E4R1: BVFUBJRegionData(),
    RegionName.E4R2: BVFUBJRegionData(),
    RegionName.E4R3: BVFUBJRegionData(),
    RegionName.E4R4: BVFUBJRegionData(),
    RegionName.E4R5: BVFUBJRegionData(),
    RegionName.E4R6: BVFUBJRegionData(),
    RegionName.E4R7: BVFUBJRegionData(),
    RegionName.E4RB: BVFUBJRegionData(),
    RegionName.E5: BVFUBJRegionData(),
    RegionName.E5R1: BVFUBJRegionData(),
    RegionName.E5R2: BVFUBJRegionData(),
    RegionName.E5R3: BVFUBJRegionData(),
    RegionName.E5R4: BVFUBJRegionData(),
    RegionName.E5R5: BVFUBJRegionData(),
    RegionName.E5R6: BVFUBJRegionData(),
    RegionName.E5R7: BVFUBJRegionData(),
    RegionName.E5RB: BVFUBJRegionData(),
    RegionName.E6: BVFUBJRegionData(),
    RegionName.E6R1: BVFUBJRegionData(),
    RegionName.E6R2: BVFUBJRegionData(),
    RegionName.E6R3: BVFUBJRegionData(),
    RegionName.E6R4: BVFUBJRegionData(),
    RegionName.E6R5: BVFUBJRegionData(),
    RegionName.E6R6: BVFUBJRegionData(),
    RegionName.E6R7: BVFUBJRegionData(),
    RegionName.E6RB: BVFUBJRegionData(),
    RegionName.E7: BVFUBJRegionData(),
    RegionName.E7R1: BVFUBJRegionData(),
    RegionName.E7R2: BVFUBJRegionData(),
    RegionName.E7R3: BVFUBJRegionData(),
    RegionName.E7R4: BVFUBJRegionData(),
    RegionName.E7R5: BVFUBJRegionData(),
    RegionName.E7R6: BVFUBJRegionData(),
    RegionName.E7R7: BVFUBJRegionData(),
    RegionName.E7RB: BVFUBJRegionData()
}

def create_and_connect_regions(world: "BVFUBJWorld"):
    for region_name in region_list.keys():
        world.multiworld.regions.append(BVFUBJRegion(region_name, region_list[region_name], world.player, world.multiworld))

    world.get_region(RegionName.MENU).connect(world.get_region(RegionName.ADVENTUREMODE))
    world.get_region(RegionName.ADVENTUREMODE).connect(world.get_region(RegionName.E1),
                                                       rule=Rules.Episode1Acc)
    world.get_region(RegionName.E1).connect(world.get_region(RegionName.E1R1),
                                            rule=Rules.Episode1Round1Acc)
    world.get_region(RegionName.E1).connect(world.get_region(RegionName.E1R2),
                                            rule=Rules.Episode1Round2Acc)
    world.get_region(RegionName.E1).connect(world.get_region(RegionName.E1R3))
    world.get_region(RegionName.E1).connect(world.get_region(RegionName.E1R4))
    world.get_region(RegionName.E1).connect(world.get_region(RegionName.E1R5))
    world.get_region(RegionName.E1).connect(world.get_region(RegionName.E1R6))
    world.get_region(RegionName.E1).connect(world.get_region(RegionName.E1R7))
    world.get_region(RegionName.E1).connect(world.get_region(RegionName.E1RB))
    world.get_region(RegionName.ADVENTUREMODE).connect(world.get_region(RegionName.E2),
                                                       rule=Rules.Episode2Acc)
    world.get_region(RegionName.E2).connect(world.get_region(RegionName.E2R1))
    world.get_region(RegionName.E2).connect(world.get_region(RegionName.E2R2))
    world.get_region(RegionName.E2).connect(world.get_region(RegionName.E2R3))
    world.get_region(RegionName.E2).connect(world.get_region(RegionName.E2R4))
    world.get_region(RegionName.E2).connect(world.get_region(RegionName.E2R5))
    world.get_region(RegionName.E2).connect(world.get_region(RegionName.E2R6))
    world.get_region(RegionName.E2).connect(world.get_region(RegionName.E2R7))
    world.get_region(RegionName.E2).connect(world.get_region(RegionName.E2RB))
    world.get_region(RegionName.ADVENTUREMODE).connect(world.get_region(RegionName.E3))
    world.get_region(RegionName.E3).connect(world.get_region(RegionName.E3R1))
    world.get_region(RegionName.E3).connect(world.get_region(RegionName.E3R2))
    world.get_region(RegionName.E3).connect(world.get_region(RegionName.E3R3))
    world.get_region(RegionName.E3).connect(world.get_region(RegionName.E3R4))
    world.get_region(RegionName.E3).connect(world.get_region(RegionName.E3R5))
    world.get_region(RegionName.E3).connect(world.get_region(RegionName.E3R6))
    world.get_region(RegionName.E3).connect(world.get_region(RegionName.E3R7))
    world.get_region(RegionName.E3).connect(world.get_region(RegionName.E3RB))
    world.get_region(RegionName.ADVENTUREMODE).connect(world.get_region(RegionName.E4))
    world.get_region(RegionName.E4).connect(world.get_region(RegionName.E4R1))
    world.get_region(RegionName.E4).connect(world.get_region(RegionName.E4R2))
    world.get_region(RegionName.E4).connect(world.get_region(RegionName.E4R3))
    world.get_region(RegionName.E4).connect(world.get_region(RegionName.E4R4))
    world.get_region(RegionName.E4).connect(world.get_region(RegionName.E4R5))
    world.get_region(RegionName.E4).connect(world.get_region(RegionName.E4R6))
    world.get_region(RegionName.E4).connect(world.get_region(RegionName.E4R7))
    world.get_region(RegionName.E4).connect(world.get_region(RegionName.E4RB))
    world.get_region(RegionName.ADVENTUREMODE).connect(world.get_region(RegionName.E5))
    world.get_region(RegionName.E5).connect(world.get_region(RegionName.E5R1))
    world.get_region(RegionName.E5).connect(world.get_region(RegionName.E5R2))
    world.get_region(RegionName.E5).connect(world.get_region(RegionName.E5R3))
    world.get_region(RegionName.E5).connect(world.get_region(RegionName.E5R4))
    world.get_region(RegionName.E5).connect(world.get_region(RegionName.E5R5))
    world.get_region(RegionName.E5).connect(world.get_region(RegionName.E5R6))
    world.get_region(RegionName.E5).connect(world.get_region(RegionName.E5R7))
    world.get_region(RegionName.E5).connect(world.get_region(RegionName.E5RB))
    world.get_region(RegionName.ADVENTUREMODE).connect(world.get_region(RegionName.E6))
    world.get_region(RegionName.E6).connect(world.get_region(RegionName.E6R1))
    world.get_region(RegionName.E6).connect(world.get_region(RegionName.E6R2))
    world.get_region(RegionName.E6).connect(world.get_region(RegionName.E6R3))
    world.get_region(RegionName.E6).connect(world.get_region(RegionName.E6R4))
    world.get_region(RegionName.E6).connect(world.get_region(RegionName.E6R5))
    world.get_region(RegionName.E6).connect(world.get_region(RegionName.E6R6))
    world.get_region(RegionName.E6).connect(world.get_region(RegionName.E6R7))
    world.get_region(RegionName.E6).connect(world.get_region(RegionName.E6RB))
    world.get_region(RegionName.ADVENTUREMODE).connect(world.get_region(RegionName.E7))
    world.get_region(RegionName.E7).connect(world.get_region(RegionName.E7R1))
    world.get_region(RegionName.E7).connect(world.get_region(RegionName.E7R2))
    world.get_region(RegionName.E7).connect(world.get_region(RegionName.E7R3))
    world.get_region(RegionName.E7).connect(world.get_region(RegionName.E7R4))
    world.get_region(RegionName.E7).connect(world.get_region(RegionName.E7R5))
    world.get_region(RegionName.E7).connect(world.get_region(RegionName.E7R6))
    world.get_region(RegionName.E7).connect(world.get_region(RegionName.E7R7))
    world.get_region(RegionName.E7).connect(world.get_region(RegionName.E7RB))