from langchain.agents import Tool
from .api import EtherscanAPI
from .functions import EtherscanFunctions
from .schema import GetEtherBalance, GetContractExecutionStatus, GetTransactionReceiptStatus, GetERC20TokenSupply, GetConfirmationTimeEstimate

etherscan_functions = EtherscanFunctions()

ETHERSCAN_TOOLS = [
    Tool(
        name="get_ether_balance",
        func=etherscan_functions.get_ether_balance,
        description="Get the Ether balance of a given address",
        args_schema=GetEtherBalance,
        return_direct=True
    ),
    Tool(
        name="get_contract_execution_status",
        func=etherscan_functions.get_contract_execution_status,
        description="Get the execution status of a contract",
        args_schema=GetContractExecutionStatus,
        return_direct=True
    ),
    Tool(
        name="get_transaction_receipt_status",
        func=etherscan_functions.get_transaction_receipt_status,
        description="Get the status of a transaction receipt",
        args_schema=GetTransactionReceiptStatus,
        return_direct=True
    ),
    Tool(
        name="get_erc20_token_supply",
        func=etherscan_functions.get_erc20_token_supply,
        description="Get the total supply of an ERC20 token",
        args_schema=GetERC20TokenSupply,
        return_direct=True
    ),
    Tool(
        name="get_confirmation_time_estimate",
        func=etherscan_functions.get_confirmation_time_estimate,
        description="Estimate the confirmation time of a transaction",
        args_schema=GetConfirmationTimeEstimate,
        return_direct=True
    )
]
