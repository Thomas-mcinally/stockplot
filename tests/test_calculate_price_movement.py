import freezegun
from stockplot.calculate_price_movement import calculate_price_movement
from tests.conftest import (
    example_yahoo_api_response_30day_aapl_2023_03_13,
    example_yahoo_api_response_30day_btc_eur_2023_03_13,
    example_yahoo_api_response_30day_tsla_2023_03_14_before_market_open,
)


@freezegun.freeze_time("2023-03-13")
def test_calculate_price_movement_scenario1(
    mock_GET_yahoo_v8_finance_chart_api_30day_range
):
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "BTC-EUR", example_yahoo_api_response_30day_btc_eur_2023_03_13
    )

    current_price, currency, change_1day, change_7day, change_30day = calculate_price_movement(
        "BTC-EUR"
    )
    assert round(current_price, 2) == 24295.92
    assert currency == "EUR"
    assert round(change_1day, 2) == 9.62
    assert round(change_7day, 2) == 8.32
    assert round(change_30day, 2) == 11.51


@freezegun.freeze_time("2023-03-13")
def test_calculate_price_movement_scenario2(
    mock_GET_yahoo_v8_finance_chart_api_30day_range
):
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "AAPL", example_yahoo_api_response_30day_aapl_2023_03_13
    )

    current_price, currency, change_1day, change_7day, change_30day = calculate_price_movement(
        "AAPL"
    )
    assert round(current_price, 2) == 150.47
    assert currency == "USD"
    assert round(change_1day, 2) == 1.33
    assert round(change_7day, 2) == -2.18
    assert round(change_30day, 2) == -0.36


@freezegun.freeze_time("2023-03-14")
def test_calculate_price_movement_before_market_opens(
    mock_GET_yahoo_v8_finance_chart_api_30day_range
):
    mock_GET_yahoo_v8_finance_chart_api_30day_range(
        "TSLA", example_yahoo_api_response_30day_tsla_2023_03_14_before_market_open
    )

    current_price, currency, change_1day, change_7day, change_30day = calculate_price_movement(
        "TSLA"
    )

    assert round(current_price, 2) == 174.95
    assert currency == "USD"
    assert round(change_1day, 2) == 0.87
    assert round(change_7day, 2) == -6.80
    assert round(change_30day, 2) == -11.14
