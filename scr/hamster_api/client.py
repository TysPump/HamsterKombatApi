from scr.utils import TOKEN
from scr.requests.sessions import SessionRequests

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

