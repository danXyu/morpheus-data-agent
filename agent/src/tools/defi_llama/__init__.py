from .api import DefiLlamaAPI
from .functions import DefiLlamaFunctions
from tools.base import Tool
from tools.schemas import GetMarketCap, GetFDV, GetPrice

defi_llama_functions = DefiLlamaFunctions()

DEFI_LLAMA_TOOLS = [
    Tool(
        name="get_protocol_total_value_locked_tool",
        func=defi_llama_functions.get_protocol_total_value_locked,
        description="Get the total value locked of a protocol",
        args_schema=GetTVL,
        return_direct=True
    ),
]