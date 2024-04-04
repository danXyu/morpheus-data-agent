from langchain.agents import Tool
from .api import CoinGeckoAPI
from .functions import CoinGeckoFunctions
from .schema import GetMarketCap, GetFDV, GetPrice, GetSparkChart

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
    ),
    Tool(
        name="get_spark_chart",
        func=coin_gecko_functions.get_spark_chart,
        description="Get the spark chart of a cryptocurrency",
        args_schema=GetSparkChart,
        return_direct=True
    )
]