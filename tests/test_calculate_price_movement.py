import freezegun
from stockplot.shared import calculate_price_movement
from tests.conftest import (
    example_yahoo_api_response_1day_tsla_2023_02_26,
    example_yahoo_api_response_90day_tsla_2023_02_26,
    example_yahoo_api_response_90day_aapl_2023_03_01,
    example_yahoo_api_response_1day_aapl_2023_03_01,
)


@freezegun.freeze_time("2023-02-26")
def test_calculate_price_movement_scenario1(
    mock_GET_yahoo_v8_finance_chart_api_1day_range,
    mock_GET_yahoo_v8_finance_chart_api_90day_range,
):
    mock_GET_yahoo_v8_finance_chart_api_90day_range(
        "TSLA", example_yahoo_api_response_90day_tsla_2023_02_26
    ),
    mock_GET_yahoo_v8_finance_chart_api_1day_range(
        "TSLA", example_yahoo_api_response_1day_tsla_2023_02_26
    )

    current_price, change_1day, change_7day, change_30day = calculate_price_movement(
        "tsla"
    )
    (
        expected_current_price,
        expected_change_1day,
        expected_change_7day,
        expected_change_30day,
    ) = (196.86, 0.27, -5.50, 10.66)
    assert round(current_price, 2) == expected_current_price
    assert round(change_1day, 2) == expected_change_1day
    assert round(change_7day, 2) == expected_change_7day
    assert round(change_30day, 2) == expected_change_30day


@freezegun.freeze_time("2023-03-01")
def test_calculate_price_movement_scenario2(
    mock_GET_yahoo_v8_finance_chart_api_1day_range,
    mock_GET_yahoo_v8_finance_chart_api_90day_range,
):
    mock_GET_yahoo_v8_finance_chart_api_90day_range(
        "AAPL", example_yahoo_api_response_90day_aapl_2023_03_01
    )
    mock_GET_yahoo_v8_finance_chart_api_1day_range(
        "AAPL", example_yahoo_api_response_1day_aapl_2023_03_01
    )

    current_price, change_1day, change_7day, change_30day = calculate_price_movement(
        "aapl"
    )
    (
        expected_current_price,
        expected_change_1day,
        expected_change_7day,
        expected_change_30day,
    ) = (145.09, -1.23, -2.57, 1.62)
    assert round(current_price, 2) == expected_current_price
    assert round(change_1day, 2) == expected_change_1day
    assert round(change_7day, 2) == expected_change_7day
    assert round(change_30day, 2) == expected_change_30day
