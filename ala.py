import asyncio
import aiohttp

async def myapi():

    url = "http://localhost:8000/api"
    
    async with aiohttp.ClientSession() as session:

        #! Test GET-Request
        async with session.get(url) as response:

            print(f"GET-Response: {await response.text()}")
        
        #! Test POST-Request mit JSON-Daten
        test_data = {"message": "helu"}

        async with session.post(url, json = test_data, headers = {"Content-Type": "application/json"}) as response:

            pass
            #response_data = await response.json()
            #
            #print(f"POST-Response: {response_data}")

async def ala(interval = 5):

    while True:

        await myapi()

        await asyncio.sleep(interval)

#! start main function
asyncio.run(ala())








"""
import sys, os
import asyncio, aiohttp


async def ping():

    try:

        async with aiohttp.ClientSession() as session:

            async with session.get("localhost:8000/api") as response:

                print(f"Status: {response.status}")
                
    except:

        print("error")


async def ala():

    while True:

        await ping()

        await asyncio.sleep(5)







asyncio.run(ala())
"""