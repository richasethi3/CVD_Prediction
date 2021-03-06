# Development and Validation of Cardiovascular Disease Risk Prediction Tool: A Machine Learning Approach

The webapp for this work can be accessed at http://cvd-prediction-app.herokuapp.com/

The goal of this project was to develop a cardiovascular disease risk assessment screening tool to predict risk of heart attack and stroke among adults using self-reported information. This would in turn could be used to get a probability of an individual developing cardiovascular disease based on a short questionnaire and evaluate risk score.

The dataset was obtained from the National Health and Nutrition Examination Survey (NHANES) – a population-based program of studies designed to assess the health and nutritional status of adults and children in the United States. 5-year (2011-2016) demographics, examination, laboratory and questionnaire data was collected from NHANES for 60, 936 individuals.

After data cleaning and processing, the target feature CVD_risk showed unequal distribution of classes with 12,878 negative classes and 1,611 positive classes, corresponding to 1:8 ratio between positive and negative class. Therefore, specialized sampling techniques were employed to handle class imbalance.

![Image](/Images/Picture1.png)

The performance of four classification algorithms – Logistic Regression, Support Vector Machine Random Forest, and k-Nearest Neighbors were analyzed using the default scikit-learn APIs. Figure below shows the Precision Recall curve and the ROC curve for the validation set with the most optimum model – Logistic Regression with SMOTEENN sampling. It showed 90% recall and 20% precision.

![Image](/Images/Picture3.png)

This approach can help transform the health insurance industry in two ways: they can provide new sources of insight to simplify and streamline current underwriting, and they can enhance the understanding of risk to enable more refined, granular categorizations of risk.

