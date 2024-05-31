from fastapi import FastAPI, Request, HTTPException
from starlette.responses import JSONResponse
from order_manager import OrderManager

order_manager = OrderManager()

def client_app():
    app = FastAPI()

    @app.post("/order/")
    async def order(request: Request):
        client_ip = request.client.host
        try:
            order_id = order_manager.create_order(client_ip)
            return JSONResponse(content={"order_id": order_id}, status_code=200)
        except HTTPException as e:
            raise e

    return app
