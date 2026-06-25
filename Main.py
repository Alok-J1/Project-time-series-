<<<<<<< HEAD
print(df.head())
import matplotlib.pyplot as plt 
import pandas as pd 
df = pd.read_excel("C:/Users/manoj/Downloads/LTOTALNSA.xlsx", sheet_name="Monthly")
df[ 'observation_date'] = pd.to_datetime(df['observation_date'], format='%Y-%m-%d')
df.set_index('observation_date', inplace=True)
daily_range  = pd.date_range(start= '2025-01-01',periods=10 , freq='D')
weekly_range  = pd.date_range(start= '2025-01-01',periods=10 , freq='W')
monthly_range  = pd.date_range(start= '2025-01-01',periods=10 , freq='ME')
monthly_sales = df.resample('ME').sum()
quarterly_sales = df.resample('QE').sum()
df['Previous_Month'] = df['LTOTALNSA'].shift(1)
df['Difference'] = df['LTOTALNSA'] - df['Previous_Month']
df ['Rolling_mean'] = df['LTOTALNSA'].rolling(window=5).mean()
plt.figure(figsize=(14,7))
plt.plot(
    df.index,
    df['LTOTALNSA'],
    linewidth=1,
    label='Monthly Vehicle Sales'
)
plt.plot(
    df.index,
    df['Rolling_mean'],
    linewidth=3,
    label='12-Month Rolling Average'
)
plt.title('US Light Vehicle Sales: Original vs Rolling Mean')
plt.xlabel('Date')
plt.ylabel('Sales (Thousands)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


=======
print(df.head());
import matplotlib.pyplot as plt ;
import pandas as pd ;
df = pd.read_excel("C:/Users/manoj/Downloads/LTOTALNSA.xlsx", sheet_name="Monthly");
print(df.columns);
>>>>>>> dd30823 (Add vehicle sales time series analysis)
