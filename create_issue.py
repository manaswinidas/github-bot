import asyncio
import os
import aiohttp

from gidgethub.aiohttp import GitHubAPI

async def main():
    async with aiohttp.ClientSession() as session:
        gh=GitHubAPI(session, "manaswinidas", 
                     oauth_token=os.getenv("GH_AUTH"))
        await gh.patch('/repos/manaswinidas/Memeapp/issues/29', 
                      data={'state' :"closed"})

asyncio.run(main())
