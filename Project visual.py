import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load preprocessed data
df = pd.read_csv("signal_metrics_cleaned.csv")

# 1️⃣ Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Feature Correlation Heatmap")
plt.show()

# 2️⃣ Category Distribution (Network Type)
sns.countplot(x='Network Type', data=df, palette='Set2')
plt.title("Distribution of Network Types")
plt.show()

# 3️⃣ Boxplot (Signal Strength vs Network Type)
sns.boxplot(x='Network Type', y='Signal Strength (dBm)', data=df, palette='coolwarm')
plt.title("Signal Strength Distribution by Network Type")
plt.show()

