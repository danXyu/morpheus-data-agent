from .api import SantimentAPI
from .functions import SantimentFunctions
from langchain.agents import Tool
from .schema import GetCoinsWithHighestPriceIncrease, GetHighestDevActivity

santiment_functions = SantimentFunctions()

SANTIMENT_TOOLS = [
    Tool(
        name="get_coins_with_highest_price_increase",
        func=santiment_functions.get_coins_with_highest_price_increase,
        description="Get the coins with the highest price increase",
        args_schema=GetCoinsWithHighestPriceIncrease,
        return_direct=True
    ),
    Tool(
        name="get_highest_dev_activity",
        func=santiment_functions.get_highest_dev_activity,
        description="Get the coins with the highest developer activity",
        args_schema=GetHighestDevActivity,
        return_direct=True
    )
]