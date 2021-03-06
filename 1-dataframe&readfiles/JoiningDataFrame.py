import pandas as pd
import matplotlib.pyplot as plt
import os


def test_run():
    start_date = "2017-11-11"
    end_date = "2021-02-09"
    dates = pd.date_range(start_date, end_date)
    df1 = pd.DataFrame(index=dates)
    print(df1)
    # read first stock data on csv file

    # default index of read csv file are integeres we want to used date as index_column with this line
    dfStock1 = pd.read_csv("data/khezar.csv", index_col="date", parse_dates=True, usecols=['date', 'close'],
                           na_values=['nan'])

    # print(dfStock1)
    dfStock1 = dfStock1.rename(columns={'close': 'khezar'})

    df1 = df1.join(dfStock1, how='inner')
    # drop nan values
    df1 = df1.dropna()
    # print(df1)
    # Read in more stocks
    symbols = ['khemehr', 'khebahman']

    for symbol in symbols:
        df_temp = pd.read_csv("data/{}.csv".format(symbol), index_col='date', parse_dates=True,
                              usecols=['date', 'close'], na_values=['nan'])

        # rename to prevent clash
        df_temp = df_temp.rename(columns={'close': symbol})
        df1 = df1.join(df_temp)  # use default how='left'

    print(df1)
    df1[['khemehr', 'khezar']].plot()
    plt.show()


# another way of implementation this

def symbol_to_path(symbol, base_dir="data"):
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


def join_symbols():
    """ better implementation of test_run1"""
    start_date = "2017-11-11"
    end_date = "2021-02-09"
    dates = pd.date_range(start_date, end_date)
    symbols = ['khezar', 'khemehr', 'khebahman']
    df = get_data(symbols, dates)
    print(df)
    # df[['khemehr', 'khezar']].plot()
    # plt.show()
    # work on subset of data
    df = normalize_data(df)
    print("After normalizing: ")
    print(df)
    df1 = df['2018-05-02':'2019-05-02']
    print("Print a rows subset of this data:")
    print(df1)

    # filter columns
    print(df[['khebahman', 'khemehr']])
    print("Another type of subset with subset of columns and rows")

    df2 = df.loc['2018-05-02':'2019-05-02', 'khemehr':'khebahman']
    print(df2)

    # plot_data(df)
    plot_selected(df, ['khezar', 'khebahman'], '2018-05-02', '2021-02-14')


def plot_data(df, title="Stock prices"):
    '''plot stock prices'''
    ax = df.plot(title=title, fontsize=2)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")

    plt.show()


def plot_selected(df, columns, start_index, end_index):
    plot_data(df.loc[start_index:  end_index, columns[0]:columns[1]], title="Selected data")


def normalize_data(df):
    """Normalize stock prices using first row of the 1-dataframe&readfiles."""
    print("Normalizing with:\n")
    print(df.iloc[0,:])
    print("finally \n\n")
    ##looks like at day 1 the stock price was 1$
    return df / df.iloc[0,:]


if __name__ == "__main__":
    # test_run()
    join_symbols()
