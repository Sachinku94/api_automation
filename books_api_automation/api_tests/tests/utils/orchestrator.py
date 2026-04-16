class OrderOrchestrator:

    def __init__(self, api_client, headers):
        self.api_client = api_client
        self.headers = headers

    def get_book_id(self):
        res = self.api_client.get("/books")
        return res.json()[0]["id"]

    def create_order(self, book_id):
        payload = {
            "bookId": book_id,
            "customerName": "Sachin"
        }
        res = self.api_client.post("/orders", payload, self.headers)
        return res.json()["orderId"]

    def update_order(self, order_id):
        payload = {"customerName": "Updated"}
        return self.api_client.patch(f"/orders/{order_id}", payload, self.headers)

    def delete_order(self, order_id):
        return self.api_client.delete(f"/orders/{order_id}", self.headers)