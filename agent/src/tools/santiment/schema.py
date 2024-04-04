from langchain.pydantic_v1 import BaseModel, Field

class GetCoinsWithHighestPriceIncrease(BaseModel):
    """Input schema for the get_coins_with_highest_price_increase_tool."""
    limit: int = Field(description="Limit of coins to get")

class GetTrendingCoins(BaseModel):
    """Input schema for the get_trending_coins_tool."""
    limit: int = Field(description="Limit of coins to get")

class GetHighestDevActivity(BaseModel):
    """Input schema for the get_highest_dev_activity_tool."""
    limit: int = Field(description="Limit of coins to get")

class GetHighestNetworkGrowth(BaseModel):
    """Input schema for the get_highest_network_growth_tool."""
    limit: int = Field(description="Limit of coins to get")

class GetHighestTokenCirculation(BaseModel):
    """Input schema for the get_highest_token_circulation_tool."""
    limit: int = Field(description="Limit of coins to get")

class GetHighestTransactionVolume(BaseModel):
    """Input schema for the get_highest_transaction_volume_tool."""
    limit: int = Field(description="Limit of coins to get")
