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
Episode1Round1Acc: Rule[Any] = (ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK)
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
Episode1RoundBAcc: Rule[Any] = ((CanReachLocation(locname.E1R1_PAR_TIME, parent_region_name=regname.E1R1) &
                               CanReachLocation(locname.E1R2_PAR_TIME, parent_region_name=regname.E1R2) &
                               CanReachLocation(locname.E1R3_PAR_TIME, parent_region_name=regname.E1R3) &
                               CanReachLocation(locname.E1R4_PAR_TIME, parent_region_name=regname.E1R4) &
                               CanReachLocation(locname.E1R5_PAR_TIME, parent_region_name=regname.E1R5) &
                               CanReachLocation(locname.E1R6_PAR_TIME, parent_region_name=regname.E1R6) &
                               CanReachLocation(locname.E1R7_PAR_TIME, parent_region_name=regname.E1R7)) &
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
Episode2RoundBAcc: Rule[Any] = ((CanReachLocation(locname.E2R1_PAR_TIME, parent_region_name=regname.E2R1) &
                               CanReachLocation(locname.E2R2_PAR_TIME, parent_region_name=regname.E2R2) &
                               CanReachLocation(locname.E2R3_PAR_TIME, parent_region_name=regname.E2R3) &
                               CanReachLocation(locname.E2R4_PAR_TIME, parent_region_name=regname.E2R4) &
                               CanReachLocation(locname.E2R5_PAR_TIME, parent_region_name=regname.E2R5) &
                               CanReachLocation(locname.E2R6_PAR_TIME, parent_region_name=regname.E2R6) &
                               CanReachLocation(locname.E2R7_PAR_TIME, parent_region_name=regname.E2R7)) &
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
Episode3RoundBAcc: Rule[Any] = ((CanReachLocation(locname.E3R1_PAR_TIME, parent_region_name=regname.E3R1) &
                               CanReachLocation(locname.E3R2_PAR_TIME, parent_region_name=regname.E3R2) &
                               CanReachLocation(locname.E3R3_PAR_TIME, parent_region_name=regname.E3R3) &
                               CanReachLocation(locname.E3R4_PAR_TIME, parent_region_name=regname.E3R4) &
                               CanReachLocation(locname.E3R5_PAR_TIME, parent_region_name=regname.E3R5) &
                               CanReachLocation(locname.E3R6_PAR_TIME, parent_region_name=regname.E3R6) &
                               CanReachLocation(locname.E3R7_PAR_TIME, parent_region_name=regname.E3R7)) &
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
Episode4RoundBAcc: Rule[Any] = ((CanReachLocation(locname.E4R1_PAR_TIME, parent_region_name=regname.E4R1) &
                               CanReachLocation(locname.E4R2_PAR_TIME, parent_region_name=regname.E4R2) &
                               CanReachLocation(locname.E4R3_PAR_TIME, parent_region_name=regname.E4R3) &
                               CanReachLocation(locname.E4R4_PAR_TIME, parent_region_name=regname.E4R4) &
                               CanReachLocation(locname.E4R5_PAR_TIME, parent_region_name=regname.E4R5) &
                               CanReachLocation(locname.E4R6_PAR_TIME, parent_region_name=regname.E4R6) &
                               CanReachLocation(locname.E4R7_PAR_TIME, parent_region_name=regname.E4R7)) &
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
Episode5RoundBAcc: Rule[Any] = ((CanReachLocation(locname.E5R1_PAR_TIME, parent_region_name=regname.E5R1) &
                               CanReachLocation(locname.E5R2_PAR_TIME, parent_region_name=regname.E5R2) &
                               CanReachLocation(locname.E5R3_PAR_TIME, parent_region_name=regname.E5R3) &
                               CanReachLocation(locname.E5R4_PAR_TIME, parent_region_name=regname.E5R4) &
                               CanReachLocation(locname.E5R5_PAR_TIME, parent_region_name=regname.E5R5) &
                               CanReachLocation(locname.E5R6_PAR_TIME, parent_region_name=regname.E5R6) &
                               CanReachLocation(locname.E5R7_PAR_TIME, parent_region_name=regname.E5R7)) &
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
Episode6RoundBAcc: Rule[Any] = ((CanReachLocation(locname.E6R1_PAR_TIME, parent_region_name=regname.E6R1) &
                               CanReachLocation(locname.E6R2_PAR_TIME, parent_region_name=regname.E6R2) &
                               CanReachLocation(locname.E6R3_PAR_TIME, parent_region_name=regname.E6R3) &
                               CanReachLocation(locname.E6R4_PAR_TIME, parent_region_name=regname.E6R4) &
                               CanReachLocation(locname.E6R5_PAR_TIME, parent_region_name=regname.E6R5) &
                               CanReachLocation(locname.E6R6_PAR_TIME, parent_region_name=regname.E6R6) &
                               CanReachLocation(locname.E6R7_PAR_TIME, parent_region_name=regname.E6R7)) &
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
Episode7RoundBAcc: Rule[Any] = ((CanReachLocation(locname.E7R1_PAR_TIME, parent_region_name=regname.E7R1) &
                               CanReachLocation(locname.E7R2_PAR_TIME, parent_region_name=regname.E7R2) &
                               CanReachLocation(locname.E7R3_PAR_TIME, parent_region_name=regname.E7R3) &
                               CanReachLocation(locname.E7R4_PAR_TIME, parent_region_name=regname.E7R4) &
                               CanReachLocation(locname.E7R5_PAR_TIME, parent_region_name=regname.E7R5) &
                               CanReachLocation(locname.E7R6_PAR_TIME, parent_region_name=regname.E7R6) &
                               CanReachLocation(locname.E7R7_PAR_TIME, parent_region_name=regname.E7R7)) &
                               ((ProgRound & Has(itemname.PROGRESSIVE_ROUND_UNLOCK, 56)) |
                               (RandRound & Has(itemname.E7RB_UNLOCK) | OpenRounds)))
MoveRandoOff: Rule[Any] = True_() & OptionFilter(bey_opt.ShuffleMoves, 0)
CanBoost: Rule[Any] = MoveRandoOff | OptionFilter(bey_opt.ShuffleMoves, 1) & Has(itemname.BOOST_UPGRADE)
CanBrake: Rule[Any] = MoveRandoOff | OptionFilter(bey_opt.ShuffleMoves, 1) & Has(itemname.BRAKE_UPGRADE)
CanUltimate: Rule[Any] = MoveRandoOff | OptionFilter(bey_opt.ShuffleMoves, 1) & Has(itemname.ULTIMATE_UPGRADE)
ProgressiveStaminaOff: Rule[Any] = True_() & OptionFilter(bey_opt.ProgressiveStaminaUnlocks, 0)
NeedsRedStaminaBar: Rule[Any] = ProgressiveStaminaOff | (OptionFilter(bey_opt.ProgressiveStaminaUnlocks, 1) &
                                                         Has(itemname.PROGRESSIVE_STAMINA_UPGRADE, 1))
NeedsOrangeStaminaBar: Rule[Any] = ProgressiveStaminaOff | (OptionFilter(bey_opt.ProgressiveStaminaUnlocks, 1) &
                                                         Has(itemname.PROGRESSIVE_STAMINA_UPGRADE, 2))
NeedsYellowStaminaBar: Rule[Any] = ProgressiveStaminaOff | (OptionFilter(bey_opt.ProgressiveStaminaUnlocks, 1) &
                                                         Has(itemname.PROGRESSIVE_STAMINA_UPGRADE, 3))
NeedsWhiteStaminaBar: Rule[Any] = ProgressiveStaminaOff | (OptionFilter(bey_opt.ProgressiveStaminaUnlocks, 1) &
                                                         Has(itemname.PROGRESSIVE_STAMINA_UPGRADE, 4))
PadShuffleOff: Rule[Any] = True_() & OptionFilter(bey_opt.ShufflePads, 0)
CanJumpPad: Rule[Any] = MoveRandoOff | OptionFilter(bey_opt.ShufflePads, 1) & Has(itemname.JUMP_PAD_UNLOCK)
CanBoostPad: Rule[Any] = MoveRandoOff | OptionFilter(bey_opt.ShufflePads, 1) & Has(itemname.BOOST_PAD_UNLOCK)
CanRechargePad: Rule[Any] = MoveRandoOff | OptionFilter(bey_opt.ShufflePads, 1) & Has(itemname.RECHARGE_PAD_UNLOCK)
