from typing import Any

from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, True_, Has

from . import BVFUBJOptions as bey_opt
from .Constants.Names import item_names as itemname, location_names as locname

ProgEpisode: Rule[Any] = (True_() & OptionFilter(bey_opt.RandomEpisodes, 0))
RandEpisode: Rule[Any] = (True_() & OptionFilter(bey_opt.RandomEpisodes, 1))
Episode1Acc: Rule[Any] = (ProgEpisode & Has(itemname.PROGRESSIVE_EPISODE_UNLOCK)
                          | RandEpisode & Has(itemname.E1_UNLOCK))
Episode2Acc: Rule[Any] = (ProgEpisode & Has(itemname.PROGRESSIVE_EPISODE_UNLOCK, 2)
                          | RandEpisode & Has(itemname.E2_UNLOCK))

OpenRounds: Rule[Any] = True_() & OptionFilter(bey_opt.RoundShuffle, 0)
ProgRound: Rule[Any] = True_() & OptionFilter(bey_opt.RoundShuffle, 1)
RandRound: Rule[Any] = (True_() & OptionFilter(bey_opt.RoundShuffle, 2) | OpenRounds)