from .api import EtherscanAPI
from .functions import EtherscanFunctions
from tools.base import Tool
from tools.schemas import GetEtherBalance, CheckContractExecutionStatus, CheckTransactionReceiptStatus, GetERC20TokenSupply, GetConfirmationTimeEstimate

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
        name="check_contract_execution_status",
        func=etherscan_functions.check_contract_execution_status,
        description="Check the execution status of a contract",
        args_schema=CheckContractExecutionStatus,
        return_direct=True
    ),
    Tool(
        name="check_transaction_receipt_status",
        func=etherscan_functions.check_transaction_receipt_status,
        description="Check the status of a transaction receipt",
        args_schema=CheckTransactionReceiptStatus,
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
