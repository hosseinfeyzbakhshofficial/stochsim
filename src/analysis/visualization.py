import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_gbm(results):
    """
    Plot GBM path using seaborn
    """
    df = pd.DataFrame({
        "time": range(len(results)),
        "price": results
    })

    sns.lineplot(data=df, x="time", y="price")

    plt.title("GBM Simulation")
    plt.xlabel("Time Step")
    plt.ylabel("Price")
    plt.grid(True)
    plt.show()


def plot_gbm_dataframe(df):
    """
    Plot GBM dataframe
    """
    plt.figure(figsize=(8, 5))

    sns.lineplot(
        data=df,
        x="time_step",
        y="price"
    )

    plt.title("GBM Simulation")
    plt.xlabel("Time Step")
    plt.ylabel("Price")
    plt.grid(True)
    plt.show()