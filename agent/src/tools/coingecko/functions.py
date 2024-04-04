from config import Config
from api import CoinGeckoAPI

class CoinGeckoFunctions:
    def __init__(self):
        self.config = Config()
        self.coin_gecko_api = CoinGeckoAPI()

    def get_coin_market_cap(self, coin_name):
        """Get the market cap of a coin."""
        try:
            market_cap = self.coin_gecko_api.get_market_cap(coin_name)
            if market_cap is None:
                return self.config.MARKET_CAP_FAILURE_MESSAGE
            return self.config.MARKET_CAP_SUCCESS_MESSAGE.format(coin_name=coin_name, market_cap=market_cap)
        except requests.exceptions.RequestException:
            return self.config.API_ERROR_MESSAGE

    def get_fully_diluted_valuation(self, coin_name):
        """Get the fully diluted valuation of a coin."""
        try:
            fdv = self.coin_gecko_api.get_fdv(coin_name)
            if fdv is None:
                return self.config.FDV_FAILURE_MESSAGE
            return self.config.FDV_SUCCESS_MESSAGE.format(coin_name=coin_name, fdv=fdv)
        except requests.exceptions.RequestException:
            return self.config.API_ERROR_MESSAGE

    def get_coin_price(self, coin_name):
        """Get the price of a cryptocurrency."""
        try:
            price = self.coin_gecko_api.get_price(coin_name)
            if price is None:
                return self.config.PRICE_FAILURE_MESSAGE
            return self.config.PRICE_SUCCESS_MESSAGE.format(coin_name=coin_name, price=price)
        except requests.exceptions.RequestException:
            return self.config.API_ERROR_MESSAGE
