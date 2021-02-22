import pandas as pd
import os
import matplotlib.pyplot as plt


def symbol_to_path(symbol, base_dir="/home/behnam/PycharmProjects/MachineLearningForTrading/data"):
    """return CSV file path given ticker symbol"""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """ Read stock data (close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='date', parse_dates=True, usecols=['date', 'close'],
                              na_values=['nan'])
        df_temp = df_temp.rename(columns={'close': symbol})
        df = df.join(df_temp)
        if symbol == symbols[0]:
            df = df.dropna(subset=[symbols[0]])
    return df


def plot_data(df, title="Stock prices"):
    '''plot stock prices'''
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()


def test_run():
    # Read data
    start_date = '2019-01-01'
    end_date = '2020-12-31'
    dates = pd.date_range(start_date, end_date)
    symbols = ['khezar', 'khebahman', 'khemehr', 'folad']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute global statistics for each stock
    print(df.mean())
    #middle
    print(df.median())
    #standard deviation
    print(df.std())

if __name__ == "__main__":
    test_run()
