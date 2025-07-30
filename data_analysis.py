import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("sample_data.csv")

# Basic info
print("Dataset Head:")
print(df.head())

# Calculate average of a selected column
column_name = "Marks"
average = df[column_name].mean()
print(f"Average of {column_name}: {average}")

# Bar chart
plt.figure(figsize=(8, 5))
plt.bar(df["Name"], df[column_name], color="skyblue")
plt.title("Marks by Student")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")

# Scatter plot
plt.figure(figsize=(6, 4))
plt.scatter(df["Age"], df[column_name], color="green")
plt.title("Marks vs Age")
plt.xlabel("Age")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("scatter_plot.png")

# Heatmap of correlations
plt.figure(figsize=(5, 4))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap.png")

print("All graphs saved as images.")
