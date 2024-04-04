import requests
from typing import Dict, Any
from .config import Config

class EtherscanAPI:
    """A class to interact with the Etherscan API, providing various blockchain data retrieval methods."""
    
    def __init__(self) -> None:
        """Initializes the EtherscanAPI"""
        self.api_key: str = Config.ETHERSCAN_API_KEY
        self.base_url: str = Config.ETHERSCAN_BASE_URL

    def _make_api_request(self, module: str, action: str, **kwargs: Any) -> Dict[str, Any]:
        """Constructs and sends a request to the Etherscan API and returns the JSON response."""
        url: str = f"{self.base_url}?module={module}&action={action}&apikey={self.api_key}"
        for key, value in kwargs.items():
            url += f"&{key}={value}"
        response = requests.get(url)
        data: Dict[str, Any] = response.json()
        return data

    def get_ether_balance(self, address: str) -> float:
        """Retrieves the Ether balance of a given address."""
        module: str = 'account'
        action: str = 'balance'
        tag: str = 'latest'
        response_data: Dict[str, Any] = self._make_api_request(module, action, address=address, tag=tag)
        balance_wei: int = int(response_data['result'])
        balance_ether: float = balance_wei / 10**18
        return balance_ether

    def get_contract_execution_status(self, transaction_hash: str) -> bool:
        """Checks if a contract execution resulted in an error."""
        module: str = 'transaction'
        action: str = 'getstatus'
        response_data: Dict[str, Any] = self._make_api_request(module, action, txhash=transaction_hash)
        status: str = response_data['result']['isError']
        return status == '0'

    def get_transaction_receipt_status(self, transaction_hash: str) -> bool:
        """Checks the receipt status of a transaction to see if it was successful."""
        module: str = 'transaction'
        action: str = 'gettxreceiptstatus'
        response_data: Dict[str, Any] = self._make_api_request(module, action, txhash=transaction_hash)
        status: str = response_data['result']['status']
        return status == '1'

    def get_erc20_token_supply(self, contract_address: str) -> int:
        """Retrieves the total supply of an ERC20 token given its contract address."""
        module: str = 'stats'
        action: str = 'tokensupply'
        response_data: Dict[str, Any] = self._make_api_request(module, action, contractaddress=contract_address)
        total_supply: int = int(response_data['result'])
        return total_supply

    def get_confirmation_time_estimate(self, network: str = "mainnet") -> Dict[str, Any]:
        """Estimates the confirmation time for transactions at current gas price levels."""
        module: str = 'gastracker'
        action: str = 'gasestimate'
        response_data: Dict[str, Any] = self._make_api_request(module, action)
        confirmation_time_estimate = int(response_data['result'])
        return confirmation_time_estimate
