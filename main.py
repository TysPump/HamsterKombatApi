import asyncio
import time

"""
Example of usage

"""

from src import HamsterApiRequests

def get_timestamp():
    current_timestamp_seconds = time.time()
    return int(current_timestamp_seconds * 1000)

async def main():
    client = HamsterApiRequests()

    await client.complete_daily_task() # Получение доступной ежедневной награды

    await client.buy_update(upgradeId="oracle", timestamp=get_timestamp()) # покупка карточки по ID

    await client.tap(taps_count=8000, availableTaps=8000, timestamp=get_timestamp()) # использование сразу всех доступных нажатий

    cipher = await client.get_cipher(word="BIP") # получение ежедневного шифра
    if not cipher.error:
        print(cipher.bonusCoins)

    cards = await client.get_upgrades() # получаем все доступные к покупке карточки
    print(cards.upgradesForBuy)


if __name__ in "__main__":
    asyncio.run(main())
