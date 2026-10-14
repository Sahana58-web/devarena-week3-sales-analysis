# Sales Data Analysis Report

## Project Overview
This report analyses a sales dataset (sales_data.csv) of 100 orders from 2024-01-01 to 2024-04-09. The goal is to find the total sales, the best-selling product and the best region using Python and pandas.

## Analysis Steps
1. **Load the data:** The CSV file was read with pandas (pd.read_csv). It has 100 rows and 7 columns: Date, Product, Quantity, Price, Customer_ID, Region and Total_Sales.
2. **Explore the data:** I checked the first 5 rows, the shape of the data and the data type of each column.
3. **Clean the data:** I checked for missing values and duplicate rows. There were none, so all 100 rows were kept. The Date column was converted from text to real dates.
4. **Calculate metrics:** I calculated total, average, highest and lowest sales, and used groupby to find sales by product and by region.
5. **Create the report:** The results are printed in a clean, formatted report.

## Key Findings
| Metric | Value |
|---|---|
| Total Orders | 100 |
| Total Sales | Rs.12,365,048 |
| Average Sale | Rs.123,650.48 |
| Highest Sale | Rs.373,932 |
| Lowest Sale | Rs.6,540 |

### Sales by Product
| Product | Total Sales (Rs.) |
|---|---|
| Laptop | 3,889,210 |
| Tablet | 2,884,340 |
| Phone | 2,859,394 |
| Headphones | 1,384,033 |
| Monitor | 1,348,071 |

### Sales by Region
| Region | Total Sales (Rs.) |
|---|---|
| North | 3,983,635 |
| South | 3,737,852 |
| East | 2,519,639 |
| West | 2,123,922 |

## Insights
- **Best-selling product:** Laptop is the best-selling product, with Rs.3,889,210 in sales (about 31% of all sales). It also sold the most units (136).
- **Best region:** North is the top region, with Rs.3,983,635 in sales (about 32% of all sales).
- **Weakest areas:** Monitor has the lowest sales among products, and West has the lowest sales among regions.
- **Opportunity:** Headphones sold the fewest units (48), so promotions on Headphones and Monitors could increase sales. The West region could also be a growth target.

## Conclusion
The dataset was clean, with no missing values or duplicates. Laptops and the North region drive the most revenue. This analysis shows how pandas can quickly turn raw sales data into useful business insights.
