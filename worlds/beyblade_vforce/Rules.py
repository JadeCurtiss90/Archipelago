from typing import Any

from rule_builder.options import OptionFilter
from rule_builder.rules import Rule, True_, Has, CanReachLocation

from . import BVFUBJOptions as bey_opt
from .Constants.Names import item_names as itemname, location_names as locname, region_names as regname

ProgEpisode: Rule[Any] = (True_() & OptionFilter(bey_opt.RandomEpisodes, 0))
RandEpisode: Rule[Any] = (True_() & OptionFilter(bey_opt.RandomEpisodes, 1))
Episode1Acc: Rule[Any] = (ProgEpisode & Has(itemname.PROGRESSIVE_EPISODE_UNLOCK)
                          | RandEpisode & Has(itemname.E1_UNLOCK))
Episode2Acc: Rule[Any] = (ProgEpisode & Has(itemname.PROGRESSIVE_EPISODE_UNLOCK, 2)
                          | RandEpisode & Has(itemname.E2_UNLOCK))
Episode3Acc: Rule[Any] = (ProgEpisode & Has(itemname.PROGRESSIVE_EPISODE_UNLOCK, 3)
                         | RandEpisode & Has(itemname.E3_UNLOCK))
Episode4Acc: Rule[Any] = (ProgEpisode & Has(itemname.PROGRESSIVE_EPISODE_UNLOCK, 4)
                         | RandEpisode & Has(itemname.E4_UNLOCK))
Episode5Acc: Rule[Any] = (ProgEpisode & Has(itemname.PROGRESSIVE_EPISODE_UNLOCK, 5)
                         | RandEpisode & Has(itemname.E5_UNLOCK))
Episode6Acc: Rule[Any] = (ProgEpisode & Has(itemname.PROGRESSIVE_EPISODE_UNLOCK, 6)
                         | RandEpisode & Has(itemname.E6_UNLOCK))
Episode7Acc: Rule[Any] = (ProgEpisode & Has(itemname.PROGRESSIVE_EPISODE_UNLOCK, 7)
                          | RandEpisode & Has(itemname.E7_UNLOCK))

OpenRounds: Rule[Any] = True_() & OptionFilter(bey_opt.RoundShuffle, 0)
ProgRound: Rule[Any] = True_() & OptionFilter(bey_opt.RoundShuffle, 1)
RandRound: Rule[Any] = (True_() & OptionFilter(bey_opt.RoundShuffle, 2))
Episode1Round1Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 1)
                          | RandRound & Has(itemname.E1R1_UNLOCK) | OpenRounds)
Episode1Round2Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 2)
                         | RandRound & Has(itemname.E1R2_UNLOCK) | OpenRounds)
Episode1Round3Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 3)
                         | RandRound & Has(itemname.E1R3_UNLOCK) | OpenRounds)
Episode1Round4Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 4)
                         | RandRound & Has(itemname.E1R4_UNLOCK) | OpenRounds)
Episode1Round5Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 5)
                         | RandRound & Has(itemname.E1R5_UNLOCK) | OpenRounds)
Episode1Round6Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 6)
                         | RandRound & Has(itemname.E1R6_UNLOCK) | OpenRounds)
Episode1Round7Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 7)
                          | RandRound & Has(itemname.E1R7_UNLOCK) | OpenRounds)
Episode1RoundBAcc: Rule[Any] = ((CanReachLocation(E1R1Par_Location, parent_region_name=regname.E1) &
                               CanReachLocation(E1R2Par_Location, parent_region_name=regname.E1) &
                               CanReachLocation(E1R3Par_Location, parent_region_name=regname.E1) &
                               CanReachLocation(E1R4Par_Location, parent_region_name=regname.E1) &
                               CanReachLocation(E1R5Par_Location, parent_region_name=regname.E1) &
                               CanReachLocation(E1R6Par_Location, parent_region_name=regname.E1) &
                               CanReachLocation(E1R7Par_Location, parent_region_name=regname.E1)) &
                               ((ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 8)) |
                               (RandRound & Has(itemname.E1RB_UNLOCK) | OpenRounds)))
Episode2Round1Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 9)
                         | RandRound & Has(itemname.E2R1_UNLOCK) | OpenRounds)
Episode2Round2Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 10)
                        | RandRound & Has(itemname.E2R2_UNLOCK) | OpenRounds)
Episode2Round3Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 11)
                        | RandRound & Has(itemname.E2R3_UNLOCK) | OpenRounds)
Episode2Round4Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 12)
                        | RandRound & Has(itemname.E2R4_UNLOCK) | OpenRounds)
Episode2Round5Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 13)
                        | RandRound & Has(itemname.E2R5_UNLOCK) | OpenRounds)
Episode2Round6Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 14)
                        | RandRound & Has(itemname.E2R6_UNLOCK) | OpenRounds)
Episode2Round7Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 15)
                         | RandRound & Has(itemname.E2R7_UNLOCK) | OpenRounds)
Episode2RoundBAcc: Rule[Any] = ((CanReachLocation(E2R1Par_Location, parent_region_name=regname.E2) &
                               CanReachLocation(E2R2Par_Location, parent_region_name=regname.E2) &
                               CanReachLocation(E2R3Par_Location, parent_region_name=regname.E2) &
                               CanReachLocation(E2R4Par_Location, parent_region_name=regname.E2) &
                               CanReachLocation(E2R5Par_Location, parent_region_name=regname.E2) &
                               CanReachLocation(E2R6Par_Location, parent_region_name=regname.E2) &
                               CanReachLocation(E2R7Par_Location, parent_region_name=regname.E2)) &
                               ((ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 16)) |
                               (RandRound & Has(itemname.E2RB_UNLOCK) | OpenRounds)))
Episode3Round1Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 17)
                         | RandRound & Has(itemname.E3R1_UNLOCK) | OpenRounds)
Episode3Round2Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 18)
                        | RandRound & Has(itemname.E3R2_UNLOCK) | OpenRounds)
Episode3Round3Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 19)
                        | RandRound & Has(itemname.E3R3_UNLOCK) | OpenRounds)
Episode3Round4Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 20)
                        | RandRound & Has(itemname.E3R4_UNLOCK) | OpenRounds)
Episode3Round5Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 21)
                        | RandRound & Has(itemname.E3R5_UNLOCK) | OpenRounds)
Episode3Round6Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 22)
                        | RandRound & Has(itemname.E3R6_UNLOCK) | OpenRounds)
Episode3Round7Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 23)
                         | RandRound & Has(itemname.E3R7_UNLOCK) | OpenRounds)
Episode3RoundBAcc: Rule[Any] = ((CanReachLocation(E3R1Par_Location, parent_region_name=regname.E3) &
                               CanReachLocation(E3R2Par_Location, parent_region_name=regname.E3) &
                               CanReachLocation(E3R3Par_Location, parent_region_name=regname.E3) &
                               CanReachLocation(E3R4Par_Location, parent_region_name=regname.E3) &
                               CanReachLocation(E3R5Par_Location, parent_region_name=regname.E3) &
                               CanReachLocation(E3R6Par_Location, parent_region_name=regname.E3) &
                               CanReachLocation(E3R7Par_Location, parent_region_name=regname.E3)) &
                               ((ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 24)) |
                               (RandRound & Has(itemname.E3RB_UNLOCK) | OpenRounds)))
Episode4Round1Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 25)
                         | RandRound & Has(itemname.E4R1_UNLOCK) | OpenRounds)
Episode4Round2Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 26)
                        | RandRound & Has(itemname.E4R2_UNLOCK) | OpenRounds)
Episode4Round3Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 27)
                        | RandRound & Has(itemname.E4R3_UNLOCK) | OpenRounds)
Episode4Round4Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 28)
                        | RandRound & Has(itemname.E4R4_UNLOCK) | OpenRounds)
Episode4Round5Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 29)
                        | RandRound & Has(itemname.E4R5_UNLOCK) | OpenRounds)
Episode4Round6Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 30)
                        | RandRound & Has(itemname.E4R6_UNLOCK) | OpenRounds)
Episode4Round7Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 31)
                         | RandRound & Has(itemname.E4R7_UNLOCK) | OpenRounds)
Episode4RoundBAcc: Rule[Any] = ((CanReachLocation(E4R1Par_Location, parent_region_name=regname.E4) &
                               CanReachLocation(E4R2Par_Location, parent_region_name=regname.E4) &
                               CanReachLocation(E4R3Par_Location, parent_region_name=regname.E4) &
                               CanReachLocation(E4R4Par_Location, parent_region_name=regname.E4) &
                               CanReachLocation(E4R5Par_Location, parent_region_name=regname.E4) &
                               CanReachLocation(E4R6Par_Location, parent_region_name=regname.E4) &
                               CanReachLocation(E4R7Par_Location, parent_region_name=regname.E4)) &
                               ((ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 32)) |
                               (RandRound & Has(itemname.E4RB_UNLOCK) | OpenRounds)))
Episode5Round1Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 33)
                         | RandRound & Has(itemname.E5R1_UNLOCK) | OpenRounds)
Episode5Round2Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 34)
                        | RandRound & Has(itemname.E5R2_UNLOCK) | OpenRounds)
Episode5Round3Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 35)
                        | RandRound & Has(itemname.E5R3_UNLOCK) | OpenRounds)
Episode5Round4Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 36)
                        | RandRound & Has(itemname.E5R4_UNLOCK) | OpenRounds)
Episode5Round5Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 37)
                        | RandRound & Has(itemname.E5R5_UNLOCK) | OpenRounds)
Episode5Round6Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 38)
                        | RandRound & Has(itemname.E5R6_UNLOCK) | OpenRounds)
Episode5Round7Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 39)
                         | RandRound & Has(itemname.E5R7_UNLOCK) | OpenRounds)
Episode5RoundBAcc: Rule[Any] = ((CanReachLocation(E5R1Par_Location, parent_region_name=regname.E5) &
                               CanReachLocation(E5R2Par_Location, parent_region_name=regname.E5) &
                               CanReachLocation(E5R3Par_Location, parent_region_name=regname.E5) &
                               CanReachLocation(E5R4Par_Location, parent_region_name=regname.E5) &
                               CanReachLocation(E5R5Par_Location, parent_region_name=regname.E5) &
                               CanReachLocation(E5R6Par_Location, parent_region_name=regname.E5) &
                               CanReachLocation(E5R7Par_Location, parent_region_name=regname.E5)) &
                               ((ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 40)) |
                               (RandRound & Has(itemname.E5RB_UNLOCK) | OpenRounds)))
Episode6Round1Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 41)
                         | RandRound & Has(itemname.E6R1_UNLOCK) | OpenRounds)
Episode6Round2Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 42)
                        | RandRound & Has(itemname.E6R2_UNLOCK) | OpenRounds)
Episode6Round3Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 43)
                        | RandRound & Has(itemname.E6R3_UNLOCK) | OpenRounds)
Episode6Round4Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 44)
                        | RandRound & Has(itemname.E6R4_UNLOCK) | OpenRounds)
Episode6Round5Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 45)
                        | RandRound & Has(itemname.E6R5_UNLOCK) | OpenRounds)
Episode6Round6Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 46)
                        | RandRound & Has(itemname.E6R6_UNLOCK) | OpenRounds)
Episode6Round7Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 47)
                         | RandRound & Has(itemname.E6R7_UNLOCK) | OpenRounds)
Episode6RoundBAcc: Rule[Any] = ((CanReachLocation(E6R1Par_Location, parent_region_name=regname.E6) &
                               CanReachLocation(E6R2Par_Location, parent_region_name=regname.E6) &
                               CanReachLocation(E6R3Par_Location, parent_region_name=regname.E6) &
                               CanReachLocation(E6R4Par_Location, parent_region_name=regname.E6) &
                               CanReachLocation(E6R5Par_Location, parent_region_name=regname.E6) &
                               CanReachLocation(E6R6Par_Location, parent_region_name=regname.E6) &
                               CanReachLocation(E6R7Par_Location, parent_region_name=regname.E6)) &
                               ((ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 48)) |
                               (RandRound & Has(itemname.E6RB_UNLOCK) | OpenRounds)))
Episode7Round1Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 49)
                         | RandRound & Has(itemname.E7R1_UNLOCK) | OpenRounds)
Episode7Round2Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 50)
                        | RandRound & Has(itemname.E7R2_UNLOCK) | OpenRounds)
Episode7Round3Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 51)
                        | RandRound & Has(itemname.E7R3_UNLOCK) | OpenRounds)
Episode7Round4Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 52)
                        | RandRound & Has(itemname.E7R4_UNLOCK) | OpenRounds)
Episode7Round5Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 53)
                        | RandRound & Has(itemname.E7R5_UNLOCK) | OpenRounds)
Episode7Round6Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 54)
                        | RandRound & Has(itemname.E7R6_UNLOCK) | OpenRounds)
Episode7Round7Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 55)
                         | RandRound & Has(itemname.E7R7_UNLOCK) | OpenRounds)
Episode7RoundBAcc: Rule[Any] = ((CanReachLocation(E7R1Par_Location, parent_region_name=regname.E7) &
                               CanReachLocation(E7R2Par_Location, parent_region_name=regname.E7) &
                               CanReachLocation(E7R3Par_Location, parent_region_name=regname.E7) &
                               CanReachLocation(E7R4Par_Location, parent_region_name=regname.E7) &
                               CanReachLocation(E7R5Par_Location, parent_region_name=regname.E7) &
                               CanReachLocation(E7R6Par_Location, parent_region_name=regname.E7) &
                               CanReachLocation(E7R7Par_Location, parent_region_name=regname.E7)) &
                               ((ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 56)) |
                               (RandRound & Has(itemname.E7RB_UNLOCK) | OpenRounds)))
ShuffleMoves: Rule[Any] = True_() & OptionFilter(bey_opt.ShuffleMoves, 1) ##todo

oveRandoOff: Rule[Any] = True_() & OptionFilter(bey_opt.ShuffleMoves, 0)
CanBoost: Rule[Any] = MoveRandoOff | OptionFilter(bey_opt.ShuffleMoves, 1) & Has(itemname.BOOST_UPGRADE)