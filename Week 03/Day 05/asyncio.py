# Source
#  https://docs.python.org/3/library/asyncio.html


import asyncio
import requests
import aiohttp
from program_timer import timer
from concurrent.futures import ThreadPoolExecutor

URL = 'https://httpbin.org/uuid'

async def fetch_uuid(Session, url):
   async with Session .get(url) as response:
    json_data = await response.json()
    print(response.json()['uuid'])

async def func():
  async with aiohttp.ClientSession() as session:
    task = await [fetch_uuid(session, URL) for _ in range(100)]
    await asyncio.gather(*tasks)


@timer(1, 1)
def main():
  asyncio.run(func())
