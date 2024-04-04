import pytest
from src.tools.coingecko import CoinGeckoAPI

@pytest.fixture
def coingecko_api():
    return CoinGeckoAPI()

def test_get_coingecko_id_coin(coingecko_api):
    coin_id = coingecko_api._get_coingecko_id("bitcoin", "coin")
    assert coin_id is not None
    assert isinstance(coin_id, str)

def test_get_coingecko_id_nft(coingecko_api):
    nft_id = coingecko_api._get_coingecko_id("cryptopunks", "nft")
    assert nft_id is not None
    assert isinstance(nft_id, str)

def test_get_price(coingecko_api):
    price = coingecko_api.get_price("bitcoin")
    assert price is not None
    assert isinstance(price, int)

def test_get_floor_price(coingecko_api):
    floor_price = coingecko_api.get_floor_price("cryptopunks")
    assert floor_price is not None
    assert isinstance(floor_price, int)

def test_get_fdv(coingecko_api):
    fdv = coingecko_api.get_fdv("bitcoin")
    assert fdv is not None
    assert isinstance(fdv, int)

def test_get_market_cap(coingecko_api):
    market_cap = coingecko_api.get_market_cap("bitcoin")
    assert market_cap is not None
    assert isinstance(market_cap, int)

def test_get_price_spark_chart(coingecko_api, capsys):
    spark_chart = coingecko_api.get_price_spark_chart("bitcoin", 1, 10, 60)
    assert spark_chart is not None
    assert "Bitcoin Price Spark Chart (Last 1 Days)" in spark_chart

