from src.utils import TOKEN
from src.requests.sessions import SessionRequests
from src.hamster_api.objects import DailyCipher, Upgrades

from typing import Any

class HamsterApiRequests(SessionRequests):
    def __init__(self) -> None:
        super().__init__()

        self.end_point = "https://api.hamsterkombatgame.io/{}"
        
        self.headers = {"Authorization": f"Bearer {TOKEN}"}

    async def complete_daily_task(self) -> dict:
        "Receives a daily reward"
        result = await self.post(
            url=self.end_point.format("clicker/check-task"),
            headers=self.headers,
            json={"taskId": "streak_days"}
        )

        return result

    async def buy_update(self, upgradeId: str, timestamp: int) -> dict:
        "Buy card by ID"
        result = await self.post(
            url=self.end_point.format("clicker/buy-upgrade"),
            headers=self.headers,
            json={upgradeId: upgradeId, timestamp: timestamp}
        )

        return result
    
    async def tap(self, taps_count: int, availableTaps: int, timestamp: int) -> dict:
        "Tap action"
        result = await self.post(
            url=self.end_point.format("clicker/tap"),
            headers=self.headers,
            json={"count": taps_count, "availableTaps": availableTaps, "timestamp": timestamp}
        )

        return result

    async def get_cipher(self, word: str) -> DailyCipher:
        result: dict[str, Any] = await self.post(
            url=self.end_point.format("clicker/claim-daily-cipher"),
            headers=self.headers,
            json={"cipher": word}
        )

        return DailyCipher.mixed_dict(data=result)

    async def get_upgrades(self) -> Upgrades:
        result: dict[str, Any] = await self.post(
            url=self.end_point.format("clicker/upgrades-for-buy"),
            headers=self.headers
        )

        return Upgrades(**result)
        
    async def get_referrals(self) -> list[dict, Any]:
        result: dict[list, Any] = await self.post(
            url=self.end_point.format("clicker/referral-stat"),
            headers=self.headers
        )

        return result["stats"]
    
    async def change_exchange(self, exchangeId: str) -> None:
        await self.post(
            url=self.end_point.format("clicker/select-exchange"),
            headers=self.headers,
            json={"exchangeId": exchangeId}
        )
