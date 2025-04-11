# operation_olist
# Operation_Olise

A data-driven project analyzing **Olist**’s e-commerce business in Brazil to identify key drivers of **sales**, **repeat purchases**, and **online operational efficiency**. This repository outlines the **analysis**, **findings**, and **recommendations** based on the slides provided (`BT slides.pdf`). The .tableau files in the repository capture interactive visualizations and dashboards for deeper insights.

---

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Data Cleaning](#data-cleaning)  
3. [Analysis Focus](#analysis-focus)  
4. [Key Findings & Insights](#key-findings--insights)  
    - [Sales Drivers](#sales-drivers)  
    - [Repeat Purchases](#repeat-purchases)  
    - [Online Operations](#online-operations)  
5. [Recommendations](#recommendations)  
6. [How to Explore This Repo](#how-to-explore-this-repo)  
7. [License & Acknowledgments](#license--acknowledgments)

---

## Project Overview
**Olist** is an e-commerce platform connecting Brazilian merchants to major marketplaces. We analyzed **real-world data** (orders, products, reviews, deliveries, etc.) spanning 2016–2018 to address the following questions:

1. **Which factors drive product sales?**  
2. **How do shipping, freight, and location affect repeat purchases?**  
3. **What online operational elements (listings, images, payment methods) influence overall sales performance?**

Brazil’s e-commerce market has grown **significantly**, presenting both **opportunities** (large customer base) and **challenges** (logistical complexity in a vast country).

---

## Data Cleaning
1. **Row Removal**  
   - Omitted rows with critical nulls (e.g., missing `orders.csv` and `products.csv` data).  
   - Retained rows in `order_reviews.csv` when missing only non-critical attributes (e.g., review comment title).

2. **Category Renaming**  
   - Renamed product category attributes (e.g., `sports_leisure` → `Sports Leisure`) for clarity.

3. **Outlier Detection**  
   - **Freight Costs**: Removed extreme outliers (e.g., 1795, 1002 in the dataset) to focus on meaningful comparisons.

By refining the dataset, we ensured **reliable** insights without skewed or incomplete records.

---

## Analysis Focus
Our analysis centers on three main pillars:

1. **Operations & Sales**  
   - **Location & Category**: Identify top-selling product categories and regions.  
   - **Complementary Purchases**: Examine frequent multi-category orders.  
   - **Seasonality**: Explore monthly/quarterly sales trends (holiday peaks, back-to-school spikes).  
   - **Shipping & Freight Costs**: Investigate whether higher costs deter sales.

2. **Repeat Purchases**  
   - **Delivery Reliability**: On-time vs. early/late deliveries and their effect on repeat orders.  
   - **Geographic Factors**: Distribution hubs vs. remote regions and their correlation with loyalty.  
   - **Freight Cost Impact**: Relationship between high shipping costs and repeat purchase rates.

3. **Online Operations**  
   - **Product Listings**: Number of images, title length, and description length.  
   - **Payment Methods**: Credit card vs. others, multi-payment usage, installment plans.  
   - **Installments**: Potential to boost sales and average order value.

---

## Key Findings & Insights

### Sales Drivers
- **Top Product Categories**:  
  1. Bed & Bath Table  
  2. Health & Beauty  
  3. Sports & Leisure  
  4. Furniture & Decor  
  5. Computer Accessories  
  Together, these account for ~40% of all products sold.

- **Top Regions**:  
  - **São Paulo** (SP), **Rio de Janeiro** (RJ), and **Minas Gerais** (MG) make up ~66.7% of sales.  
  - Urban areas with higher GDP per capita tend to show **increased** sales volume.

- **Complementary Purchases**:  
  - Categories like **Bed & Bath Table + Furniture Decor** and **Home Comfort + Housewares** often appear together in multi-item orders, indicating potential bundling strategies.

- **Seasonality**:  
  - **Holiday Season (Nov–Dec)** sees spikes in Toys, Bed & Bath Table, Furniture & Decor.  
  - **Back-to-School (Jan–Feb)** drives Stationary & Computer Accessories.  
  - **Mid-year (Mar–Jul)** sees Housewares and Health & Beauty gains.

- **Freight Costs vs. Sales**:  
  - No direct linear correlation. **Price normalization** (freight-to-price ratio) shows that shipping cost alone isn’t a guaranteed barrier—other factors (e.g., brand, product category) also influence sales.

### Repeat Purchases
- **Delivery Reliability > Speed**:  
  - **On-time deliveries** have the **highest** repeat purchase rate (~5.67%).  
  - Early or late arrivals introduce uncertainty, reducing loyalty.

- **Geographic Proximity**:  
  - Customers in southern states near Olist’s HQ have higher repeat rates, correlating with lower freight costs and more reliable delivery times.

- **Freight Cost**:  
  - Repeat purchasers often see **lower** average freight costs. The difference isn’t enormous, but it’s consistent across the data.

- **Category Loyalty**:  
  - Smaller categories like **La Cuisine**, **Arts & Crafts**, and **Fashion: Children** show **high repeat-purchase proportions** (loyal niche customer bases).

### Online Operations
- **Number of Product Images**:  
  - ~6–7 images per listing optimizes customer interest (p < 0.01).  
  - More than 12 images sees diminishing returns due to small sample sizes.

- **Product Title & Description Length**:  
  - No clear “optimal” character count. Spikes observed likely outliers with specialized products.

- **Payment Preferences**:  
  - **Credit Cards** dominate (78.34% usage).  
  - **Installments** used in ~71% of total sales volume; also drive **70.2% higher** average order value.

- **Installment Duration**:  
  - No direct link between more months and higher order value—customers simply appreciate flexible payment.

---

## Recommendations

1. **Targeted Advertising**  
   - **Focus** on São Paulo, Rio de Janeiro, Minas Gerais.  
   - Highlight top categories in each region.

2. **Seasonal Promotions**  
   - **Holiday Season** (Nov–Dec): Toys, Bed & Bath Table, Furniture & Decor.  
   - **Back-to-School** (Jan–Feb): Stationary, Computers & Accessories.  
   - **Mar–Jul**: Housewares, Health & Beauty, Sports & Leisure.

3. **Bundled Discounts**  
   - Combine frequently co-purchased items (e.g., Bed & Bath Table + Furniture Decor).

4. **Logistics Optimization**  
   - **On-Time Delivery** is crucial. Minimize variance by partnering with reliable shippers.  
   - Establish distribution hubs near distant regions to reduce freight cost and speed up deliveries.

5. **Customer Loyalty Programs**  
   - Focus on categories showing strong repeat potential (La Cuisine, Arts & Crafts, Children’s Fashion).  
   - Offer region-specific incentives or shipping discounts to keep freight costs manageable.

6. **Listing Improvements**  
   - Enforce **minimum 3 product images**, recommend ~6–7 to boost buyer confidence.  
   - Consider A/B testing for advanced listing details.

7. **Installment & BNPL Options**  
   - Partner with local installment services (Cleo, ADDI, DiniePay).  
   - Market “Buy Now, Pay Later” to increase average order value and expand the customer base.

---

## How to Explore This Repo

1. **Slides**:  
   - `BT slides.pdf`: Detailed visuals and discussion points for the entire analysis.

2. **.tableau Files**:  
   - Interactive dashboards that illustrate shipping costs, seasonality, repeat purchases, etc.

3. **Data & Scripts**:  
   - If included, refer to `data/` folder for cleaned CSVs and code scripts used for deeper analysis.

4. **Recommendations Summary**:  
   - Review the final section in the slides or the bullets above to understand next steps.

---

## License & Acknowledgments
- **License**: This project is for educational and demonstration purposes.  
- **Acknowledgments**:  
  - Thank you to Olist for the open dataset and the Brazilian e-commerce context.  
  - Shoutout to the course instructors and teammates for guidance in data cleaning, analysis, and storytelling.

> **Disclaimer**: All insights are based on a provided dataset and may not reflect real-world shifts after the study period. Further validation with updated data is recommended.
