import pytest
from src.tools.santiment.api import SantimentAPI

@pytest.fixture
def santiment_api():
    return SantimentAPI()

def test_make_api_request(santiment_api):
    query = '''
        query {
            allProjects {
                slug
            }
        }
    '''
    response = santiment_api._make_api_request(query)
    assert response is not None, "Response should not be None"
    assert isinstance(response, dict), "Response should be a dictionary"

def test_get_coins_with_highest_price_increase(santiment_api):
    highest_price_increase_coins = santiment_api.get_coins_with_highest_price_increase()
    assert highest_price_increase_coins is not None, "Coins data should not be None"
    assert isinstance(highest_price_increase_coins, list), "Coins should be a list"
    if highest_price_increase_coins:
        assert isinstance(highest_price_increase_coins[0], tuple), "Each coin should be a dictionary"

def test_get_highest_dev_activity(santiment_api):
    highest_dev_activity = santiment_api.get_highest_dev_activity()
    assert highest_dev_activity is not None, "Highest dev activity data should not be None"
    assert isinstance(highest_dev_activity, list), "Highest dev activity should be a list"
    if highest_dev_activity:
        assert isinstance(highest_dev_activity[0], tuple), "Each item should be a tuple"

# def test_get_highest_network_growth(santiment_api):
#     highest_network_growth = santiment_api.get_highest_network_growth()
#     assert highest_network_growth is not None, "Highest network growth data should not be None"
#     assert isinstance(highest_network_growth, list), "Highest network growth should be a list"
#     if highest_network_growth:
#         assert isinstance(highest_network_growth[0], tuple), "Each item should be a dictionary"

# def test_get_highest_token_circulation(santiment_api):
#     highest_token_circulation = santiment_api.get_highest_token_circulation()
#     assert highest_token_circulation is not None, "Highest token circulation data should not be None"
#     assert isinstance(highest_token_circulation, list), "Highest token circulation should be a list"
#     if highest_token_circulation:
#         assert isinstance(highest_token_circulation[0], tuple), "Each item should be a dictionary"

# def test_get_highest_transaction_volume(santiment_api):
#     highest_transaction_volume = santiment_api.get_highest_transaction_volume()
#     assert highest_transaction_volume is not None, "Highest transaction volume data should not be None"
#     assert isinstance(highest_transaction_volume, list), "Highest transaction volume should be a list"
#     if highest_transaction_volume:
#         assert isinstance(highest_transaction_volume[0], tuple), "Each item should be a dictionary"
