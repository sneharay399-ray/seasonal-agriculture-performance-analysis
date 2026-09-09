# Seasonal Agriculture Performance Analysis

A data-driven exploratory analysis of agricultural performance across the
Kharif, Rabi, and Zaid seasons, using a simulated farm-record dataset built
for this project. The analysis covers yield, profitability, environmental
conditions, resource use, correlations, statistical testing, a multivariate
regression, and outlier investigation.

## Project Overview

Agricultural performance changes across seasons due to differences in
rainfall, temperature, irrigation demand, and market conditions. This
project analyzes **2,600 farm-season records across 28 variables** (after
cleaning) to identify seasonal patterns, relationships, differences, and
unusual observations.

The analysis focuses on:
- Seasonal yield and production
- Revenue, cost, and profitability
- Rainfall, temperature, humidity, and soil conditions
- Fertilizer, pesticide, and water usage
- Water-use efficiency
- Disease and pest incidence
- Crop-wise seasonal performance
- State-wise seasonal performance
- Irrigation method and seasonal performance
- Correlation and multivariate relationships
- Statistical significance and outlier analysis

## Dataset

`seasonal_agriculture_dataset.csv` is a **synthetic dataset generated for
this project** (see `generate_dataset.py`) — it is not sourced from any
external or third-party dataset. It simulates:

- **Seasons:** Kharif, Rabi, Zaid
- **Crops:** Rice, Wheat, Maize, Soybean, Mustard, Barley, Sugarcane, Groundnut
- **States:** West Bengal, Bihar, Uttar Pradesh, Odisha, Assam, Jharkhand, Chhattisgarh, Punjab
- **Years:** 2021–2024
- **Records:** 2,625 (before cleaning) / 2,600 (after removing duplicates)
- **Variables:** 28

Missing values and duplicate rows were deliberately introduced so the
notebook includes a genuine data-cleaning step.

## Objectives

1. Explore and clean the dataset.
2. Compare agricultural performance across seasons.
3. Study relationships between environmental/resource factors and yield.
4. Compare crops, states, and irrigation methods across seasons.
5. Test statistical significance of seasonal differences.
6. Fit a multivariate regression model for yield.
7. Identify outliers and discuss their implications.
8. Generate evidence-based recommendations.

## Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- SciPy (ANOVA, Kruskal-Wallis)
- Scikit-learn (Linear Regression)
- Jupyter Notebook

## Methodology

1. **Data Preparation** — load data, inspect structure, impute missing
   values (median for numeric, mode for categorical), remove duplicates.
2. **Descriptive & Univariate Analysis** — summary statistics, distribution
   and boxplots.
3. **Seasonal Analysis** — compare yield, profit, and water efficiency
   across Kharif, Rabi, Zaid.
4. **Environmental & Risk Patterns** — rainfall, temperature, humidity,
   disease/pest incidence by season.
5. **Comparative Analysis** — Crop × Season, State × Season, Irrigation ×
   Season.
6. **Correlation Analysis** — Pearson correlation heatmap across
   environmental, resource, and outcome variables.
7. **Statistical Testing** — one-way ANOVA (yield across seasons),
   Kruskal-Wallis test (profit across seasons).
8. **Multivariate Regression** — linear regression predicting yield from
   environmental and resource variables.
9. **Outlier Analysis** — IQR-based detection on profit and yield.

## Key Findings

Exact figures are produced when the notebook runs (`Seasonal_Agriculture_Analysis.ipynb`),
including:
- Average yield, profit, and water efficiency by season
- Highest-yielding crop–season and state–season combinations
- ANOVA and Kruskal-Wallis test results for seasonal differences in yield and profit
- Regression coefficients and R² for the yield model
- Count and share of outlier records in profit and yield

## Recommendations

- Use season-specific benchmarks rather than a single annual average when
  planning crop selection and resource allocation.
- Prioritize irrigation upgrades (drip/sprinkler) where water efficiency is
  low.
- Monitor rainfall, temperature, and disease/pest incidence together,
  especially in the Kharif season.
- Investigate outlier records individually before using them for planning.
- Judge performance using yield **and** profitability together, since the
  two do not always move in the same direction.

## Limitations

- The dataset is synthetically generated for this project and is designed
  to resemble realistic agricultural patterns — it does not represent
  measured field data.
- Correlation and regression describe association, not causation.
- Outlier treatment choices can influence statistical results.
- Findings should not be generalized to real farms or regions without
  validation against actual agricultural data.

## Project Structure

```
Seasonal-Agriculture-Performance-Analysis/
│
├── Seasonal_Agriculture_Analysis.ipynb
├── generate_dataset.py
├── seasonal_agriculture_dataset.csv
└── README.md
```

## How to Run

1. Clone/download the project files.
2. (Optional) Run `python generate_dataset.py` to regenerate the dataset.
3. Open `Seasonal_Agriculture_Analysis.ipynb` in Jupyter Notebook or Google
   Colab.
4. Make sure `seasonal_agriculture_dataset.csv` is in the same working
   directory.
5. Run the notebook cells from top to bottom.

## Author

**Sneha**
BBA, Dinabandhu Andrews Institute of Technology & Management, Kolkata
