# Group 8 - Parameter Tuning and Select Best Model

## Quick Start

### Prerequisites
Before running the code, make sure you have Python installed along with the necessary dependencies. You can install the dependencies using `pip` and the provided `requirements.txt` file.

```
pip install -r requirements.txt
```

### Running the Code
1. Make sure the following files are present in the directory:
   - `main.py`: The main script to run the models.
   - `util.py`: A helper function to load the bicycle traffic datasets.
   - `data`: data folder containg the bicycle traffic datasets
   - `requirements.txt`: The list of dependencies.

2. Run the `main.py` script to create and test the 3 models.
```
python main.py
```

3. The output will print the accuracy for each model and alpha for ridge and lasso. Also will print the best model and its accuracy



### Scores for each Model

#### Linear Regression Model
 - Accuracy Score: .769

#### Lasso Regression Model
 - Alpha: 7.906
 - Accuracy Score: .768

#### Ridge Regression Model
 - Alpha: 1.207
 - Accuracy Score: .770

### Best Model
The best model was calculated to be the Ridge Regression model.
The ridge regression model had an accuracy of .770 with an alpha value of 1.207
