import pandas as pd
import matplotlib.pyplot as plt


def test_run():
    df = pd.read_csv("data/خبهمن.csv")
    print(df.head())
    print(df.tail())
    print("------")
    print(df[10:21])


def get_max_close(symbol):
    # return the maximum closing value for stock indicated by symbol
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['close'].max()  # compute and return max


def get_mean_volume(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['volume'].mean()


def test_run2():
    for symbol in ['خبهمن', 'خمهر']:
        print("Max Close")
        print(symbol, get_max_close(symbol))
        print("Mean Volume")
        print(symbol, get_mean_volume(symbol))


def plot_stock_data(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    print(df['close'])
    df[['close', 'open']].plot()  # plot 2 columns
    plt.show()


if __name__ == "__main__":
    test_run()
    test_run2()
    plot_stock_data("خبهمن")
