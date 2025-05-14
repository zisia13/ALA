import asyncio
import aiohttp

url = "http://localhost:8000/api"

json_data_1 = {

    "command" : "data",

    "data": {

        "message" : "Helu",
    },

    "login" : {

        "username" : "testusername",
        "password" : "testpassword",
    },

    "authorization" : {

        "channel_id" : "testchannel",
        "key" : "testkey"
    }
}

json_data_2 = {

    "command" : "data",

    "data": {

        "message" : "Helu",
    },

    "login" : {

        "username" : "testusername",
        "password" : "testpassword",
    }
}

async def post_request():

    async with aiohttp.ClientSession() as session:

        async with session.post(url, json = json_data_2, headers = {"Content-Type": "application/json"}) as response:

            #response_data = await response.json()
            
            if response.status != 200:

                print(f"Server answer bad: {response.status}")

            else:

                print("Success")

async def get_request():

    async with aiohttp.ClientSession() as session:

        async with session.get(url) as response:

            print(f"GET-Response: {await response.text()}")

async def ala():

    while True:

        await post_request()

        await asyncio.sleep(5)

#! start main loop
asyncio.run(ala())



"""
async def ping_url(url, interval):
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    print(f"{url} → Status: {response.status}")
        except Exception as e:
            print(f"{url} → Fehler: {e}")
        await asyncio.sleep(interval)

async def main():
    tasks = [
        ping_url("https://www.google.com", 10),
        ping_url("https://www.github.com", 5),
    ]
    await asyncio.gather(*tasks)  # Führe beide Loops parallel aus

asyncio.run(main())
"""
