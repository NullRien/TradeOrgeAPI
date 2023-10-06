import httpx

class TradeOgreAPI:
    def __init__(self, api_key: str, api_secret: str):
        self.base_url = "https://tradeogre.com/api/v1"
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = httpx.Client()

    # Public Endpoints
    def get_markets(self) -> dict:
        url = f"{self.base_url}/markets"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_order_book(self, market: str) -> dict:
        url = f"{self.base_url}/orders/{market}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_ticker(self, market: str) -> dict:
        url = f"{self.base_url}/ticker/{market}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_trade_history(self, market: str) -> dict:
        url = f"{self.base_url}/history/{market}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    # Private Endpoints
    def get_balance(self, currency: str) -> dict:
        url = f"{self.base_url}/account/balance"
        headers = {"currency": currency}
        response = self.session.post(url, headers=headers, auth=(self.api_key, self.api_secret))
        response.raise_for_status()
        return response.json()
        
    def get_balances(self) -> dict:
        url = f"{self.base_url}/account/balances"
        response = self.session.get(url, auth=(self.api_key, self.api_secret))
        response.raise_for_status()
        return response.json()

    def get_order(self, uuid: str) -> dict:
        url = f"{self.base_url}/account/order"
        headers = {"uuid": uuid}
        response = self.session.post(url, headers=headers, auth=(self.api_key, self.api_secret))
        response.raise_for_status()
        return response.json()

    def get_orders(self, market: str) -> dict:
        url = f"{self.base_url}/account/orders"
        headers = {"market": market}
        response = self.session.get(url, headers=headers, auth=(self.api_key, self.api_secret))
        response.raise_for_status()
        return response.json()

    def buy(self, market: str, quantity: str, price: str) -> dict:
        print("Starting buy order")
        url = f"{self.base_url}/order/buy"
        data = {
            "market": market,
            "quantity": quantity,  # Note: Changed "Quantity" to "quantity" for consistency
            "price": price
        }
        response = self.session.post(url, data=data, auth=(self.api_key, self.api_secret))
        print(response.json())
        input("Ending buy order")
        response.raise_for_status()
        return response.json()

    def sell(self, market: str, quantity: float, price: float) -> dict:
        url = f"{self.base_url}/order/sell"
        data = {
            "market": market,
            "quantity": str(quantity),
            "price": str(price)
        }
        response = self.session.post(url, data=data, auth=(self.api_key, self.api_secret))
        response.raise_for_status()
        return response.json()

    def cancel_order(self, uuid: str) -> dict:
        url = f"{self.base_url}/order/cancel"
        data = {"uuid": uuid}
        response = self.session.post(url, data=data, auth=(self.api_key, self.api_secret))
        response.raise_for_status()
        return response.json()

    def __del__(self):
        self.session.close()

