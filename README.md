# Digital Customer Journey & Conversion Analysis

## Overview

This project analyses online shopping session data to investigate what factors are associated with customer conversion.

The analysis uses SQL and Python to explore conversion performance across:

- Visitor type
- Traffic source
- Customer segments
- Monthly and weekly patterns
- Session engagement behaviour

The project also includes a data-quality investigation into duplicate records and unusual BounceRate/ExitRate patterns.

The aim is to demonstrate practical skills in **SQL, Python, data cleaning, exploratory analysis, visualisation and communicating data-driven insights**.


## Key Findings

- Overall conversion rate: **15.47%** (1,908 of 12,330 sessions)
- New visitors converted at nearly double the rate of returning visitors
  (24.91% vs 13.93%) — a statistically significant difference (chi-square, p < 0.001)
- November had both the highest conversion rate (25.35%) and high session
  volume, consistent with Black Friday/Cyber Monday activity
- The weekday/weekend effect on conversion reverses depending on visitor
  type — significant for returning visitors, not for new visitors
- 125 duplicate records were investigated and found to represent a
  distinct low-engagement session pattern rather than a data error


## Business Questions

The analysis focuses on several questions:

1. What is the overall conversion rate?
2. Do new and returning visitors convert at different rates?
3. Does conversion performance vary by traffic source?
4. Are particular combinations of visitor type and traffic source associated with higher conversion?
5. Does conversion performance vary by month or day of the week?
6. Are there data-quality issues that could affect the analysis?
7. What insights could be investigated further with additional customer and commercial data?


## Dataset

The project uses the **Online Shoppers Purchasing Intention Dataset**, containing **12,330 online shopping sessions**.

Each row represents a shopping session and includes behavioural, traffic and visitor characteristics together with a binary `Revenue` outcome indicating whether the session resulted in a purchase.

Key variables include:

- `VisitorType`
- `TrafficType`
- `Month`
- `Weekend`
- `BounceRates`
- `ExitRates`
- `PageValues`
- `ProductRelated`
- `ProductRelated_Duration`
- `Revenue`

The dataset is used for analytical and portfolio purposes.

## Tools & Technologies

- **Python**
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **SQL**
- **SQLite**
- **Jupyter Notebook**
- **VS Code**
- **Git / GitHub**


## Project Structure

```text
digital-customer-journey-analysis/
│
├── data/
│   └── online_shoppers_intention.csv
│
├── database/
│   └── shoppers.db
│
├── notebooks/
│   └── digital_customer_journey_analysis.ipynb
│
├── sql/
│   └── SQL analysis queries
│
├── src/
│   └── Python analysis scripts
│
├── README.md
└── .gitignore
└── requirement.txt