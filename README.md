# Vendor-Performance
Personal data analysis project using Python and statistical methods to assess vendor performance, optimise pricing strategies, and improve inventory efficiency.
# Vendor Performance Report

## Project Overview
This personal project explores vendor and product-level performance in a retail dataset using Python and Power BI. The goal is to generate actionable insights through exploratory data analysis, statistical methods, and visual storytelling.

## Business Context
Retail profitability depends on effective inventory and vendor management. This project investigates vendor contributions to revenue and gross profit, analyzes the impact of bulk purchasing, and identifies inefficiencies in inventory turnover and pricing. Insights from the analysis can help inform pricing strategy, vendor diversification, and stock optimization.

## Objectives
- Identify underperforming brands for promotional or pricing adjustments.
- Highlight top vendors by contribution to sales and profit.
- Evaluate the impact of bulk purchasing on unit cost savings.
- Identify low-turnover inventory that ties up capital and space.
- Statistically validate differences in profitability across vendor groups.

## Tech Stack
- Python
- pandas
- matplotlib / seaborn
- scipy.stats
- SQLite (via SQLAlchemy)
- Jupyter Notebook
- Power BI

## Files and Scripts

| File | Purpose |
|------|--------|
| `Exploratory Data Analysis.ipynb` | Perform initial EDA, summary statistics, and correlation analysis |
| `Vendor Performance Analysis.ipynb` | Generate vendor-level insights, comparisons, and hypothesis testing |
| `scripts/ingestion.py` | Load raw CSV files into a SQLite database |
| `scripts/get_vendor_summary.py` | Aggregate and store summary tables for reporting |
| `report/Vendor Performance Report.pdf` | Final formatted report summarizing analysis, visuals, and recommendations |
| `dashboard/VendorPerformance.pbix` | Power BI dashboard for interactive visualization of key metrics |

## Key Visualizations

> *(Ensure these images are saved in a `visuals/` or `output/` folder and embedded here once committed)*

- Sales vs. Gross Profit by Vendor
- Inventory Turnover Distribution
- Unit Cost vs. Bulk Purchase Size
- Profit Margin Distribution for Top vs. Low Vendors
- Correlation Heatmaps

## Insights & Recommendations Summary

- 198 brands with high margins but low volume are ideal candidates for promotional campaigns.
- Top 10 vendors contribute nearly 66% of total purchases, suggesting a need to diversify supplier risk.
- Bulk purchasing reduces unit costs by up to 72%, supporting cost-efficient procurement strategies.
- $2.71 million in unsold inventory represents a major holding cost, requiring clearance or demand forecasting adjustments.
- T-tests confirm statistically significant differences in profit margins across vendor groups, indicating the need for tailored pricing strategies.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Vendor-Performance.git
   cd vendor-performance-report

