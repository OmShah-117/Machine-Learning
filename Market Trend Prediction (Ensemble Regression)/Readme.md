📈Market Trend Prediction using M-Ensemble Regression

Project Overview-

This project implements a complete data science pipeline for financial time-series analysis and market trend prediction. It leverages historical market data and various external factors, including economic indicators, volatility indices (VIX), and market sentiment scores, to predict the Daily Return Percentage of a stock or index.
The pipeline includes Data Cleaning, extensive Exploratory Data Analysis (EDA) using Plotly, Feature Engineering to create lagged and volatility indicators, and the development of a predictive model using an M-Ensemble (Voting Regressor) approach.

🎯 Goal

The primary objective is to predict the Daily Return Percentage using a combination of traditional and machine learning regression models, and to evaluate their performance, highlighting the challenges of forecasting market returns.

📂 Dataset

The project utilizes the Market_Trend_External.csv dataset, which contains daily time-series data covering a significant period (1902-2023).

🛠️ Pipeline and Methodology-

Data Loading and Initial Inspection 
1. The dataset was loaded and inspected for structure and data types.The Date column was converted to datetime format for time-series analysis.No advanced cleaning (like missing value imputation) was explicitly required after initial inspection.

2. Exploratory Data Analysis (EDA)EDA was performed using Plotly to visualize trends and relationships:
Q1: Close Price Trend Over Time: A line plot revealed the long-term upward trend in the closing price (1902-2023).
Q2: Daily Return Distribution: A histogram showed that the daily returns are tightly clustered around zero, as expected for market returns.
Q3: VIX vs. Daily Return: A scatter plot with an OLS trendline explored the relationship between the VIX (volatility index) and daily returns, suggesting an inverse correlation (higher VIX often correlates with lower returns, though the trend is weak).
Q4: Economic News vs. Volatility: A bar plot compared the average Volatility_Range (High-Low) on days with and without an Economic_News_Flag, showing that days with news events have a higher average volatility.
Q8: Correlation Matrix: A heatmap of financial variables indicated extremely high correlation (close to 1) between the different price columns (Open_Price, High_Price, Low_Price, Close_Price).

3. Feature Engineering and Data PreparationTo facilitate the prediction of the next day's return, several time-series specific features were engineered:
Target Variable: Target was set as the Daily_Return_Pct.
Lagged Features (Shifted by 1 day):Close_Lag1 (Previous day's closing price)VIX_Lag1 (Previous day's VIX close)Sentiment_Lag1 (Previous day's sentiment score)
Volatility Indicator:Volatility_7D (7-day rolling standard deviation of Daily_Return_Pct, lagged by 1 day)The final modeling dataset was filtered to the last 10,000 observations (df_model) and split into an 80/20 train/test set using a time-series split (data is not shuffled).
4. Ensemble Regression ModelingAn M-Ensemble (Voting Regressor) was implemented to combine the predictive power of different base models:
Base Models:
rgr1: Linear Regression
rgr2: Decision Tree Regressor (max_depth=5)
rgr3: Random Forest Regressor (n_estimators=50, max_depth=5)
Ensemble Model:vrg: Voting Regressor combining rgr1, rgr2, and rgr3 with weights set to [1, 1, 2] (giving higher importance to the Random Forest).

📊 Model Evaluation Results

The models were evaluated on the test set using two standard regression metrics: Root Mean Squared Error (RMSE) and R2 Score.

Key Findings-

The Random Forest Regressor demonstrated the best individual performance, achieving the lowest RMSE (17.3814) and the highest R2 score (0.0573).The Voting Regressor performed better than the Linear Regression and Decision Tree models, validating the ensemble approach, but was slightly outperformed by the Random Forest.Despite the Random Forest being the best model, its R^2 score of 0.0573 indicates that it explains less than 6% of the variance in the daily returns. This result is typical for predicting highly noisy and near-random financial time-series data, emphasizing the difficulty of "beating the market."

💻 Technologies Used

Python,
Pandas (Data Manipulation),
NumPy (Numerical Operations),
Plotly Express (Data Visualization/EDA),
Scikit-learn (Machine Learning: LinearRegression, DecisionTreeRegressor, RandomForestRegressor, VotingRegressor).

Kaggle Link- https://www.kaggle.com/code/omshah117/market-trend-prediction-m-ensemble-regression
