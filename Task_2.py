import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. EXTRACT ---
print("Loading data...")
# Make sure the file name matches exactly what you saved it as
df = pd.read_csv('Unemployment in India.csv')

# --- 2. TRANSFORM (Data Cleaning) ---
print("Cleaning data...")
# The Kaggle dataset has hidden spaces in the column names, so we strip them out
df.columns = df.columns.str.strip()

# Drop any blank rows
df = df.dropna()

# Clean the 'Date' column and convert it to proper datetime objects
df['Date'] = df['Date'].str.strip()
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# --- 3. LOAD / VISUALIZE ---
print("Generating visualizations...")
sns.set_theme(style="whitegrid")

# Chart A: Unemployment Trend Over Time (Showing the COVID-19 Impact)
plt.figure(figsize=(12, 6))
# Calculate the average unemployment rate for each date
trend_data = df.groupby(
    'Date')['Estimated Unemployment Rate (%)'].mean().reset_index()

sns.lineplot(data=trend_data, x='Date', y='Estimated Unemployment Rate (%)',
             color='red', linewidth=2, marker='o')
plt.title('Impact of COVID-19 on Unemployment Rate in India',
          fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Average Unemployment Rate (%)', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('COVID_Unemployment_Trend.png')  # Saves a copy to your folder
plt.show()  # Pauses code to show you the chart

# Chart B: Average Unemployment by Region
plt.figure(figsize=(12, 8))
# Sort regions by highest unemployment
region_data = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean(
).sort_values(ascending=False).reset_index()

sns.barplot(data=region_data, x='Estimated Unemployment Rate (%)',
            y='Region', palette='viridis')
plt.title('Average Unemployment Rate by Region',
          fontsize=16, fontweight='bold')
plt.xlabel('Average Unemployment Rate (%)', fontsize=12)
plt.ylabel('State / Region', fontsize=12)
plt.tight_layout()
plt.savefig('Unemployment_By_Region.png')
plt.show()

print("Task 2 Complete! Check your folder for the saved images.")
