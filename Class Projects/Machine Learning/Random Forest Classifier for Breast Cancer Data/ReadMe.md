# Homework 5: Random Forest Classifier for Breast Cancer Data

## Quick Start
### Requirements
- Python 3.x
- Scikit-Learn
- Pandas
- NumPy

### Installation
1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the code:

### Hyperparameters Used
The following hyperparameters were tuned using `RandomizedSearchCV`:

- `n_estimators`: Ranges from 50 to 500 in steps of 50
- `max_depth`: [None, 10, 20, 30]
- `min_samples_split`: [2, 5, 10, 20, 50]
- `min_samples_leaf`: [1, 2, 4, 6, 8]

Final hyperparameters will be printed in the console output.

### Results
The model achieved the following performance metrics:
- **Features Used for Model**: Top 2 features with highest correlation to the target variable.
- **Average Accuracy**: 0.95, computed using cross-validation with 5 folds.
