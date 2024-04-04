from langchain.pydantic_v1 import BaseModel, Field

class GetEtherBalance(BaseModel):
    """Input schema for the get_ether_balance_tool."""
    address: str = Field(description="Ether address to get the balance from")

class GetContractExecutionStatus(BaseModel):
    """Input schema for the get_contract_execution_status_tool."""
    transaction_hash: str = Field(description="Transaction hash to check the status of")

class GetTransactionReceiptStatus(BaseModel):
    """Input schema for the get_transaction_receipt_status_tool."""
    transaction_hash: str = Field(description="Transaction hash to check receipt of")

class GetERC20TokenSupply(BaseModel):
    """Input schema for the get_erc20_token_supply_tool."""
    contract_address: str = Field(description="Contract address of the ERC20 token")

class GetConfirmationTimeEstimate(BaseModel):
    """Input schema for the get_confirmation_time_estimate_tool."""
    network: str = Field(description="Name of the network") # Defaults to mainnet

