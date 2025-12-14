# Global CO2 Emission Forecasting (2020-2024)

## Project Overview
This project focuses on building and evaluating a time series forecasting model for global **CO2 emissions** between 2020 and 2024. Using climate and energy consumption data, the goal is to predict daily `co2_emission` levels and identify areas for model performance improvement.

The primary model implemented is a **Random Forest Regressor**. The analysis is detailed in the accompanying Jupyter Notebook: `notebookcd07943da6.ipynb`.

## Dataset
The analysis utilizes the **Global Climate and Energy Consumption Dataset (2020-2024)**.
* **Code:** https://www.kaggle.com/code/omshah117/time-series-forecasting-of-global-co2-emissions
* **Size:** Over 36,000 daily records across various countries.
* **Target Variable:** `co2_emission`
* **Key Predictors:** `energy_consumption`, `temperature`, and date-related features.

## Exploratory Data Analysis (EDA) Highlights
The EDA section of the notebook revealed critical insights into the data's characteristics:

* **Strong Seasonality:** A clear, cyclical annual trend was observed in global average temperature, suggesting strong seasonality needs to be incorporated into the model.
* **High Correlation:** A significant **positive correlation** exists between `energy_consumption` and the target variable, `co2_emission`.
* **Top Emitters:** The United States, China, and Germany recorded the highest average CO2 emissions within the dataset's timeframe.

## Modeling and Results
A **Random Forest Regressor** was trained on the time series data to predict `co2_emission`. The model demonstrates **moderate to low accuracy**, highlighting the complexity of forecasting these environmental variables.

| Metric | Result |
| :--- | :--- |
| **Model Used** | Random Forest Regressor |
| **Mean Absolute Error (MAE)** | **180.72** |
| **Root Mean Squared Error (RMSE)** | **214.09** |

The high MAE (180.72) indicates that, on average, the model's predictions are significantly off. The larger RMSE suggests the presence of large errors for some predictions, confirming that the model needs substantial refinement.

## Future Improvements

To significantly enhance the model's predictive power, the following steps are recommended:

1.  **Time Series Feature Engineering:**
    * Implement **lagged features** (e.g., CO2 emission from the previous day or week) to directly capture historical dependencies.
    * Extract and encode **temporal features** (e.g., day of the week, month, season indicators) from the `date` column.
2.  **Alternative Model Architectures:**
    * Evaluate traditional time series models like **ARIMA** or **SARIMA** to better handle trend and seasonality.
    * Test deep learning models such as **LSTM (Long Short-Term Memory) Neural Networks**, which are highly effective for sequential data and capturing long-term temporal relationships.
3.  **Advanced Hyperparameter Tuning:**
    * Systematically optimize the current Random Forest's hyperparameters (`n_estimators`, `max_depth`) using techniques like Grid Search or Randomized Search to maximize its performance before switching to other models.

## Installation and Setup

To replicate this analysis, clone the repository and install the necessary dependencies:

```bash
git clone <repository-url>
cd co2-emission-forecasting
pip install -r requirements.md
