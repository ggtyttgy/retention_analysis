"""
retention analysis - generates the retention trend plot and prints key stats.

Run: python analysis.py
"""
import pandas as pd
import matplotlib.pyplot as plt

data = {"Quarter": ['Q1', 'Q2', 'Q3', 'Q4'], "RetentionRate": [65.47, 73.85, 73.61, 77.49]}
df = pd.DataFrame(data)
avg = df["RetentionRate"].mean()

print("Quarterly retention rates:")
print(df.to_string(index=False))
print("\nComputed average retention rate: {:.2f}".format(avg))

# Plot
plt.figure(figsize=(10,5))
plt.plot(df["Quarter"], df["RetentionRate"], marker='o')
plt.axhline(85, linestyle='--', linewidth=1, label='Industry Target (85)')
plt.axhline(avg, linestyle=':', linewidth=1, label=f'Average ({avg:.2f})')
plt.title("Customer Retention Rate — 2024 Quarterly Trend")
plt.ylabel("Retention Rate (%)")
plt.ylim(60, 90)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("retention_trend.png")
print("Saved plot to retention_trend.png")
