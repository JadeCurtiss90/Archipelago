from typing import NamedTuple, Optional

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

}


all_items_table: dict[str, BVFUBJItemData] = {**base_item_table, }

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