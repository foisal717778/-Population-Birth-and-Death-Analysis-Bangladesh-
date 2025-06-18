import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data/birth_death_bangladesh.csv')
df["Net_Population_Change"] = df["Births"] - df["Deaths"]

# Plotting
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
plt.plot(df["Month"], df["Births"], marker='o', label='Births')
plt.plot(df["Month"], df["Deaths"], marker='o', label='Deaths')
plt.plot(df["Month"], df["Net_Population_Change"], marker='o', label='Net Change')
plt.title("Birth, Death, and Net Population Change (Bangladesh: Feb–May 2025)")
plt.xlabel("Month")
plt.ylabel("Number of People")
plt.legend()
plt.tight_layout()
plt.savefig('output/population_trend.png')
plt.show()
