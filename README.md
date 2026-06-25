# Time Series Analysis: U.S. Light Vehicle Sales Dynamics

## Project Overview
This project is from [roadmap.sh](https://roadmap.sh/projects/pandas-time-series) focuses on performing Exploratory Time Series Analysis (ETSA) on a light vehicle sales dataset sourced from **[FRED](https://fred.stlouisfed.org/series/LTOTALNSA)(Federal Reserve Economic Data)**. The primary objective is to demonstrate proficiency in handling time-series data structures using Python and the Pandas library, specifically focusing on resampling, shifting, and trend extraction.

## Key Features
* **Data Preprocessing:** Automated parsing of date columns and setting up a `DatetimeIndex`.
* **Resampling:** Aggregating granular sales data into Monthly and Quarterly totals to observe broader business performance.
* **Feature Engineering:** Utilizing `.shift()` and `.diff()` to calculate period-over-period changes and growth rates.
* **Trend Analysis:** Implementation of a 12-month Rolling Mean (Moving Average) to smooth out seasonal fluctuations and visualize long-term market trends.
* **Professional Visualization:** Automated generation of high-resolution trend charts (300 DPI) using Matplotlib.

## Technologies Used
* **Language:** Python
* **Libraries:** Pandas, Matplotlib
* **Environment:** VS Code / Jupyter Notebook

## Insights & Learning Outcomes
Through this project, I applied several advanced Pandas methods:
- **Resampling ('M', 'Q'):** Essential for financial reporting where data needs to be grouped by business cycles.
- **Differencing:** A fundamental technique in time series forecasting to make the data stationary.
- **Rolling Windows:** Used to identify the "signal" within the "noise" of monthly sales volatility.
