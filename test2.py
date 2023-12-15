import asyncio
import requests
import time
import random


def test(index: int):
    # delay
    time.sleep(random.randint(1, 4)) # random
    data = requests.get("https://www.google.com")
    # data = requests.get("http://localhost:3000/api/...")
    print(f"[ {index} ]", data)


async def main():
    for i in range(3):
        loop.run_in_executor(None, test, i)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# python-dotenv


# import asyncio
# import requests
#
# async def main():
#     loop = asyncio.get_event_loop()
#     future1 = loop.run_in_executor(None, requests.get, 'http://www.google.com')
#     future2 = loop.run_in_executor(None, requests.get, 'http://www.google.co.uk')
#     response1 = await future1
#     response2 = await future2
#     print(response1.text)
#     print(response2.text)
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())