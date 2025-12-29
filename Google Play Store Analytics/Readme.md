# Google Play Store Analytics

## Project Overview

This repository contains a Jupyter Notebook that performs an end-to-end exploratory data analysis (EDA) and basic modeling on **Google Play Store app data**. The goal is to understand app market trends, user preferences, pricing strategies, and factors influencing app ratings and installs.

The notebook walks through data inspection, cleaning, visualization, and feature-driven insights that can help developers and product teams make data-informed decisions.

---

## Key Objectives

* Analyze app categories, ratings, reviews, installs, and pricing
* Identify patterns affecting app popularity and user engagement
* Explore relationships between ratings, reviews, installs, and app size
* Prepare data for basic machine learning experiments

---

## Dataset

The dataset used in this notebook is the **Google Play Store Apps dataset**, which typically includes:

* App name
* Category
* Rating
* Reviews
* Size
* Installs
* Type (Free / Paid)
* Price
* Content rating
* Genres

> Dataset quality issues such as missing values, inconsistent formats, and outliers are handled during preprocessing.

---

## Tools & Libraries Used

* **Python**
* **Pandas** – data manipulation and cleaning
* **NumPy** – numerical computations
* **Plotly** – interactive visualizations
* **Scikit-learn** – basic preprocessing and modeling utilities

---

## Notebook Workflow

### 1. Initial Inspection

* Load and preview the dataset.
* Understand data types and structure.
* Identify missing and inconsistent values.

### 2. Data Cleaning & Preprocessing

* Handle missing ratings and reviews.
* Convert installs and price into numeric formats.
* Remove or treat outliers.
* Encode categorical variables where needed.

### 3. Exploratory Data Analysis (EDA)

* Category-wise app distribution.
* Rating distribution across categories.
* Free vs Paid app comparisons.
* Relationship between installs, reviews, and ratings.
* Price impact on ratings and installs.

### 4. Feature Preparation & Modeling (Introductory)

* Feature selection and scaling.
* Train-test split.
* Applying basic machine learning models for insight exploration.

---

## Key Insights

* Free apps dominate the Play Store ecosystem.
* Certain categories consistently achieve higher ratings.
* Apps with higher reviews generally correlate with higher installs.
* Paid apps tend to have higher ratings but significantly fewer installs.

---

## How to Run the Notebook

1. Clone this repository

   ```bash
   git clone https://github.com/your-username/google-play-store-analytics.git
   ```
2. Navigate to the project directory

   ```bash
   cd google-play-store-analytics
   ```
3. Install dependencies

   ```bash
   pip install pandas numpy plotly scikit-learn
   ```
4. Launch Jupyter Notebook

   ```bash
   jupyter notebook
   ```
5. Open and run `google-play-store-analytics.ipynb`

---

Kaggle Link- https://www.kaggle.com/code/omshah117/google-play-store-analytics

---

## Future Improvements

* Advanced feature engineering.
* Predictive modeling for app success.
* Time-series analysis (if temporal data is available).
* Deployment of insights via dashboards.

---

⭐ If you find this project helpful, consider giving it a star!
