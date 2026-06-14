# Superstore Sales Analytics Report

**Prepared by:** Aniket [Last Name]  
**Date:** June 2026  
**Tools Used:** Python (Pandas, Matplotlib), Microsoft Excel

---

## Executive Summary

This report analyzes the Superstore sales dataset to assess revenue performance, profitability, product concentration, regional contribution, and customer segment value. The dataset contains 9,994 transactions spanning 2014-01-03 through 2017-12-30, providing a four-year view of commercial performance across the United States.

Overall sales reached **$2,297,200.86** with total profit of **$286,397.02**, resulting in a profit margin of **12.47%**. Performance is concentrated in a small number of regions, categories, and products, while the data also shows clear seasonal uplift in the final quarter of each year.

The West region is the strongest commercial market, and the Consumer segment is the largest customer base by both sales and order volume. At the product level, several Technology and Furniture items drive a disproportionate share of revenue, but some Furniture sub-categories continue to suppress profitability.

Management attention should focus on strengthening high-margin categories, reducing losses in underperforming sub-categories, and replicating the commercial patterns visible in the best-performing region and customer segment.

---

## Objective

This report answers the following business questions:

- How has sales and profit performance evolved over time?
- Which regions contribute most to revenue and profitability?
- Which categories and sub-categories create value, and which erode margin?
- Which products are the main revenue drivers?
- Which customer segment is most commercially valuable?
- What actions should management prioritize to improve profitability and growth?

---

## Dataset Overview

| Attribute | Details |
|---|---|
| Source | `Sample - Superstore.csv` |
| File location | `data/Sample - Superstore.csv` |
| Records | 9,994 |
| Columns | 21 |
| Time period covered | 2014-01-03 to 2017-12-30 |
| Geographic scope | United States |
| Primary measures | Sales, Quantity, Discount, Profit |

The dataset includes order, customer, geography, product, and financial fields. For analysis purposes, the report also uses a derived monthly period field and a profit margin metric defined as Profit divided by Sales.

---

## Key Performance Indicators (KPIs)

| KPI | Value |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Profit Margin % | 12.47% |
| Total Orders | 5,009 |

---

## Analysis & Findings

### Monthly Sales Trend

Monthly performance shows a strong seasonal pattern, with the most significant sales uplift occurring in the final quarter of the year. The highest sales month in the dataset was **November 2017** at **$118,447.83**, while the highest profit month was **December 2016** at **$17,885.31**.

This pattern indicates that demand accelerates materially in the year-end period, likely due to commercial planning cycles, promotional activity, and enterprise purchasing behavior. Profitability is less stable than sales and can be pressured in weaker months, including some early-year periods.

### Region Performance

The **West** region is the leading performer, generating **$725,457.82** in sales and **$108,418.45** in profit. The **East** region follows closely in sales and remains a strong profit contributor. The **Central** region performs moderately, while the **South** region is the weakest on both sales and profit.

This suggests that commercial strength is not evenly distributed across the business footprint. The West region appears to combine scale and profitability more effectively than the other geographies.

| Region | Sales | Profit |
|---|---:|---:|
| West | $725,457.82 | $108,418.45 |
| East | $678,781.24 | $91,522.78 |
| Central | $501,239.89 | $39,706.36 |
| South | $391,721.91 | $46,749.43 |

### Category & Sub-Category Breakdown

At the category level, **Technology** and **Furniture** contain the highest revenue-generating sub-categories. The strongest sub-categories include **Phones**, **Chairs**, **Storage**, **Binders**, and **Accessories**. Among these, Phones and Chairs are especially significant revenue contributors.

Profitability varies sharply within categories. The most notable loss-making sub-categories are **Tables** and **Bookcases** in Furniture, along with **Supplies** in Office Supplies. These areas reduce total margin and should be reviewed for discounting, pricing, and product mix issues.

| Category | Sub-Category | Sales | Profit |
|---|---|---:|---:|
| Technology | Phones | $330,007.05 | $44,515.73 |
| Furniture | Chairs | $328,449.10 | $26,590.17 |
| Office Supplies | Storage | $223,843.61 | $21,278.83 |
| Furniture | Tables | $206,965.53 | -$17,725.48 |
| Office Supplies | Binders | $203,412.73 | $30,221.76 |
| Technology | Machines | $189,238.63 | $3,384.76 |
| Technology | Accessories | $167,380.32 | $41,936.64 |
| Technology | Copiers | $149,528.03 | $55,617.82 |
| Furniture | Bookcases | $114,880.00 | -$3,472.56 |
| Office Supplies | Appliances | $107,532.16 | $18,138.01 |

### Top 10 Products by Sales

Revenue is concentrated in a small number of high-value products, many of which sit in Technology and premium Furniture segments. The leading product is **Canon imageCLASS 2200 Advanced Copier**, with sales of **$61,599.82**.

The top 10 products demonstrate that a limited number of large-ticket items contribute significantly to revenue performance. This concentration creates both opportunity and risk: these products are strong growth levers, but the business also depends on them disproportionately.

| Rank | Product | Sales |
|---|---|---:|
| 1 | Canon imageCLASS 2200 Advanced Copier | $61,599.82 |
| 2 | Fellowes PB500 Electric Punch Plastic Comb Binding Machine with Manual Bind | $27,453.38 |
| 3 | Cisco TelePresence System EX90 Videoconferencing Unit | $22,638.48 |
| 4 | HON 5400 Series Task Chairs for Big and Tall | $21,870.58 |
| 5 | GBC DocuBind TL300 Electric Binding System | $19,823.48 |
| 6 | GBC Ibimaster 500 Manual ProClick Binding System | $19,024.50 |
| 7 | Hewlett Packard LaserJet 3310 Copier | $18,839.69 |
| 8 | HP Designjet T520 Inkjet Large Format Printer - 24" Color | $18,374.90 |
| 9 | GBC DocuBind P400 Electric Binding System | $17,965.07 |
| 10 | High Speed Automatic Electric Letter Opener | $17,030.31 |

### Customer Segment Analysis

The **Consumer** segment is the most valuable customer base, delivering **$1,161,401.24** in sales, **$134,119.21** in profit, and **2,586** orders. **Corporate** is the second-largest segment, followed by **Home Office**.

This confirms that Consumer customers dominate demand volume, while Corporate customers remain an important secondary source of profitability. Home Office contributes less volume but still provides meaningful margin support.

| Segment | Sales | Profit | Order Count |
|---|---:|---:|---:|
| Consumer | $1,161,401.24 | $134,119.21 | 2,586 |
| Corporate | $706,146.44 | $91,979.13 | 1,514 |
| Home Office | $429,653.14 | $60,298.68 | 909 |

---

## Key Insights

- The business generates strong year-end revenue spikes, with November consistently emerging as the strongest sales period.
- The West region is the most attractive market overall, combining the highest sales with the highest profit.
- Technology delivers some of the strongest individual product and sub-category economics, especially through copiers, accessories, and phones.
- Furniture contains meaningful revenue but also the clearest margin leakage, especially in Tables and Bookcases.
- The Consumer segment is the commercial engine of the business, accounting for the largest share of orders, sales, and profit.

---

## Recommendations

1. Prioritize margin recovery in loss-making Furniture sub-categories by reviewing discount policy, pricing discipline, and product assortment.
2. Double down on high-performing Technology items by protecting stock availability, strengthening promotion strategy, and using them as anchor products.
3. Replicate the West region playbook in weaker regions, especially by examining channel execution, customer mix, and local product preference.
4. Build a fourth-quarter growth plan to capitalize on the annual demand peak and improve inventory readiness ahead of the season.
5. Segment Consumer and Corporate customers with differentiated campaigns, since their purchase patterns and value profiles are not identical.

---

## Conclusion

The Superstore dataset shows a business with solid revenue scale, moderate profitability, and clear concentration in a small number of regions, product groups, and customer segments. The West region, Technology products, and the Consumer segment are the strongest drivers of commercial performance.

At the same time, the analysis highlights margin pressure in specific Furniture sub-categories and uneven geographic performance. These issues represent the clearest opportunities for management action.

With tighter pricing control, stronger regional execution, and more disciplined portfolio management, the business can improve profitability without sacrificing growth.