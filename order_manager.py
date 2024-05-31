from collections import deque
from fastapi import HTTPException

class OrderManager:
    def __init__(self):
        self.pending_orders = deque()
        self.in_progress_order = None
        self.completed_orders = {}
        self.delusional_client = {}
        self.MAX_DELUSIONAL_ORDERS = 100

    def create_order(self, client_ip):
        if self.delusional_client.get(client_ip, 0) > self.MAX_DELUSIONAL_ORDERS:
            raise HTTPException(status_code=429, detail="Too many requests from this client.")
        
        order_id = len(self.pending_orders) + 1 + (self.in_progress_order or 0)
        self.pending_orders.append(order_id)
        self.delusional_client[client_ip] = self.delusional_client.get(client_ip, 0) + 1
        return order_id

    def start_order(self):
        if not self.pending_orders:
            return None
        self.in_progress_order = self.pending_orders.popleft()
        return self.in_progress_order

    def finish_order(self):
        if not self.in_progress_order:
            return None
        completed_order = self.in_progress_order
        self.in_progress_order = None
        self.completed_orders[completed_order] = "completed"
        return completed_order
