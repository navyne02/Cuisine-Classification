# Cuisine Classification Model

## Objective
Develop a machine learning model to classify restaurants based on their cuisine type.

## Features Used
- Average Cost for two
- Votes
- Price Range
- Has Table Booking
- Has Online Delivery
- City

## Model Used
- Random Forest Classifier

## Approach
- Cleaned dataset and handled missing values
- Simplified cuisines (used primary cuisine only)
- Reduced dataset to top 10 cuisines to handle imbalance
- Encoded categorical variables
- Split data into training and testing sets
- Trained the model and evaluated performance

## Results
- Achieved accuracy ≈ 37%
- Model performs better on frequent cuisines

## Sample Output
Predicted: North Indian | Actual: North Indian
Predicted: American | Actual: American

## Tech Stack
- Python
- Pandas
- Scikit-learn

## Challenges
- Class imbalance in dataset
- Weak relationship between features and cuisine
- Overlapping feature values across cuisines

## Conclusion
The model provides moderate accuracy due to overlapping features. Including more relevant features like menu data could improve performance.

