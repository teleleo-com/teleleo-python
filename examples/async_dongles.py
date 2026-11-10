"""Fetch the details of every modem concurrently with the async client.

export TELELEO_API_KEY=...
python examples/async_dongles.py
"""

import asyncio

from teleleo import AsyncTeleleo


async def main() -> None:
    async with AsyncTeleleo() as client:
        page = await client.dongles.list(is_short=True)
        dongles = await asyncio.gather(*(client.dongles.get(d.dongle_id) for d in page.items))
        for dongle in dongles:
            print(dongle.dongle_id, dongle.name, dongle.dongle_online_status)


asyncio.run(main())
