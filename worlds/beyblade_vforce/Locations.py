from typing import Optional, NamedTuple, Any, TYPE_CHECKING

from BaseClasses import Location, Region
from rule_builder.rules import Rule

from . import Helpers_Function
from .Constants.Names import location_names as LocationName
from .Constants.world_constants import GAME_NAME

if TYPE_CHECKING:
    from .world import BVFUBJWorld

class BVFUBJOptionData(NamedTuple):
    option_list: dict[str, list[Any]]
    combine: bool = True

class  BVFUBJLocationData(NamedTuple):
    region: str
    location_groups: list[str]  # one or more groups that this location belongs to
    access: Rule[Any] = None
    req_options: BVFUBJOptionData = None
    ram_data: Helpers_Function.RamData = None


class  BVFUBJLocation(Location):
    game: str = GAME_NAME
    data: BVFUBJLocationData

    def __init__(self, player: int, name: str, address: Optional[int], parent: Optional[Region]):
        super(BVFUBJLocation, self).__init__(player, name, address, parent)
        self.data = all_location_table[name]
        self.address = LOCATION_NAME_TO_ID["item"] if "item" in LOCATION_NAME_TO_ID else None


all_location_table: dict[str, BVFUBJLocationData] = {

}

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
    for loc, data in all_location_table.items():
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