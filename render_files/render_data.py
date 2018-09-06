from enum import Enum, auto
from typing import Dict, List


class IconDisplay(Enum):
    ICON, DIRECTION, JOB = range(3)


class Font(Enum):
    ARIAL = auto()
    COURIER = auto()
    CELTIC_GARAMOND = auto()
    CAELDERA = auto()
    CONSOLAS = auto()
    DEJAVU_WIDE = auto()
    DEJAVU = auto()
    DUNDALK = auto()
    LUCIDA = auto()
    PRESTIGE = auto()
    TERMINAL = auto()


GAME_FONTS: Dict[Font, List[str]] = {Font.ARIAL: ["arial8x8.png", "arial10x10.png", "arial12x12.png"],
                                     Font.COURIER: ["courier8x8_aa_tc.png", "courier10x10_aa_tc.png",
                                                    "courier12x12_aa_tc.png"],
                                     Font.CELTIC_GARAMOND: ["celtic_garamond_10x10_gs_tc.png"],
                                     Font.CAELDERA: ["caeldera8x8_gs_tc.png"],
                                     Font.CONSOLAS: ["consolas8x8_gs_tc.png", "consolas10x10_gs_tc.png",
                                                     "consolas12x12_gs_tc.png"],
                                     Font.DEJAVU_WIDE: ["dejavu_wide12x12_gs_tc.png", "dejavu_wide16x16_gs_tc.png"],
                                     Font.DEJAVU: ["dejavu8x8_gs_tc.png", "dejavu10x10_gs_tc.png",
                                                   "dejavu12x12_gs_tc.png", "dejavu16x16_gs_tc.png"],
                                     Font.DUNDALK: ["dundalk12x12_gs_tc.png"],
                                     Font.LUCIDA: ["lucida8x8_gs_tc.png", "lucida10x10_gs_tc.png",
                                                   "lucida12x12_gs_tc.png"],
                                     Font.PRESTIGE: ["prestige8x8_gs_tc.png", "prestige10x10_gs_tc.png",
                                                     "prestige12x12_gs_tc.png"],
                                     Font.TERMINAL: ["terminal8x8_gs_tc.png", "terminal10x10_gs_tc.png"]}
