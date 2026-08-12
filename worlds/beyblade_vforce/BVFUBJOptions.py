from dataclasses import dataclass
from typing import Dict, Any

from Options import Toggle, Range, PerGameCommonOptions, Choice, StartInventoryPool, DeathLinkMixin, OptionSet, \
    DefaultOnToggle, OptionDict, OptionCounter, OptionGroup
from .Items import trap_filler_items


#Example Options from Luigi's Mansion


class RamdomEpisodes(Toggle):
    """Episode unlocks are shuffled in as progressive items by default. With this option enabled, episodes will be
        shuffled in a random order instead"""
    display_name = "Random Episodes"
    internal_name = "random_episodes"
    option_progressive = 0
    option_random = 1
    default = 0

class RoundShuffle(Choice):
    """Shuffle the rounds in each episode. Random round unlocks will still require their corresponding episode to
        be unlocked before they can be played"""
    display_name = "Round Shuffle"
    internal_name = "shuffle_rounds"
    option_off = 0
    option_progressive = 1
    option_random = 2
    default = 0

class ParChecks(Toggle):
    """Add par times for each course as locations"""
    display_name = "Round Shuffle"
    internal_name = "par_checks"

class ShuffleMoves(Toggle):
    """Shuffle in the Beyblade's accelerate, brake and ultimate abilities"""
    display_name = "Round Shuffle"
    internal_name = "shuffle_moves"

class ShufflePads(Toggle):
    """Shuffle in jump, boost and recharge pads as both locations and items"""
    display_name = "Round Shuffle"
    internal_name = "shuffle_pads"

class FillerWeights(OptionCounter):
    """
    Set filler weights for filler items.
    Each weight represents a number of balls in a lottery roller with that trap on it.
    So if you had Banana Trap set to 3, and Ice Trap set to 7, and the rest set to 0,
    you would have a 3/10 for a Banana Trap to be chosen when rolling for trap fillers
    Must be between 0 and 100
    """
    display_name = "Filler Weights"
    internal_name = "filler_weights"
    min = 0
    max = 100
    valid_keys = ["Bundles", "Coins", "Bills", "Bars", "Gems", "Dust", "Hearts"]
    default = {
        "Bundles": 10,
        "Coins": 15,
        "Bills": 10,
        "Bars": 10,
        "Gems": 5,
        "Dust": 40,
        "Hearts": 10
    }
    all_on_dict = {item: 100 for item in valid_keys}
    all_off_dict = {item: 0 for item in valid_keys}

class TrapWeights(OptionCounter):# Affects item pool but not logic. used in create_items step
    """
    Set Trap Weights for traps chosen as filler items, if Trap Percentage is greater than 0.
    Each weight represents a number of balls in a lottery roller with that trap on it.
    So if you had Daredevil Trap set to 3, and Joy Trap set to 7, and the rest set to 0,
    you would have a 3/10 chance for a Daredevil Trap to be chosen when rolling for trap fillers
    Must be between 0 and 100
    """
    display_name = "Trap Weights"
    internal_name = "trap_weights"
    min = 0
    max = 100
    valid_keys = trap_filler_items.keys()
    default = {item: data.default_weight for item, data in trap_filler_items.items()}
    all_on_dict = {item: 100 for item in trap_filler_items.keys()}
    all_off_dict = {item: 0 for item in trap_filler_items.keys()}


class TrapPercentage(Range):# Affects item pool but not logic. used in create_items step
    """
    Set the percentage of filler items that are traps. Default percentage is 0%
    """
    display_name = "Trap Percentage"
    internal_name = "trap_percentage"
    range_start = 0
    range_end = 100
    default = 0

class Option1(DefaultOnToggle):
    """
    If enabled, in-game hints will be sent out to the multiworld when discovered.

    This is automatically disabled if hint distribution is set to Junk, Disabled or Vague
    """
    display_name = "Send Hints"
    internal_name = "send_hints"

@dataclass
class  BVFUBJOptions(DeathLinkMixin, PerGameCommonOptions):
    trap_weights: TrapWeights
    trap_percentage: TrapPercentage
    Option1: Option1
    start_inventory_from_pool: StartInventoryPool


trap_settings = {
    FillerWeights.internal_name:             FillerWeights.all_off_dict,
}

game_options_presets: Dict[str, Dict[str, Any]] = {
    "Raining Traps": trap_settings,

}

options_groups = [
        OptionGroup("Extra Locations", [
            Option1,
        ]),
        OptionGroup("Itempool Changes", [
            TrapWeights,
            TrapPercentage,
        ])
    ]