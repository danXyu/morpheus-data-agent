from .api import CoinGeckoAPI
from .functions import CoinGeckoFunctions
from tools.base import Tool
from tools.schemas import GetMarketCap, GetFDV, GetPrice

coin_gecko_functions = CoinGeckoFunctions()

COINGECKO_TOOLS = [
    Tool(
        name="get_market_cap",
        func=coin_gecko_functions.get_coin_market_cap,
        description="Get the market cap of a coin",
        args_schema=GetMarketCap,
        return_direct=True
    ),
    Tool(
        name="get_fully_diluted_valuation",
        func=coin_gecko_functions.get_fully_diluted_valuation,
        description="Get the fully diluted valuation of a coin",
        args_schema=GetFDV,
        return_direct=True
    ),
    Tool(
        name="get_coin_price",
        func=coin_gecko_functions.get_coin_price,
        description="Get the price of a cryptocurrency",
        args_schema=GetPrice,
        return_direct=True
    )
]