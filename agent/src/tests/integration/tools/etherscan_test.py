import pytest
from src.tools.etherscan import EtherscanAPI

@pytest.fixture
def etherscan_api():
    """Fixture to instantiate the EtherscanAPI class."""
    return EtherscanAPI()

def test_get_ether_balance(etherscan_api):
    address = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe"  # Example Ethereum address
    balance = etherscan_api.get_ether_balance(address)
    assert balance is not None, "Balance should not be None"
    assert isinstance(balance, float), "Balance should be a float"

def test_get_contract_execution_status(etherscan_api):
    transaction_hash = "0x00"  # Example transaction hash
    status = etherscan_api.get_contract_execution_status(transaction_hash)
    assert status is not None, "Status should not be None"
    assert isinstance(status, bool), "Status should be a boolean"

def test_get_transaction_receipt_status(etherscan_api):
    transaction_hash = "0x00"  # Example transaction hash
    status = etherscan_api.get_transaction_receipt_status(transaction_hash)
    assert status is not None, "Status should not be None"
    assert isinstance(status, bool), "Status should be a boolean"

def test_get_erc20_token_supply(etherscan_api):
    contract_address = "0x00"  # Example contract address
    supply = etherscan_api.get_erc20_token_supply(contract_address)
    assert supply is not None, "Supply should not be None"
    assert isinstance(supply, int), "Supply should be an integer"

def test_get_confirmation_time_estimate(etherscan_api):
    confirmation_time_estimate = etherscan_api.get_confirmation_time_estimate()
    assert confirmation_time_estimate is not None, "Confirmation time estimate should not be None"
    assert isinstance(confirmation_time_estimate, int), "Confirmation time estimate should be an integer"
