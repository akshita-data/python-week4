import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# STEP 1: LOAD DATA
# -------------------------------
df = pd.read_csv("sales_data.csv", encoding="latin1")

# Clean column names
df.columns = df.columns.str.strip()
df.columns = df.columns.str.upper()

print("\nColumns:\n", df.columns)

# -------------------------------
# STEP 2: CLEAN DATA
# -------------------------------
df.fillna(df.mean(numeric_only=True), inplace=True)
df.fillna(df.mode().iloc[0], inplace=True)
df.drop_duplicates(inplace=True)

# -------------------------------
# STEP 3: ANALYSIS
# -------------------------------
sales_col = "TOTAL_SALES"

total_sales = df[sales_col].sum()
avg_sales = df[sales_col].mean()

# Sales by product
sales_by_product = df.groupby("PRODUCT")[sales_col].sum()

# Sales by region
sales_by_region = df.groupby("REGION")[sales_col].sum()

# Convert date
df["DATE"] = pd.to_datetime(df["DATE"])

# Monthly sales
df["MONTH"] = df["DATE"].dt.to_period("M")
monthly_sales = df.groupby("MONTH")[sales_col].sum()

# -------------------------------
# STEP 4: REPORT 
# -------------------------------
print("\n===== FINAL REPORT =====")
print(f"Total Revenue: {total_sales:.2f}")
print(f"Average Sales: {avg_sales:.2f}")
print(f"Best Product: {sales_by_product.idxmax()}")
print(f"Best Region: {sales_by_region.idxmax()}")

# -------------------------------
# STEP 5: VISUALIZATION
# -------------------------------

# 📊 1. BAR CHART (Top Products)
sales_by_product.sort_values(ascending=False).head(10).plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 📊 2. PIE CHART (Region Distribution)
sales_by_region.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.show()

# 📈 3. LINE CHART (Monthly Sales Trend)
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid()
plt.show()

# -------------------------------
# STEP 6: INSIGHTS
# -------------------------------
print("\n===== INSIGHTS =====")
print(f"Total revenue generated is {total_sales:.2f}")
print(f"Top product is {sales_by_product.idxmax()}")
print(f"Top region is {sales_by_region.idxmax()}")
print("Sales show trends over time (see line chart)")