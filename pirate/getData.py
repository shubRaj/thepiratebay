import asyncio,aiohttp
base_url = "https://api.shubraj.com/torrent/"
async def main(params):
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url,params=params) as response:
            if response.status == 200:
                data = await response.json()
                return data
if __name__=="__main__":
    print(asyncio.run(main({"query":"avengers"})))