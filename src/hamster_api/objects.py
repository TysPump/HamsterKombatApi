from pydantic import BaseModel
from typing import Optional


class DailyCipher(BaseModel):
    error: Optional[str] = None
    bonusCoins: Optional[int] = None
    isClaimed: Optional[bool] = None
    remainSeconds: Optional[int] = None