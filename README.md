## **📘 Project Overview**

This project combines my passion for the automotive industry, specifically **Mercedes-Benz**, with my interest in finance and data analysis. Financial statements can often be complex and difficult to interpret, making it challenging to extract meaningful insights.In this notebook, we perform a comprehensive **financial statement analysis** of **Mercedes-Benz Group** covering the period from **2020 to 2024**. The data was sourced using the `yfinance` API, which allows seamless access to financial statements and stock market data.

Our goal is to uncover key **trends**, identify **performance drivers**, and derive **actionable insights** that can inform strategies for growth and improved profitability.

## **❓ Questions Answered**

- Is the company making more profit now than it did in the past?
- Is the company getting better or worse at managing its money, paying off what it owes, and running efficiently?
- Are investors likely to get good returns based on how the company is using its money and assets?
- Where does the company get most of its cash from, and how is it spending that money?
- Is the company relying more on loans or its own money to fund its activities?
- As the company earns more, is it also keeping more of that money as profit?

## **📊 Overall Insights**
*To get detailed insights, click here :* [Notebook](Notebooks/02_Financial_Anlysis.ipynb)

From 2021 to 2024, Mercedes-Benz’s financial journey tells a story of strength, challenges, and opportunities.

In the beginning, the company was doing well — making solid profits and managing its operations efficiently. The **Gross Profit Margin** stayed comfortably **above 22%**, showing that core operations were healthy. But by 2024, this number dropped slightly to **19.6%**, hinting at rising costs or pricing pressures.

At the same time, the **Net Profit Margin** — which shows how much actual profit remains after all expenses — fell from **17.2% to just 7%**. This means even though the business was running well, other costs were eating into its profits.

Looking at returns, key indicators like **Return on Equity** and **Return on Assets** declined over time, suggesting the company was making less profit from the money and assets it had.

But it’s not all bad news.

Mercedes-Benz actually **improved its financial health** in several areas:
- It became better at handling short-term obligations, as seen in the rising **Current Ratio**.
- It **reduced its reliance on debt**, which is a smart move in uncertain times.
- Its **operating cash flow** — the cash it earns from its main business — remained strong.

On the growth side, though, things were slower. **Revenue growth** dropped from **12%** to negative territory, and **Net income** (final profit) shrank even more sharply. This suggests that while the company still made money, it struggled to grow and keep profits high.


### 🧾 **Final Takeaway**

Mercedes-Benz is still a strong and stable company, but like many businesses, it’s feeling the pressure of rising costs and slowing growth. Going forward, focusing on reducing unnecessary expenses and making smarter use of its resources could help bring profits back on track.

## 🛠️ **Tools Used**

- **Python** – Core language for analysis and visualization  
  - `pandas` for data manipulation  
  - `matplotlib` & `seaborn` for visualizing trends and ratios  
  - `yfinance` API to extract financial statements (MBG.DE)

- **Jupyter Notebook** – For combining code, visuals, and insights in one place  
- **VS Code** – For code editing and project organization  
- **Git & GitHub** – For version control and sharing the analysis

## **📊 Project Workflow**

1. **Data Extraction** – Collected financial statements using the `yfinance` API.  
2. **Data Cleaning** – Formatted dates, handled missing values, and structured data.   
3. **Ratio Analysis** – Calculated profitability, liquidity, solvency, and return ratios.  
4. **Visualization** – Created charts to highlight financial performance and structure.  
5. **Insights** – Interpreted trends and answered business questions.  
6. **Documentation** – Summarized findings in notebooks and this README.

*For steps 1 to 4* : [Click here](Notebooks/01_Data_Preparation.ipynb)

*For steps 5 and 6* : [Click here](Notebooks/02_Financial_Anlysis.ipynb)

## 📚 **What I Learned Along the Way**

This project wasn't just about numbers—it was about telling the story behind them.

- I used Python to dive deep into Mercedes-Benz’s financials, learning how to turn raw data into clear insights using `pandas`, `matplotlib`, and `seaborn`.

- Cleaning messy data reminded me that no good story starts without organizing the facts first.

- As I explored financial ratios, I began to see what makes a company strong, stable, or struggling—far beyond just reading numbers on a page.

- Automating data extraction with `yfinance` saved time and made the process smooth, helping me focus on what mattered: understanding the business behind the data.

## 🧗 **Challenges Faced**

Every project comes with its own learning curve, and this one was no exception. Here are a few challenges I encountered and how I tackled them:

- **📅 Dealing with Incorrect Labels**  
  One of the early issues I faced was with the year labels on my visualizations. The graphs were showing data from **2022 to 2025**, even though the actual financial data ranged from **2021 to 2024**. After some debugging, I discovered the problem was rooted in how the index was being interpreted after data transposition. Adjusting the index formatting resolved the inconsistency and ensured accurate representation.

- **🧩 Avoiding Code Redundancy**  
  As the analysis grew more complex, I realized I was repeating the same data-loading and preprocessing code across notebooks. To keep things clean and modular, I created a separate Python script (`prep_data.py`) and imported its functions into my notebook. This made the workflow more maintainable and professional.

- **🤔 Deciding What to Visualize**  
  With so much financial data available, it was tempting to visualize everything. But not every chart tells a meaningful story. One of the key challenges was filtering out noise and focusing only on visuals that added real analytical value—those that highlighted trends, answered business questions, or revealed deeper financial insights.

Each hurdle taught me something new—not just about coding, but about clarity, structure, and storytelling with data.




## **Explanation of some terms used in this project**
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










