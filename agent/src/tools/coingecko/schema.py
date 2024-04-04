from langchain.pydantic_v1 import BaseModel, Field

class GetPrice(BaseModel):
    """Input schema for the get_coin_price_tool."""
    coin: str = Field(description="Name of the coin")

class GetMarketCap(BaseModel):
    """Input schema for the get_coin_market_cap_tool."""
    coin: str = Field(description="Name of the coin")

class GetFloorPrice(BaseModel):
    """Input schema for the get_nft_floor_price_tool."""
    nft: str = Field(description="Name of the NFT")