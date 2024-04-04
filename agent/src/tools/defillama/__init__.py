from langchain.agents import Tool
from .api import DefiLlamaAPI
from .functions import DefiLlamaFunctions
from .schema import GetProtocolTotalValueLocked

defi_llama_functions = DefiLlamaFunctions()

DEFI_LLAMA_TOOLS = [
    Tool(
        name="get_protocol_total_value_locked_tool",
        func=defi_llama_functions.get_protocol_total_value_locked,
        description="Get the total value locked of a protocol",
        args_schema=GetProtocolTotalValueLocked,
        return_direct=True
    ),
]