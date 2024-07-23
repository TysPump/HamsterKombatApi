from . import BaseModel, Dict, Any, List

class Upgrades(BaseModel):
    upgradesForBuy: List[Dict[str, Any]]
    sections: List[Dict[str, Any]]
    dailyCombo: Dict[str, Any]