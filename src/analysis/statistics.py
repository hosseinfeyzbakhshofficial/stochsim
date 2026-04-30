import numpy as np
import pandas as pd


def estimate_statistics(results):
    """
    Compute basic statistics of GBM simulation output.

    Parameters
    ----------
    results : np.ndarray
        Simulated price path

    Returns
    -------
    dict
        Dictionary containing summary statistics
    """
    return {
        "mean": np.mean(results),
        "variance": np.var(results),
        "min": np.min(results),
        "max": np.max(results),
    }


def create_dataframe(results):
    """
    Convert simulation output into pandas DataFrame.

    Parameters
    ----------
    results : np.ndarray
        Simulated GBM path

    Returns
    -------
    pd.DataFrame
        DataFrame with time step and price columns
    """
    df = pd.DataFrame({
        "time_step": range(len(results)),
        "price": results
    })

    return df