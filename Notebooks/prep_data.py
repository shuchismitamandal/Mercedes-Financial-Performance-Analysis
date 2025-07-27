# Import the necessary libraries
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define the ticker symbol for Mercedes-Benz
ticker_symbol = "MBG.DE" 

# Create a Ticker object
mercedes = yf.Ticker(ticker_symbol)

income_statement_df = mercedes.income_stmt
balance_sheet_df = mercedes.balance_sheet
cash_flow_df = mercedes.cashflow

# Data cleaning
income_statement_df.drop('2020-12-31',axis=1,inplace=True)
balance_sheet_df.drop('2020-12-31',axis=1,inplace=True)
cash_flow_df.drop('2020-12-31',axis=1,inplace=True)

income_statement_transposed = income_statement_df.T
balance_sheet_transposed = balance_sheet_df.T
cash_flow_transposed = cash_flow_df.T

income_statement_transposed.index = pd.to_datetime(income_statement_transposed.index)
balance_sheet_transposed.index = pd.to_datetime(balance_sheet_transposed.index)
cash_flow_transposed.index = pd.to_datetime(cash_flow_transposed.index)

income_statement_transposed = income_statement_transposed.sort_index(ascending=True)
balance_sheet_transposed = balance_sheet_transposed.sort_index(ascending=True)
cash_flow_transposed = cash_flow_transposed.sort_index(ascending=True)

income_statement_transposed.fillna(0, inplace=True)
balance_sheet_transposed.fillna(0, inplace=True)
cash_flow_transposed.fillna(0, inplace=True)

# Displaying the columns chosen for further analysis
selected_income = income_statement_transposed[['Gross Profit', 'Net Income', 'Total Revenue','EBIT','Operating Income','Tax Rate For Calcs']]
selected_balance = balance_sheet_transposed[['Current Assets', 'Current Liabilities', 'Total Debt', 'Stockholders Equity', 'Total Assets','Invested Capital','Total Equity Gross Minority Interest']]
selected_cashflow = cash_flow_transposed[['Operating Cash Flow','Investing Cash Flow','Financing Cash Flow']]

# Merge the selected financial data into one DataFrame based on the date index
financial_data = pd.merge(selected_income, selected_balance, left_index=True, right_index=True)
financial_data = pd.merge(financial_data, selected_cashflow, left_index=True, right_index=True)

# Initialize a DataFrame to store ratios
df = pd.DataFrame(index=financial_data.index)

# 1. Gross Profit Margin
# Handle potential division by zero by setting to NaN or 0 if denominator is 0
df['Gross Profit Margin'] = (financial_data['Gross Profit'] / financial_data['Total Revenue']).replace([float('inf'), -float('inf')], pd.NA)

# 2. Net Profit Margin
df['Net Profit Margin'] = (financial_data['Net Income'] / financial_data['Total Revenue']).replace([float('inf'), -float('inf')], pd.NA)

# 3. Current Ratio
df['Current Ratio'] = (financial_data['Current Assets'] / financial_data['Current Liabilities']).replace([float('inf'), -float('inf')], pd.NA)

# 4. Debt-to-Equity Ratio
# Check for zero Stockholders Equity to avoid division by zero
df['Debt-to-Equity Ratio'] = (financial_data['Total Debt'] / financial_data['Stockholders Equity']).replace([float('inf'), -float('inf')], pd.NA)

# 5. Asset Turnover Ratio
df['Asset Turnover Ratio'] = (financial_data['Total Revenue'] / financial_data['Total Assets']).replace([float('inf'), -float('inf')], pd.NA)

# 6. Return on Equity (ROE)
df['Return on Equity (ROE)'] = (financial_data['Net Income'] / financial_data['Stockholders Equity']).replace([float('inf'), -float('inf')], pd.NA)

# 7. Return on Assets (ROA)
df['Return on Assets (ROA)'] = (financial_data['Net Income'] / financial_data['Total Assets']).replace([float('inf'), -float('inf')], pd.NA)

# 8. Return on Invested Capital (ROIC)
NOPAT = financial_data['Operating Income'] * (1 - (financial_data['Tax Rate For Calcs'] / 100))
df['Return on Invested Capital (ROIC)'] = (NOPAT / financial_data['Invested Capital']).replace([float('inf'), -float('inf')], pd.NA)

df['Gross Profit Margin'] = df['Gross Profit Margin'] * 100
df['Net Profit Margin'] = df['Net Profit Margin'] * 100
df['Return on Equity (ROE)'] = df['Return on Equity (ROE)'] * 100
df['Return on Assets (ROA)'] = df['Return on Assets (ROA)'] * 100
df['Return on Invested Capital (ROIC)'] = df['Return on Invested Capital (ROIC)'] * 100

# Return the final processed dataframes for use in notebooks
def get_processed_data():
    return financial_data, df
