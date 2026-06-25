import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset

df = pd.read_excel(
    "C:/Users/manoj/Downloads/LTOTALNSA.xlsx",
    sheet_name="Monthly"
)

# Convert Date Column

df['observation_date'] = pd.to_datetime(df['observation_date'])

# Make date the index
df.set_index('observation_date', inplace=True)

# Display First Few Rows

print(df.head())

# Create Date Ranges

daily_range = pd.date_range(
    start='2025-01-01',
    periods=10,
    freq='D'
)

weekly_range = pd.date_range(
    start='2025-01-01',
    periods=10,
    freq='W'
)

monthly_range = pd.date_range(
    start='2025-01-01',
    periods=10,
    freq='ME'
)

print("\nDaily Range")
print(daily_range)

print("\nWeekly Range")
print(weekly_range)

print("\nMonthly Range")
print(monthly_range)

# Resampling

monthly_sales = df['LTOTALNSA'].resample('ME').sum()
quarterly_sales = df['LTOTALNSA'].resample('QE').sum()

print("\nMonthly Sales")
print(monthly_sales.head())

print("\nQuarterly Sales")
print(quarterly_sales.head())

# Shift and Difference

df['Previous_Month'] = df['LTOTALNSA'].shift(1)

# Simpler than subtracting manually
df['Difference'] = df['LTOTALNSA'].diff()

# Rolling Mean

df['Rolling_Mean'] = df['LTOTALNSA'].rolling(window=12).mean()

# Plot

plt.figure(figsize=(14,7))

plt.plot(
    df.index,
    df['LTOTALNSA'],
    label='Monthly Vehicle Sales',
    linewidth=1
)

plt.plot(
    df.index,
    df['Rolling_Mean'],
    label='12-Month Rolling Average',
    linewidth=3
)

plt.title("US Light Vehicle Sales")
plt.xlabel("Date")
plt.ylabel("Sales (Thousands)")
plt.legend()

plt.grid(
    True,
    linestyle='--',
    alpha=0.6
)
plt.tight_layout()
plt.show()