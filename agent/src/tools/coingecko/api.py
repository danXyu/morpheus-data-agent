import requests
import logging
from langchain.pydantic_v1 import BaseModel, Field
from langchain.agents import Tool
from typing import Optional
from .config import Config

class CoinGeckoAPI:
    def __init__(self):
        self.base_url = Config.COINGECKO_BASE_URL
        self.config = Config()

    def get_coingecko_id(self, text: str, type: str = "coin") -> Optional[str]:
        """Get the CoinGecko ID for a given coin or NFT."""
        url = f"{self.base_url}/search"
        params = {"query": text}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            if type == "coin":
                return data['coins'][0]['id'] if data['coins'] else None
            elif type == "nft":
                return data['nfts'][0]['id'] if data.get('nfts') else None
            else:
                raise ValueError("Invalid type specified")
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {str(e)}")
            raise

    def get_price(self, coin: str) -> Optional[float]:
        """Get the price of a coin from CoinGecko API."""
        coin_id = self.get_coingecko_id(coin, type="coin")
        if not coin_id:
            return None
        url = f"{self.base_url}/simple/price"
        params = {'ids': coin_id, 'vs_currencies': 'USD'}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()[coin_id]['usd']
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to retrieve price: {str(e)}")
            raise

    def get_floor_price(self, nft: str) -> Optional[float]:
        """Get the floor price of an NFT from CoinGecko API."""
        nft_id = self.get_coingecko_id(str(nft), type="nft")
        if not nft_id:
            return None
        url = f"{self.base_url}/nfts/{nft_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()["floor_price"]["usd"]
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to retrieve floor price: {str(e)}")
            raise

    def get_fdv(self, coin: str) -> Optional[float]:
        """Get the fully diluted valuation of a coin from CoinGecko API."""
        coin_id = self.get_coingecko_id(coin, type="coin")
        if not coin_id:
            return None
        url = f"{self.base_url}/coins/{coin_id}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get("market_data", {}).get("fully_diluted_valuation", {}).get("usd")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to retrieve FDV: {str(e)}")
            raise

    def get_market_cap(self, coin: str) -> Optional[float]:
        """Get the market cap of a coin from CoinGecko API."""
        coin_id = self.get_coingecko_id(coin, type="coin")
        if not coin_id:
            return None
        url = f"{self.base_url}/coins/markets"
        params = {'ids': coin_id, 'vs_currency': 'USD'}
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()[0]['market_cap']
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to retrieve market cap: {str(e)}")
            raise

    def get_price_spark_chart(self, coin: str, days: int = 60, height: int = 10, width: int = 60) -> None:
        """Get the price spark chart of a coin from CoinGecko API."""
        coin_id = self.get_coingecko_id(coin, type="coin")
        if not coin_id:
            return None
        url = f"{self.base_url}/coins/{coin_id}/market_chart?vs_currency=usd&days={days}"
        try:
            response = requests.get(url)
            response.raise_for_status()

            if response.status_code == 200:
                data = response.json()
                prices = [price[1] for price in data["prices"]]
                min_price = min(prices)
                max_price = max(prices)
                normalized_prices = [int((price - min_price) / (max_price - min_price) * height) for price in prices]
                step = len(prices) // width
                reduced_prices = normalized_prices[::step]
                chart = f"{coin_id.capitalize()} Price Spark Chart (Last {days} Days)\n\n"
                for i in range(height, -1, -1):
                    row = ""
                    for price in reduced_prices:
                        if price >= i:
                            row += "█"
                        else:
                            row += " "
                    chart += row + "\n"
                return chart
            else:
                print("Failed to fetch price data from the CoinGecko API.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to retrieve price spark chart: {str(e)}")
            raise

