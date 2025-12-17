Google Play Store Analytics & Rating Prediction
This project performs an extensive exploratory data analysis (EDA) and builds machine learning models to predict app ratings using the Google Play Store dataset. It utilizes interactive visualizations to uncover market trends and evaluates predictive performance using Random Forest and XGBoost.

📊 Project Overview
The notebook explores a dataset of over 10,000 apps to understand the factors that drive popularity and high user ratings. Key phases include:

Data Cleaning: Handling malformed entries, normalizing app sizes (MB/kB to bytes), and cleaning numeric fields like Installs and Price.

Exploratory Data Analysis (EDA): Using Plotly for interactive 2D and 3D visualizations.

Machine Learning: Training regressors to predict app ratings based on features like category, reviews, and size.

🛠️ Requirements
The analysis requires the following Python libraries:

pandas & numpy

plotly (for interactive charts)

scikit-learn

xgboost

🧹 Data Cleaning Highlights
To prepare the raw data for analysis, the following steps were implemented:

Faulty Data Removal: Eliminated "shifted" rows where category data was missing or incorrect.

Feature Engineering: * Converted Installs (e.g., "10,000+") and Price (e.g., "$4.99") into clean numeric formats.

Normalized the Size column into a uniform byte format, resolving entries in Megabytes (M) and Kilobytes (k).

Deduplication: Dropped duplicate app entries to ensure statistical accuracy.

📈 Key Insights from EDA
Market Distribution: The store is dominated by Free apps (~92.6%), with Family, Game, and Tools being the most populated categories.

Top Performers: The Game category leads in total engagement with approximately 13.87 billion installs.

Ratings Trends: The average app rating is 4.17, with genres like Puzzle (4.37) and Art & Design (4.36) receiving the highest average scores.

App Size vs. Success: There is only a weak correlation (0.13) between app size and installs, suggesting that small, optimized apps can be just as successful as large ones.

Freshness: Approximately 66% of the apps in the dataset were updated in 2018, indicating a highly active developer ecosystem.

🤖 Predictive Modeling
The project uses regression models to predict an app's rating.

Random Forest: Achieved a Mean Absolute Error (MAE) of 0.3876.

XGBoost: Implemented to further refine predictive accuracy through gradient boosting.

🚀 Usage
Ensure the googleplaystore.csv dataset is available in the data directory.

Open the google-play-store-analytics.ipynb notebook.

Run all cells to regenerate the cleaning pipeline, visualizations, and model results.
