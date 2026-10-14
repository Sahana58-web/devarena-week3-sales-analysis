# Sales Data Analysis
# This program loads sales data, cleans it, calculates metrics and prints a report

import pandas as pd

# Step 1: Load the data (a CSV file is like an Excel sheet)
df = pd.read_csv('sales_data.csv')

# Step 2: Explore the data
print("=" * 45)
print("STEP 1: DATA EXPLORATION")
print("=" * 45)
print("First 5 rows:")
print(df.head())
print()
print("Rows and columns:", df.shape)
print()
print("Data types:")
print(df.dtypes)

# Step 3: Clean the data
print()
print("=" * 45)
print("STEP 2: DATA CLEANING")
print("=" * 45)
print("Missing values in each column:")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

df = df.dropna()              # remove rows with missing values (if any)
df = df.drop_duplicates()     # remove duplicate rows (if any)
df['Date'] = pd.to_datetime(df['Date'])   # convert Date text into real dates
print("Rows after cleaning:", len(df))

# Step 4: Calculate metrics
total_sales = df['Total_Sales'].sum()
average_sale = df['Total_Sales'].mean()
highest_sale = df['Total_Sales'].max()
lowest_sale = df['Total_Sales'].min()

sales_by_product = df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False)
best_product = sales_by_product.index[0]

units_by_product = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)
most_units_product = units_by_product.index[0]

sales_by_region = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
best_region = sales_by_region.index[0]

# Step 5: Print the final report
print()
print("=" * 45)
print("SALES ANALYSIS REPORT")
print("=" * 45)
print(f"Period: {df['Date'].min().date()} to {df['Date'].max().date()}")
print(f"Total Orders: {len(df)}")
print()
print(f"Total Sales: Rs.{total_sales:,.2f}")
print(f"Average Sale: Rs.{average_sale:,.2f}")
print(f"Highest Sale: Rs.{highest_sale:,.2f}")
print(f"Lowest Sale: Rs.{lowest_sale:,.2f}")
print()
print(f"Best-Selling Product (by revenue): {best_product}")
print(f"Most Units Sold: {most_products if False else most_units_product} ({units_by_product.iloc[0]} units)")
print(f"Best Region: {best_region}")
print()
print("Sales by Product:")
for product, amount in sales_by_product.items():
    print(f"  {product}: Rs.{amount:,.2f}")
print()
print("Sales by Region:")
for region, amount in sales_by_region.items():
    print(f"  {region}: Rs.{amount:,.2f}")
