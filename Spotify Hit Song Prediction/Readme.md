
🎵 Spotify Hit Song Predictor: Binary Classification

This project implements a binary classification pipeline using Ensemble Methods (Random Forest and XGBoost) to predict whether a Spotify track will achieve High Popularity, defined as a Spotify Popularity Score greater than 75.

The solution is valuable for Data Scientists, Machine Learning engineers, and Business Analysts in the music industry who aim to identify potential hit songs early in their lifecycle.

Key Steps in the Pipeline
The notebook processes raw Spotify track and artist data through four main stages:

1) ⚙️ Feature Engineering & Data Preparation
Track Age: Calculated the age of each track (in years from the release date up to 2024) and used the median to impute missing values.

Genre Grouping: Extracted the primary artist genre and grouped less frequent genres into an 'other_genre' category, retaining the top 20 most common genres for modeling.

Target Creation: A binary column, is_highly_popular, was created, where:

1 (Hit): track_popularity >75

0 (Non-Hit): track_popularity ≤75

2) 📊 Exploratory Data Analysis (EDA)
EDA confirmed several key relationships:

The genre 'unknown' (a result of imputation/cleaning) and 'rap' were among the most frequent primary genres.

There's a positive correlation between track_popularity and the logarithmic scale of artist_followers, suggesting that tracks by artists with larger follower bases are generally more popular.

3) Model Training and Evaluation
Two powerful classification models were trained to predict the is_highly_popular target: Random Forest Classifier and XGBoost Classifier.

Both models were optimized using class weights (class_weight='balanced' for Random Forest and scale_pos_weight for XGBoost) to handle the significant class imbalance (the scarcity of 'Hit' tracks).

While overall accuracy is high, the low recall for the High Popularity (1) class suggests the model correctly identifies most non-hits but still struggles to capture a large percentage of the actual hit songs.

Conclusion: The models confirm that Artist Followers, Artist Popularity, and Track Duration are the most critical features in predicting a song's high popularity.
