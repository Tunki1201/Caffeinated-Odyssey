import uvicorn
from fastapi import FastAPI
import asyncio

from client_server import client_app
from barista_server import barista_app

client_app = client_app()
barista_app = barista_app()

def start_servers():
    asyncio.run(start_all())

async def start_all():
    config1 = uvicorn.Config(client_app, host="0.0.0.0", port=8000, log_level="info")
    config2 = uvicorn.Config(barista_app, host="0.0.0.0", port=8001, log_level="info")
    server1 = uvicorn.Server(config1)
    server2 = uvicorn.Server(config2)

    await asyncio.gather(server1.serve(), server2.serve())

if __name__ == "__main__":
    start_servers()
