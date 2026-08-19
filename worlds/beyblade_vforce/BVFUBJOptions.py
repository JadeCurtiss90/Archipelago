from dataclasses import dataclass
from typing import Dict, Any

from Options import Toggle, Range, PerGameCommonOptions, Choice, StartInventoryPool, DeathLinkMixin, OptionSet, \
    DefaultOnToggle, OptionDict, OptionCounter, OptionGroup
from Items import trap_item_table


#Example Options from Luigi's Mansion


class RandomEpisodes(Toggle):
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
    display_name = "Par Checks"
    internal_name = "par_checks"

class ShuffleMoves(Toggle):
    """Shuffle in the Beyblade's accelerate, brake and ultimate abilities"""
    display_name = "Move Shuffle"
    internal_name = "shuffle_moves"

class ProgressiveStaminaUnlocks(Choice):
    """Shuffle in the Beyblade's maximum stamina (AKA the length of the ripcord bar). Either the four colored ripcord
        segments, or the sixteen notches on those segments, can be shuffled"""
    display_name = "Progressive Stamina Shuffle"
    internal_name = "shuffle_progressive_stamina"
    option_off = 0
    option_progressive_colors = 1
    option_progressive_notches = 2
    default = 0

class ShufflePads(Toggle):
    """Shuffle in jump, boost and recharge pads as both locations and items"""
    display_name = "Shuffle Pads"
    internal_name = "shuffle_pads"

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
    valid_keys = trap_item_table.keys()
    default = {item: data.default_weight for item, data in trap_item_table.items()}
    all_on_dict = {item: 100 for item in trap_item_table.keys()}
    all_off_dict = {item: 0 for item in trap_item_table.keys()}


class TrapPercentage(Range):# Affects item pool but not logic. used in create_items step
    """
    Set the percentage of filler items that are traps. Default percentage is 0%
    """
    display_name = "Trap Percentage"
    internal_name = "trap_percentage"
    range_start = 0
    range_end = 100
    default = 0

@dataclass
class  BVFUBJOptions(DeathLinkMixin, PerGameCommonOptions):
    trap_weights: TrapWeights
    trap_percentage: TrapPercentage
    random_episodes: RandomEpisodes
    round_shuffle: RoundShuffle
    par_checks: ParChecks
    shuffle_moves: ShuffleMoves
    progressive_stamina_unlocks: ProgressiveStaminaUnlocks
    shuffle_pads: ShufflePads
    start_inventory_from_pool: StartInventoryPool


trap_settings = {
    TrapWeights.internal_name:             TrapWeights.all_on_dict,
}

game_options_presets: Dict[str, Dict[str, Any]] = {
    "Raining Traps": trap_settings,

}

options_groups = [
        OptionGroup("Episode & Round Access", [
            RandomEpisodes,
            RoundShuffle,
        ]),
        OptionGroup("Extra Locations", [
            ParChecks,
        ]),
        OptionGroup("Logic Changes", [
            ShuffleMoves,
            ShufflePads,
            ProgressiveStaminaUnlocks
        ]),
        OptionGroup("Itempool Changes", [
            TrapWeights,
            TrapPercentage,
        ]),
    ]