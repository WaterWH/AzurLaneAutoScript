from module.campaign.campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger
from .sp1 import Config as ConfigBase

MAP = CampaignMap('SP2')
MAP.shape = 'K6'
MAP.camera_data = ['D2', 'D4', 'H2', 'H4']
MAP.camera_data_spawn_point = ['D4']
MAP.map_data = """
    -- -- ++ ++ -- Me -- ++ ++ ME --
    Me ME ++ ++ ME -- ME -- ME -- ME
    -- -- MB -- MB -- -- -- -- -- --
    ++ -- -- MB -- __ Me ++ ++ ME ++
    SP -- Me -- ME -- -- ++ ME -- ME
    SP SP ++ ++ ++ ME -- -- -- -- ME
"""
MAP.weight_data = """
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
    50 50 50 50 50 50 50 50 50 50 50
"""
MAP.spawn_data = [
    {'battle': 0, 'enemy': 2, 'siren': 2},
    {'battle': 1, 'enemy': 2},
    {'battle': 2, 'enemy': 1},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'boss': 1},
]
A1, B1, C1, D1, E1, F1, G1, H1, I1, J1, K1, \
A2, B2, C2, D2, E2, F2, G2, H2, I2, J2, K2, \
A3, B3, C3, D3, E3, F3, G3, H3, I3, J3, K3, \
A4, B4, C4, D4, E4, F4, G4, H4, I4, J4, K4, \
A5, B5, C5, D5, E5, F5, G5, H5, I5, J5, K5, \
A6, B6, C6, D6, E6, F6, G6, H6, I6, J6, K6, \
    = MAP.flatten()


class Config(ConfigBase):
    # ===== Start of generated config =====
    MAP_HAS_MAP_STORY = False
    MAP_HAS_FLEET_STEP = False
    MAP_HAS_AMBUSH = False
    # ===== End of generated config =====


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        return self.battle_default()

    def battle_4(self):
        return self.clear_boss()
