## **📘 Project Overview**

This project combines my passion for the automotive industry, specifically **Mercedes-Benz**, with my interest in finance and data analysis. Financial statements can often be complex and difficult to interpret, making it challenging to extract meaningful insights.In this notebook, we perform a comprehensive **financial statement analysis** of **Mercedes-Benz Group** covering the period from **2020 to 2024**. The data was sourced using the `yfinance` API, which allows seamless access to financial statements and stock market data.

Our goal is to uncover key **trends**, identify **performance drivers**, and derive **actionable insights** that can inform strategies for growth and improved profitability.

## ❓ Questions Answered

- Is the company making more profit now than it did in the past?
- Is the company getting better or worse at managing its money, paying off what it owes, and running efficiently?
- Are investors likely to get good returns based on how the company is using its money and assets?
- Where does the company get most of its cash from, and how is it spending that money?
- Is the company relying more on loans or its own money to fund its activities?
- As the company earns more, is it also keeping more of that money as profit?

## 🛠️ Tools Used

- **Python** – Core language for analysis and visualization  
  - `pandas` for data manipulation  
  - `matplotlib` & `seaborn` for visualizing trends and ratios  
  - `yfinance` API to extract financial statements (MBG.DE)

- **Jupyter Notebook** – For combining code, visuals, and insights in one place  
- **VS Code** – For code editing and project organization  
- **Git & GitHub** – For version control and sharing the analysis

## 📊 Project Workflow

1. **Data Extraction** – Collected financial statements using the `yfinance` API.  
2. **Data Cleaning** – Formatted dates, handled missing values, and structured data.  
3. **EDA** – Explored key metrics and trends from 2020 to 2024.  
4. **Ratio Analysis** – Calculated profitability, liquidity, solvency, and return ratios.  
5. **Visualization** – Created charts to highlight financial performance and structure.  
6. **Insights** – Interpreted trends and answered business questions.  
7. **Documentation** – Summarized findings in notebooks and this README.

For steps 1 to 4 : [Click here](Notebooks/01_Data_Preparation.ipynb)

For steps 5 and 6 : [Click here](Notebooks/02_Financial_Anlysis.ipynb)


## Explanation of some terms used in this project
### 🤔 What Are Financial Statements?

A **financial statement** is a summary of a company’s financial performance and position. It usually includes:

1. **Income Statement** – Reports revenue, expenses, and profit over time.  
2. **Balance Sheet** – Shows assets, liabilities, and equity at a specific point.  
3. **Cash Flow Statement** – Tracks cash movement from operations, investing, and financing.


### 🤓 About `yfinance`

We used the **`yfinance`** Python library to retrieve financial data for Mercedes-Benz Group AG (`MBG.DE`) from Yahoo Finance. This allowed us to:

- Automatically extract income statements, balance sheets, and cash flow data  
- Analyze performance from **2020 to 2024** using up-to-date and accurate figures

Using `yfinance` eliminated the need for manual downloads and streamlined the analysis process.


### 🤔 What is a Ticker Symbol?

A **ticker symbol** is a short code used to identify a company’s stock. In this project, we used the symbol **`MBG.DE`** (Mercedes-Benz Group on the Deutsche Börse) to fetch financial data via the `yfinance` API.










