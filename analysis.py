import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Basic info
print(df.head())

# Metrics
total_files = len(df)
success_rate = (df['status'] == 'Success').mean() * 100
avg_time = df['processing_time'].mean()

print("Total Files:", total_files)
print("Success Rate:", success_rate)
print("Average Processing Time:", avg_time)

# Success vs Failure
df['status'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Success vs Failure")
plt.show()

# Processing Trend
df.groupby('date')['processing_time'].mean().plot()
plt.title("Processing Time Trend")
plt.xlabel("Date")
plt.ylabel("Time")
plt.show()

# User Activity
df['user_id'].value_counts().plot(kind='bar')
plt.title("User Activity")
plt.show()
