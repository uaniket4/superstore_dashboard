"""Build core Superstore sales analysis charts and summary metrics."""

# Section: Import the libraries needed for data processing and chart creation.
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd


# Section: Define the input and output locations used by the analysis script.
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "Sample - Superstore.csv"
OUTPUT_DIR = BASE_DIR / "output"


# Section: Load the CSV, parse the date columns, and add the required derived fields.
def load_data() -> pd.DataFrame:
    df = pd.read_csv(
        DATA_PATH,
        encoding="latin-1",
        parse_dates=["Order Date", "Ship Date"],
    )
    df["Month"] = df["Order Date"].dt.to_period("M")
    df["Profit Margin"] = (df["Profit"] / df["Sales"].replace(0, pd.NA)).fillna(0)
    return df


# Section: Save the monthly sales and profit trend as a dual line chart.
def plot_monthly_trend(df: pd.DataFrame) -> None:
    monthly = (
        df.groupby("Month", as_index=False)[["Sales", "Profit"]]
        .sum()
        .sort_values("Month")
    )
    x_values = monthly["Month"].astype(str)

    fig, ax = plt.subplots(figsize=(13, 7))
    ax.plot(x_values, monthly["Sales"], marker="o", linewidth=2.5, label="Sales", color="#1f77b4")
    ax.plot(x_values, monthly["Profit"], marker="o", linewidth=2.5, label="Profit", color="#ff7f0e")
    ax.set_title("Monthly Sales & Profit Trend")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount")
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "01_monthly_sales_profit_trend.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# Section: Save the region performance chart as side-by-side horizontal bars sorted by sales.
def plot_region_performance(df: pd.DataFrame) -> None:
    region = df.groupby("Region", as_index=False)[["Sales", "Profit"]].sum().sort_values("Sales", ascending=False)
    positions = range(len(region))
    bar_height = 0.35

    fig, ax = plt.subplots(figsize=(11, 6.5))
    ax.barh([p - bar_height / 2 for p in positions], region["Sales"], height=bar_height, label="Sales", color="#4c78a8")
    ax.barh([p + bar_height / 2 for p in positions], region["Profit"], height=bar_height, label="Profit", color="#f58518")
    ax.set_yticks(list(positions))
    ax.set_yticklabels(region["Region"])
    ax.set_title("Region Performance")
    ax.set_xlabel("Amount")
    ax.grid(axis="x", alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "02_region_performance.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# Section: Save the category and sub-category breakdown with negative profit bars highlighted in red.
def plot_category_subcategory_breakdown(df: pd.DataFrame) -> None:
    breakdown = (
        df.groupby(["Category", "Sub-Category"], as_index=False)[["Sales", "Profit"]]
        .sum()
        .assign(Label=lambda frame: frame["Category"] + " - " + frame["Sub-Category"])
        .sort_values("Sales", ascending=True)
    )
    positions = range(len(breakdown))
    bar_height = 0.35
    profit_colors = ["#d62728" if value < 0 else "#2ca02c" for value in breakdown["Profit"]]

    fig, ax = plt.subplots(figsize=(14, max(7, 0.4 * len(breakdown))))
    ax.barh([p - bar_height / 2 for p in positions], breakdown["Sales"], height=bar_height, label="Sales", color="#1f77b4")
    ax.barh([p + bar_height / 2 for p in positions], breakdown["Profit"], height=bar_height, label="Profit", color=profit_colors)
    ax.set_yticks(list(positions))
    ax.set_yticklabels(breakdown["Label"])
    ax.set_title("Category & Sub-Category Breakdown")
    ax.set_xlabel("Amount")
    ax.grid(axis="x", alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "03_category_subcategory_breakdown.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# Section: Save the top 10 products by sales as a horizontal bar chart.
def plot_top_products(df: pd.DataFrame) -> None:
    top_products = (
        df.groupby("Product Name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
        .sort_values("Sales", ascending=True)
    )

    fig, ax = plt.subplots(figsize=(14, 8))
    ax.barh(top_products["Product Name"], top_products["Sales"], color="#4c78a8")
    ax.set_title("Top 10 Products by Sales")
    ax.set_xlabel("Sales")
    ax.set_ylabel("Product Name")
    ax.grid(axis="x", alpha=0.25)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "04_top_10_products_by_sales.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# Section: Save the customer segment analysis as a grouped bar chart for sales, profit, and order count.
def plot_segment_analysis(df: pd.DataFrame) -> None:
    segment = (
        df.groupby("Segment", as_index=False)
        .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"), Order_Count=("Order ID", "nunique"))
        .sort_values("Sales", ascending=False)
    )
    x_positions = range(len(segment))
    bar_width = 0.25

    fig, ax = plt.subplots(figsize=(11, 6.5))
    ax.bar([x - bar_width for x in x_positions], segment["Sales"], width=bar_width, label="Sales", color="#4c78a8")
    ax.bar(x_positions, segment["Profit"], width=bar_width, label="Profit", color="#f58518")
    ax.bar([x + bar_width for x in x_positions], segment["Order_Count"], width=bar_width, label="Order Count", color="#54a24b")
    ax.set_xticks(list(x_positions))
    ax.set_xticklabels(segment["Segment"])
    ax.set_title("Customer Segment Analysis")
    ax.set_ylabel("Value")
    ax.grid(axis="y", alpha=0.25)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "05_customer_segment_analysis.png", dpi=200, bbox_inches="tight")
    plt.close(fig)


# Section: Print a concise overall summary for the dataset after the charts are created.
def print_summary(df: pd.DataFrame) -> None:
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    overall_profit_margin = 0 if total_sales == 0 else (total_profit / total_sales) * 100
    total_orders = df["Order ID"].nunique()

    print(f"Total Sales: {total_sales:,.2f}")
    print(f"Total Profit: {total_profit:,.2f}")
    print(f"Overall Profit Margin %: {overall_profit_margin:,.2f}%")
    print(f"Total Orders: {total_orders:,}")


# Section: Run the full analysis workflow when the script is executed directly.
def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = load_data()

    plot_monthly_trend(df)
    plot_region_performance(df)
    plot_category_subcategory_breakdown(df)
    plot_top_products(df)
    plot_segment_analysis(df)
    print_summary(df)


if __name__ == "__main__":
    main()