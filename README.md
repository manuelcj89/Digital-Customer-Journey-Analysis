# Digital Customer Journey & Conversion Analysis

## Overview

This project analyses 12,330 online shopping sessions to identify factors associated with customer conversion and translate the findings into potential areas for commercial investigation.

The analysis combines SQL, Python/Pandas and statistical testing, covering visitor behaviour, traffic sources, customer segments and trends over different time-periods.

- Visitor type
- Traffic source
- Customer segments
- Monthly and weekly patterns
- Session engagement behaviour

The project also includes a data-quality investigation into duplicate records and unusual BounceRate/ExitRate patterns.

The aim is to demonstrate practical skills in **SQL, Python, data cleaning, exploratory analysis, visualisation and communicating data-driven insights**.


## Key Findings

- **Overall conversion rate:** 15.47% (1,908 of 12,330 sessions)
- **Visitor Type** New visitors converted at nearly double the rate of returning
  visitors (24.91% vs 13.93%) — a statistically significant difference (chi-square, p < 0.001)
- **Seasonality:** November had both the highest conversion rate (25.35%) and high     session volume while December fell to 12.51%
- **Weekday/weekend:** The pattern on conversion reverses depending on visitor
  type — significant for returning visitors, not for new visitors
- **Data quality:** 125 duplicate records were identified and investigated. They shared a distinctive low-engagement pattern, including unusual BounceRate/ExitRate values, but the dataset does not establish whether these represent a specific analytics-system behaviour or a data-quality issue.

## Recommendations

- **Investigate why returning visitors convert at a notably lower rate
  than new visitors.** The gap is large and consistent enough to be
  worth exploring further e.g. through site search behaviour, user 
  research etc. rather than assumed to be expected.

- **Treat traffic-source conversion differences as a starting point for
  further investigation when considering budget allocation.**
  Conversion rate alone doesn't account for cost, volume, or margin per
  channel. Combining these findings with marketing spend data would be
  needed before drawing conclusions about where to prioritise.

- **Explore what may explain the November conversion peak.** 
  Potentially seasonal demand, promotional activity, or another factor
  not captured in this dataset. A single year of data cannot confirm
  whether this is a recurring pattern.

- **Treat the weekday/weekend difference by visitor type as a
  hypothesis for new visitors specifically.** 
  This pattern was statistically significant for returning visitors
  only; the apparent new-visitor difference did not reach significance
  and may reflect sampling variation.

- **Request a mapping** for 'TrafficType', 'OperatingSystems', 'Browser'
  and 'Region' codes from the data owner, to allow the traffic-source
  findings to be interpreted against real-world channels.

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
└── requirements.txt