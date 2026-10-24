import pandas as pd

# Load the dataset
df = pd.read_csv("data/Sample - Superstore.csv", encoding="latin1")

# Display the first 5 rows
print(df.head())

# Display all column names
print("\nColumn Names:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Calculate overall sales and profit
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

print("\n--- Overall Business Performance ---")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")

# Calculate average sales and profit
print(f"Average Sales: ${df['Sales'].mean():,.2f}")
print(f"Average Profit: ${df['Profit'].mean():,.2f}")

# Sales and profit by category
category_analysis = df.groupby("Category")[["Sales", "Profit"]].sum()

print("\n--- Category-wise Sales and Profit ---")
print(category_analysis.sort_values(by="Profit", ascending=False))
import matplotlib.pyplot as plt

# Calculate sales and profit by category
category_analysis = df.groupby("Category")[["Sales", "Profit"]].sum()

# Create a bar chart
category_analysis.plot(kind="bar", figsize=(9, 5))

plt.title("Sales and Profit by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Amount ($)")
plt.xticks(rotation=0)
plt.tight_layout()

# Save the chart
plt.savefig("category_sales_profit.png")
plt.show()
# Find the top 10 products by sales
top_products = df.groupby("Product Name")["Sales"].sum()

top_products = top_products.sort_values(ascending=False).head(10)

print("\n--- Top 10 Best-Selling Products ---")
print(top_products)
# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Extract month and year
df["Month"] = df["Order Date"].dt.to_period("M")

# Calculate monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n--- Monthly Sales ---")
print(monthly_sales)

# Plot monthly sales
monthly_sales.plot(figsize=(12, 5), marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("monthly_sales_trend.png")
plt.show()
# Find the top 10 products by profit
top_profit_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n--- Top 10 Most Profitable Products ---")
print(top_profit_products)

# Analyze sales and profit by region
region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum()

print("\n--- Regional Sales and Profit ---")
print(region_analysis.sort_values(by="Profit", ascending=False))

# Plot regional performance
region_analysis.plot(kind="bar", figsize=(8, 5))

plt.title("Sales and Profit by Region")
plt.xlabel("Region")
plt.ylabel("Amount ($)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("regional_sales_profit.png")
plt.show()
# Analyze profit by subcategory
subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n--- Profit by Subcategory ---")
print(subcategory_profit)

print("\nMost Profitable Subcategory:")
print(subcategory_profit.idxmax())

print("\nLeast Profitable Subcategory:")
print(subcategory_profit.idxmin())