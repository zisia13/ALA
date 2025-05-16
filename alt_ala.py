import asyncio, aiohttp

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