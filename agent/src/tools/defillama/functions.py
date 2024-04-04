from .config import Config
from .api import DefiLlamaAPI

class DefiLlamaFunctions:
    def __init__(self):
        self.config = Config()
        self.defi_llama_api = DefiLlamaAPI()

    def get_protocol_total_value_locked(self, protocol_name):
        """Get the TVL (Total Value Locked) of a protocol."""
        try:
            tvl = get_protocol_tvl(protocol_name)
            if tvl is None:
                return self.config.TVL_FAILURE_MESSAGE
            return self.config.TVL_SUCCESS_MESSAGE.format(protocol_name=protocol_name, tvl=tvl)
        except requests.exceptions.RequestException:
            return self.config.API_ERROR_MESSAGE
