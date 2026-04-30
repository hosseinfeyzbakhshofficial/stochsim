from src.processes.gbm import simulate_gbm
from src.analysis.statistics import estimate_statistics, create_dataframe
from src.analysis.visualization import plot_gbm_dataframe

# simulate
result = simulate_gbm(100, 0.1, 0.2, T=1, dt=0.01, seed=42)

# statistics
stats = estimate_statistics(result)
print(stats)

# dataframe
df = create_dataframe(result)

# plot
plot_gbm_dataframe(df)