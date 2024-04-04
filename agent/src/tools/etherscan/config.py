from dotenv import load_dotenv
import os
import logging

load_dotenv()

# Logging configuration
logging.basicConfig(level=logging.INFO)

# Configuration object
class Config:
    ETHERSCAN_API_KEY = os.getenv("ETHERSCAN_API_KEY")
    ETHERSCAN_BASE_URL = "https://api.etherscan.io/api"

    # User-facing strings
    ETHER_BALANCE_SUCCESS_MESSAGE = "The Ether balance of {address} is {balance_ether} ETH"
    ETHER_BALANCE_FAILURE_MESSAGE = "Failed to retrieve Ether balance. Please enter a valid address."
    CONTRACT_EXECUTION_SUCCESS_MESSAGE = "The contract execution with transaction hash {transaction_hash} was successful."
    CONTRACT_EXECUTION_FAILURE_MESSAGE = "Failed to check contract execution status. Please enter a valid transaction hash."
    TRANSACTION_RECEIPT_SUCCESS_MESSAGE = "The transaction with transaction hash {transaction_hash} was successful."
    TRANSACTION_RECEIPT_FAILURE_MESSAGE = "Failed to check transaction receipt status. Please enter a valid transaction hash."
    ERC20_TOKEN_SUPPLY_SUCCESS_MESSAGE = "The total supply of the ERC20 token with contract address {contract_address} is {total_supply}."
    ERC20_TOKEN_SUPPLY_FAILURE_MESSAGE = "Failed to retrieve ERC20 token supply. Please enter a valid contract address."
    CONFIRMATION_TIME_ESTIMATE_SUCCESS_MESSAGE = "The estimated confirmation time for {network} is {confirmation_time_estimate} seconds."
    CONFIRMATION_TIME_ESTIMATE_FAILURE_MESSAGE = "Failed to retrieve confirmation time estimate. Please enter a valid network."
    API_ERROR_MESSAGE = "I can't seem to access the API at the moment."