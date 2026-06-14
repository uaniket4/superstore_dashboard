"""Generate a PDF report from the saved Superstore analysis charts."""

# Section: Import the libraries needed to assemble the PDF report and render chart images.
from datetime import date
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd


# Section: Define the input and output locations used by the report generator.
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "Sample - Superstore.csv"
OUTPUT_DIR = BASE_DIR / "output"
PDF_PATH = OUTPUT_DIR / "Superstore_Sales_Report.pdf"


# Section: Load the dataset and compute the summary values shown on the title page.
def load_summary() -> dict:
    df = pd.read_csv(
        DATA_PATH,
        encoding="latin-1",
        parse_dates=["Order Date", "Ship Date"],
    )
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    profit_margin = 0 if total_sales == 0 else (total_profit / total_sales) * 100

    return {
        "rows": len(df),
        "orders": df["Order ID"].nunique(),
        "sales": total_sales,
        "profit": total_profit,
        "profit_margin": profit_margin,
        "date_min": df["Order Date"].min(),
        "date_max": df["Order Date"].max(),
    }


# Section: Build a title page that introduces the report and summarizes the dataset.
def add_title_page(pdf: PdfPages, summary: dict) -> None:
    fig = plt.figure(figsize=(8.27, 11.69))
    fig.patch.set_facecolor("white")

    fig.text(0.5, 0.88, "Superstore Sales Analytics Report", ha="center", va="center", fontsize=22, fontweight="bold")
    fig.text(0.5, 0.82, f"Generated on {date.today().strftime('%B %d, %Y')}", ha="center", va="center", fontsize=12)

    summary_text = (
        f"Rows: {summary['rows']:,}\n"
        f"Unique Orders: {summary['orders']:,}\n"
        f"Total Sales: {summary['sales']:,.2f}\n"
        f"Total Profit: {summary['profit']:,.2f}\n"
        f"Overall Profit Margin: {summary['profit_margin']:,.2f}%\n"
        f"Order Date Range: {summary['date_min'].date()} to {summary['date_max'].date()}"
    )
    fig.text(0.5, 0.62, summary_text, ha="center", va="center", fontsize=14, linespacing=1.8)
    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


# Section: Add a chart image to the PDF as a full-page display.
def add_image_page(pdf: PdfPages, image_path: Path, title: str) -> None:
    image = plt.imread(image_path)
    fig, ax = plt.subplots(figsize=(8.27, 11.69))
    ax.imshow(image)
    ax.set_title(title, fontsize=16, pad=12)
    ax.axis("off")
    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


# Section: Add a plain text page with placeholder insight bullets for manual completion.
def add_key_insights_page(pdf: PdfPages) -> None:
    fig = plt.figure(figsize=(8.27, 11.69))
    fig.patch.set_facecolor("white")

    fig.text(0.08, 0.92, "Key Insights", fontsize=20, fontweight="bold", ha="left")
    bullet_text = (
        "• Placeholder insight 1: ________________________________\n\n"
        "• Placeholder insight 2: ________________________________\n\n"
        "• Placeholder insight 3: ________________________________\n\n"
        "• Placeholder insight 4: ________________________________\n\n"
        "• Placeholder insight 5: ________________________________"
    )
    fig.text(0.1, 0.8, bullet_text, fontsize=13, va="top", ha="left", linespacing=1.6)
    pdf.savefig(fig, bbox_inches="tight")
    plt.close(fig)


# Section: Assemble the complete PDF report from the summary page and saved chart images.
def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    summary = load_summary()
    chart_files = [
        (OUTPUT_DIR / "01_monthly_sales_profit_trend.png", "Monthly Sales & Profit Trend"),
        (OUTPUT_DIR / "02_region_performance.png", "Region Performance"),
        (OUTPUT_DIR / "03_category_subcategory_breakdown.png", "Category & Sub-Category Breakdown"),
        (OUTPUT_DIR / "04_top_10_products_by_sales.png", "Top 10 Products by Sales"),
        (OUTPUT_DIR / "05_customer_segment_analysis.png", "Customer Segment Analysis"),
    ]

    with PdfPages(PDF_PATH) as pdf:
        add_title_page(pdf, summary)
        for image_path, title in chart_files:
            add_image_page(pdf, image_path, title)
        add_key_insights_page(pdf)

    print(f"Saved report to {PDF_PATH}")


if __name__ == "__main__":
    main()