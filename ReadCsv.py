import pandas as pd


def test_run():
    df = pd.read_csv("data/خبهمن.csv")
    print(df.head())
    print(df.tail())
    print("------")
    print(df[10:21])

def get_max_close(symbol):
    # return the maximum closing value for stock indicated by symbol
    df=pd.read_csv("data/خبهمن.csv")
    return df['close'].max() #compute and return max


if __name__=="__main__":
    test_run()