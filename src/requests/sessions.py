import aiohttp
from typing import Optional, Any, Dict

class SessionRequests:
    def __init__(self) -> None:
        self.session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self) -> "SessionRequests":
        if not self.session:
            self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        if self.session:
            await self.session.close()
            self.session = None

    async def post(
        self, 
        url: str,
        headers: Dict[str, str],
        json: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        if not self.session:
            self.session = aiohttp.ClientSession()
        try:
            async with self.session.post(url=url, headers=headers, json=json) as response:
                response.raise_for_status()
                result = await response.json()
                return result
        except aiohttp.ClientError as e:
            return {"error": str(e)}

    async def get(
        self, 
        url: str,
        headers: Dict[str, str],
        params: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        if not self.session:
            self.session = aiohttp.ClientSession()
        try:
            async with self.session.get(url=url, headers=headers, params=params) as response:
                response.raise_for_status()
                result = await response.json()
                return result
        except aiohttp.ClientError as e:
            return {"error": str(e)}