from fastapi import FastAPI, HTTPException
from order_manager import OrderManager
import asyncio
import random

order_manager = OrderManager()

def barista_app():
    app = FastAPI()

    @app.post("/start/")
    async def start_order():
        order_id = order_manager.start_order()
        if order_id:
            return {"message": f"Order {order_id} started."}
        else:
            raise HTTPException(status_code=404, detail="No pending orders.")

    @app.post("/finish/")
    async def finish_order():
        order_id = order_manager.finish_order()
        if order_id:
            await asyncio.sleep(random.randint(30, 60))
            return {"message": f"Order {order_id} finished."}
        else:
            raise HTTPException(status_code=404, detail="No orders in progress.")

    return app
