from langchain.pydantic_v1 import BaseModel, Field

class GetProtocolTotalValueLocked(BaseModel):
    """Input schema for the get_protocol_total_value_locked_tool."""
    protocol: str = Field(description="Name of the protocol")

