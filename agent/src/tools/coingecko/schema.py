from langchain.pydantic_v1 import BaseModel, Field

class GetMarketCap(BaseModel):
    """Input schema for the get_coin_market_cap_tool."""
    coin: str = Field(description="Name of the coin")

