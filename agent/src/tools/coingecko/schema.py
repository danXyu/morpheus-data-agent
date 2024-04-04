from langchain.pydantic_v1 import BaseModel, Field

class GetPrice(BaseModel):
    """Input schema for the get_coin_price_tool."""
    coin: str = Field(description="Name of the coin")

class GetMarketCap(BaseModel):
    """Input schema for the get_coin_market_cap_tool."""
    coin: str = Field(description="Name of the coin")

class GetFDV(BaseModel):
    """Input schema for the get_fully_diluted_valuation_tool."""
    coin: str = Field(description="Name of the coin")

class GetFloorPrice(BaseModel):
    """Input schema for the get_nft_floor_price_tool."""
    nft: str = Field(description="Name of the NFT")

class GetSparkChart(BaseModel):
    """Input schema for the get_spark_chart_tool."""
    coin: str = Field(description="Name of the coin")
    # TODO: Add days, height, and width as customizable parameters
    # days: int = Field(description="Number of days for the spark chart")
    # height: int = Field(description="Height of the spark chart")
    # width: int = Field(description="Width of the spark chart")
