"""
this script is used to analyze cars mpg and predict fuel efficiency using linear progression.
The data is from https://archive.ics.uci.edu/ml/datasets/Auto+MPG
Usage: python predict_auto_mpg.py
author: Tamby Kaghdo
"""
import pandas as pd
import sys
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def create_scatter_plot(df):
    """
    this function creates scatter plots to show correlations between mpg and other attributes
    :param df: pandas data frame
    :return: NA
    """

    fig = plt.figure()

    ax1 = fig.add_subplot(3,2,1)
    ax2 = fig.add_subplot(3,2,2)
    ax3 = fig.add_subplot(3,2,3)
    ax4 = fig.add_subplot(3,2,4)
    ax5 = fig.add_subplot(3,2,5)
    ax6 = fig.add_subplot(3,2,6)
    df.plot("weight", "mpg", kind="scatter", ax=ax1)
    df.plot("acceleration", "mpg", kind="scatter", ax=ax2)
    df.plot("cylinders", "mpg", kind="scatter", ax=ax3)
    df.plot("displacement", "mpg", kind="scatter", ax=ax4)
    df.plot("model year", "mpg", kind="scatter", ax=ax5)
    df.plot("origin", "mpg", kind="scatter", ax=ax6)
    plt.tight_layout()
    plt.show()
    

def main():
    auto_columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year",
                    "origin", "car name"]
    # the input file is space delimited and column names is in auto_columns
    auto_df = pd.read_table("data/auto-mpg.data", delim_whitespace=True, names=auto_columns)
    print(auto_df.head())
    #create_scatter_plot(auto_df)

    lr = LinearRegression()
    lr.fit(auto_df[["weight"]], auto_df["mpg"])

    mpg_predictions = lr.predict(auto_df[["weight"]])

    plt.scatter(auto_df["weight"], auto_df["mpg"], color="green")
    plt.scatter(auto_df["weight"], mpg_predictions, color="blue")
    plt.ylabel('weight')
    plt.xlabel('mpg actual (green). mpg prediction (blue)')
    plt.title("Actual MPG vs. Predicted MPG")

    #plt.show()

    # MSE will be in mpg squared
    mse = mean_squared_error(auto_df["mpg"], mpg_predictions)
    print(mse)

    #RMSE in mpg
    rmse = mse ** (1/2)
    print(rmse)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)