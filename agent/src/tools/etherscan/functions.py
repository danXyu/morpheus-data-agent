from .config import Config
from .api import EtherscanAPI

class EtherscanFunctions:
    def __init__(self):
        self.config = Config()
        self.etherscan_api = EtherscanAPI()

    def get_ether_balance(self, address):
        """Retrieves the Ether balance of a given address."""
        try:
            balance = self.etherscan_api.get_eth_balance(address)
            if balance is None:
                return Config.BALANCE_FAILURE_MESSAGE
            return Config.BALANCE_SUCCESS_MESSAGE.format(address=address, balance=balance)
        except requests.exceptions.RequestException:
            return Config.API_ERROR_MESSAGE

    def get_contract_execution_status(self, tx_hash):
        """Gets the execution status of a contract."""
        try:
            status = self.etherscan_api.get_contract_execution_status(tx_hash)
            if status is None:
                return Config.CONTRACT_STATUS_FAILURE_MESSAGE
            return Config.CONTRACT_STATUS_SUCCESS_MESSAGE.format(tx_hash=tx_hash, status=status)
        except requests.exceptions.RequestException:
            return Config.API_ERROR_MESSAGE

    def get_transaction_receipt_status(self, tx_hash):
        """Gets the status of a transaction receipt."""
        try:
            status = self.etherscan_api.get_transaction_receipt_status(tx_hash)
            if status is None:
                return Config.RECEIPT_STATUS_FAILURE_MESSAGE
            return Config.RECEIPT_STATUS_SUCCESS_MESSAGE.format(tx_hash=tx_hash, status=status)
        except requests.exceptions.RequestException:
            return Config.API_ERROR_MESSAGE

    def get_erc20_token_supply(self, contract_address):
        """Retrieves the total supply of an ERC20 token."""
        try:
            supply = self.etherscan_api.get_erc20_token_supply(contract_address)
            if supply is None:
                return Config.SUPPLY_FAILURE_MESSAGE
            return Config.SUPPLY_SUCCESS_MESSAGE.format(contract_address=contract_address, supply=supply)
        except requests.exceptions.RequestException:
            return Config.API_ERROR_MESSAGE

    def get_confirmation_time_estimate(self, tx_hash):
        """Estimates the confirmation time of a transaction."""
        try:
            estimate = self.etherscan_api.get_confirmation_time_estimate(tx_hash)
            if estimate is None:
                return Config.CONFIRMATION_ESTIMATE_FAILURE_MESSAGE
            return Config.CONFIRMATION_ESTIMATE_SUCCESS_MESSAGE.format(tx_hash=tx_hash, estimate=estimate)
        except requests.exceptions.RequestException:
            return Config.API_ERROR_MESSAGE
