import asyncio
import aiohttp

url = "http://localhost:8000/api"
backup_url = "http://localhost:8000/backup"

import json
import sys

from json_data import (

    authenticated_json,
    basic_json,
    request_backup_json
)

class ALA():

    def __init__(self):

        pass

    async def print_backup_data(self):

        async with aiohttp.ClientSession() as session:

            async with session.post(backup_url, json = request_backup_json, headers = {"Content-Type": "application/json"}) as response:

                response_data = await response.json()

                if response.status != 200:

                    print(f"Server answer bad: {response.status}")

                else:

                    print(json.dumps(response_data, indent = 4))
                    print("\nFinished... Exit")
                    sys.exit(1)


    async def post_request(self):

        async with aiohttp.ClientSession() as session:

            async with session.post(url, json = authenticated_json, headers = {"Content-Type": "application/json"}) as response:

                #response_data = await response.json()

                if response.status != 200:

                    print(f"Server answer bad: {response.status}")

                else:

                    print("Success")

    async def get_request(self):

        async with aiohttp.ClientSession() as session:

            async with session.get(url) as response:

                print(f"GET-Response: {await response.text()}")

    async def ala(self):

        while True:

            try:

                #await self.post_request()

                await self.print_backup_data()

            except Exception as network_error:

                print(network_error)

            await asyncio.sleep(5)

    def run(self):

        asyncio.run(self.ala())

if __name__ == "__main__":

    ala = ALA()

    ala.run()
