from config import Config
from api import SantimentAPI

class SantimentFunctions:
    def __init__(self):
        self.config = Config()
        self.santiment_api = SantimentAPI()

    def get_coins_with_highest_price_increase(self, limit):
        """Retrieves the coins with the highest price increase."""
        try:
            coins = self.santiment_api.get_coins_with_highest_price_increase(limit)
            if coins is None:
                return Config.COINS_WITH_HIGHEST_PRICE_INCREASE_FAILURE_MESSAGE
            return Config.COINS_WITH_HIGHEST_PRICE_INCREASE_SUCCESS_MESSAGE.format(coins=coins)
        except requests.exceptions.RequestException:
            return Config.API_ERROR_MESSAGE

    def get_trending_coins(self, limit):
        """Retrieves the trending coins."""
        try:
            coins = self.santiment_api.get_trending_coins(limit)
            if coins is None:
                return Config.TRENDING_COINS_FAILURE_MESSAGE
            return Config.TRENDING_COINS_SUCCESS_MESSAGE.format(coins=coins)
        except requests.exceptions.RequestException:
            return Config.API_ERROR_MESSAGE

    def get_highest_dev_activity(self, limit):
        """Retrieves the coins with the highest developer activity."""
        try:
            coins = self.santiment_api.get_highest_dev_activity(limit)
            if coins is None:
                return Config.HIGHEST_DEV_ACTIVITY_FAILURE_MESSAGE
            return Config.HIGHEST_DEV_ACTIVITY_SUCCESS_MESSAGE.format(coins=coins)
        except requests.exceptions.RequestException:
            return Config.API_ERROR_MESSAGE

    def get_highest_network_growth(self, limit):
        """Retrieves the coins with the highest network growth."""
        try:
            coins = self.santiment_api.get_highest_network_growth(limit)
            if coins is None:
                return Config.HIGHEST_NETWORK_GROWTH_FAILURE_MESSAGE
            return Config.HIGHEST_NETWORK_GROWTH_SUCCESS_MESSAGE.format(coins=coins)
        except requests.exceptions.RequestException:
            return Config.API_ERROR_MESSAGE

    def get_highest_token_circulation(self, limit):
        """Retrieves the coins with the highest token circulation."""
        try:
            coins = self.santiment_api.get_highest_token_circulation(limit)
            if coins is None:
                return Config.HIGHEST_TOKEN_CIRCULATION_FAILURE_MESSAGE
            return Config.HIGHEST_TOKEN_CIRCULATION_SUCCESS_MESSAGE.format(coins=coins)
        except requests.exceptions.RequestException:
            return Config.API_ERROR_MESSAGE

    def get_highest_transaction_volume(self, limit):
        """Retrieves the coins with the highest transaction volume."""
        try:
            coins = self.santiment_api.get_highest_transaction_volume(limit)
            if coins is None:
                return Config.HIGHEST_TRANSACTION_VOLUME_FAILURE_MESSAGE
            return Config.HIGHEST_TRANSACTION_VOLUME_SUCCESS_MESSAGE.format(coins=coins)
        except requests.exceptions.RequestException:
            return Config.API_ERROR_MESSAGE
