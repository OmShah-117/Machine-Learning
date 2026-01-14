## AI Impact on Jobs 2030: Risk 

### Prediction using Support Vector Machine (SVM)-

This project aims to predict the Risk Category of a job (Low, Medium, or High) based on various job attributes, including salary, experience, education level, and key AI exposure indices. This is formulated as a Multi-Class Classification problem, with the Support Vector Classifier (SVC) being the primary model used for prediction.The analysis confirms a strong relationship between the target variable Risk_Category and the predictive features, resulting in a model with near-perfect accuracy on the test set.

### Project Structure-

The project is contained within a single Jupyter Notebook:Job Risk Pred (SVM).ipynb: Contains all steps from data loading, Exploratory Data Analysis (EDA), feature engineering, model training (SVC), and evaluation.

### Dataset and Key Insights- 

The dataset, sourced from a Kaggle competition, contains information on various job titles and their predicted risk levels concerning AI automation by 2030.Size: 3,000 rows.Quality: The data was exceptionally clean, with zero missing values and no duplicate rows, thus requiring no initial cleaning.Key Findings from EDARisk Distribution (Q2): The Medium Risk category is the largest, containing 1,521 jobs (over half the dataset). The Low 739 and High 740 risk categories are almost equally balanced.Risk & Automation (Q4): A direct correlation was confirmed:Low Risk jobs have a median Automation_Probability_2030 near 0.2. Medium Risk jobs have a median probability near 0.5.High Risk jobs have a median probability near 0.8.Education & Salary (Q1): A clear positive trend exists, where higher education levels generally correlate with higher average salaries (e.g., PhD salaries are highest).AI Exposure Index (Q5):Highest Exposure includes jobs like Graphic Designer, Construction Worker, and Delivery Driver.Lowest Exposure includes roles like Research Scientist, Data Analyst, and Teacher.

### Model and MethodologyFeature Engineering and Preprocessing-

The SVC model relies on distance calculations, necessitating careful preprocessing:Target Label Encoding: The categorical target variable, Y Risk_Category, was converted to numerical integers 0, 1, 2 using LabelEncoder. Categorical Encoding: Features like Job_Title and Education_Level were converted into a machine-readable format using OneHotEncoder.Numerical Scaling (Crucial for SVM): All numerical features (Salary, Experience, and Skill columns) were normalized using StandardScaler to ensure fair weighting in the SVC's distance-based algorithm.Model Training: Support Vector Classifier (SVC)Model: SVC with a Radial Basis Function (RBF) kernel and class_weight='balanced'.Split: 80% Training set, 20% Test set (stratified).

🚀 Results Metric Score Test: Set Accuracy 99.33%; Discussion on Accuracy- 

The near-perfect accuracy suggests that the Risk_Category is determined by very clear, quantifiable thresholds (e.g., on Automation_Probability_2030. The SVC model, being powerful for high-dimensional classification, was able to perfectly capture these boundaries.Note: The 99.33% accuracy is likely overstated for real-world application. While it confirms the features are extremely strong predictors, some degradation should be expected when applying the model to messy, unlabeled, real-world data outside the provided dataset.

💡 Why SVM was Chosen-

The Support Vector Machine (SVC) was an optimal choice for this problem:High-Dimensional Space: After OneHotEncoding for Job_Title and Education_Level, the feature space became high-dimensional. SVMs are mathematically designed to find the optimal separation hyperplane that maximizes the margin between classes in such complex spaces.Strong Generalization: When combined with the necessary StandardScaler preprocessing, SVMs provide strong generalization capabilities, making the model robust and less prone to overfitting than other algorithms might be in this scenario.

Kaggle Link- https://www.kaggle.com/code/omshah117/ai-job-risk-prediction
