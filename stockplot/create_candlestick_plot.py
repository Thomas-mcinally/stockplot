from mplfinance import figure, plot


def create_in_memory_candlestick_plot(
    ticker,
    currency,
    data_1day,
    data_90day,
    current_price,
    change_1day,
    change_7day,
    change_30day,
) -> None:
    """
    Creates a mplfinance candlestick plot in memory. Can be displayed at a later time using the show() function from mplfinance
    Parameters:
        ticker (str): Stock ticker
        currency (str): currency for all prices
        data_1day (pandas.DataFrame): Price for ticker every 30m for last 24h
        data_90day (pandas.DataFrame): Price for ticker every 1h for last 90days
        current_price (float): Current price for ticker
        change_1day (float): Percentage price change over last 24hr
        change_7day (float): Percentage price change over last 7days
        change_30day (float): Percentage price change over last 30days
    """
    last_trading_day = data_1day.index.format()[0].split(" ")[0]

    fig = figure(figsize=(13, 6), style="blueskies")

    ax1 = fig.add_subplot(2, 2, 1)
    ax1_vol = fig.add_subplot(2, 2, 3)
    ax2 = fig.add_subplot(2, 2, 2)
    ax2_vol = fig.add_subplot(2, 2, 4)

    plot(
        data_90day,
        ax=ax1,
        volume=ax1_vol,
        type="line",
        datetime_format="%d-%m",
        xrotation=20,
        axtitle=f"{ticker} last 90 days",
    )
    plot(
        data_1day,
        ax=ax2,
        volume=ax2_vol,
        type="candle",
        xrotation=20,
        axtitle=f"{ticker} last trading day ({last_trading_day})",
    )
    fig.suptitle(
        f"Current market price: {current_price:.2f} {currency} , Daily change {change_1day:.2f}% , 7-day change: {change_7day:.2f}%, 30-day change: {change_30day:.2f}%"
    )

    return
