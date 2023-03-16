import sys
import yfinance as yf
from mplfinance import show
from stockplot.calculate_price_movement import calculate_price_movement
from stockplot.create_candlestick_plot import create_in_memory_candlestick_plot


def main(ticker: str = sys.argv[1]) -> None:
    ticker = ticker.upper()

    (
        current_price,
        currency,
        percentage_change_1day,
        percentage_change_7day,
        percentage_change_30day,
    ) = calculate_price_movement(ticker)

    data_90day = yf.download(
        ticker, period="90d", interval="1d", auto_adjust=True, progress=False
    )
    data_1day = yf.download(
        ticker, period="1d", interval="30m", auto_adjust=True, progress=False
    )

    create_in_memory_candlestick_plot(
        ticker,
        currency,
        data_1day,
        data_90day,
        current_price,
        percentage_change_1day,
        percentage_change_7day,
        percentage_change_30day,
    )
    show()


if __name__ == "__main__":
    main()
