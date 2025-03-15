# Homework 6: SVM Digit Classification

## Quick Start
### Requirements
- Matplotlib 
- Scikit-Learn
- Pandas
- NumPy
- Seaborn

### Installation
1. Clone the repository.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Jupyter Notebook
    ```bash
    jupyter notebook hw6.ipynb
    ```
4. View results:
      - The notebook will show the performance of linear, radical (RBF), and polynomial kernals, including cross-validation and test accuracies.
      - Visualization and classification reports will also be generated.
  
## Parameters Selected
- **Linear Kernal**
    - C: 10.0
- **Radical (RBF) Kernal**
    - C: 100.0
    - Gamma: 0.01
- **Polynomial Kernal**
    - C: 1.0
    - Degree: 3
 
## Results
### Cross-Validation Accuracy

|Kernal            | Accuracy         | 
|----------------- |----------------- |
| Linear           | 94.13%           |
| Radical (RBF)    | 98.14%           |
| Polynomial       | 92.75%           |
---------------------------------------

## Classification Reports
- **Linear Kernal**
  ```plaintext
              precision    recall  f1-score   support

           0       0.98      1.00      0.99        53
           1       0.96      0.96      0.96        50
           2       1.00      1.00      1.00        47
           3       0.96      0.96      0.96        54
           4       0.98      1.00      0.99        60
           5       0.94      0.97      0.96        66
           6       1.00      0.98      0.99        53
           7       1.00      0.98      0.99        55
           8       0.93      0.91      0.92        43
           9       0.97      0.95      0.96        59

   accuracy                            0.97       540
   macro avg       0.97      0.97      0.97       540
   weighted avg    0.97      0.97      0.97       540
   ```

- **Radical (RBF) Kernal**
  ```plaintext
              precision    recall  f1-score   support

           0       0.98      1.00      0.99        53
           1       1.00      1.00      1.00        50
           2       0.98      1.00      0.99        47
           3       0.98      0.98      0.98        54
           4       1.00      1.00      1.00        60
           5       0.98      0.98      0.98        66
           6       1.00      1.00      1.00        53
           7       0.98      0.98      0.98        55
           8       0.98      0.93      0.95        43
           9       0.95      0.95      0.95        59

   accuracy                            0.98       540
   macro avg       0.98      0.98      0.98       540
   weighted avg    0.98      0.98      0.98       540
   ```

- **Polynomial Kernal**
  ```plaintext
              precision    recall  f1-score   support

           0       0.98      1.00      0.99        53
           1       0.98      1.00      0.99        50
           2       1.00      1.00      1.00        47
           3       0.98      0.96      0.97        54
           4       1.00      0.97      0.98        60
           5       0.98      0.97      0.98        66
           6       0.98      0.98      0.98        53
           7       1.00      0.98      0.99        55
           8       0.91      0.95      0.93        43
           9       0.97      0.98      0.97        59

   accuracy                            0.98       540
   macro avg       0.98      0.98      0.98       540
   weighted avg    0.98      0.98      0.98       540
  ```

## Notes
- PCA reduced the dimensionality from the original dataset to retain 80% of the information.
- RandomSearchCV was used to tune the hyperparameters for each kernal.
- Results indicate that the **Radical (RBF) Kernal** had the best overall performance on both cross-validation and test data.
