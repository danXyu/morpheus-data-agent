import pytest
from src.tools.defi_llama import DefiLlamaAPI

@pytest.fixture
def defillama_api():
    return DefiLlamaAPI()

def test_get_protocols_list(defillama_api):
    protocols_list, gecko_ids = defillama_api.get_protocols_list()
    assert protocols_list is not None
    assert gecko_ids is not None
    assert isinstance(protocols_list, list)
    assert isinstance(gecko_ids, list)
    assert all(isinstance(item, str) for item in protocols_list)
    assert all(isinstance(item, str) for item in gecko_ids)

# TODO: This test is broken. This function in the API might be misconfigured.
def test_get_protocol_tvl(defillama_api):
    protocol_tvl = defillama_api.get_protocol_tvl("bitcoin")
    assert protocol_tvl is not None
    assert isinstance(protocol_tvl, dict)
