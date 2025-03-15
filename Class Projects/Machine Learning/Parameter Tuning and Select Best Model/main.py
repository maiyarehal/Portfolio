import util, warnings
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.model_selection import RandomizedSearchCV, cross_val_score
import numpy as np
from sklearn.exceptions import ConvergenceWarning
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore", category=ConvergenceWarning)
counts, weather, daily = util.prepare_data()

column_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'holiday',
                'daylight_hrs', 'PRCP', 'dry day', 'Temp (C)', 'annual']
X = daily[column_names]
y = daily['Total']


lr_model = LinearRegression(fit_intercept=False)
lr_model.fit(X, y)
daily['predicted'] = lr_model.predict(X)
lr_cv_scores = cross_val_score(lr_model, X, y, cv=10)


mean_lr = np.mean(lr_cv_scores)
print(f"The accuracy score for regular linear regression: {mean_lr}")

alpha_dist = np.logspace(-4, 4, 50)

params = {'alpha': alpha_dist}

ridge = Ridge()
ridge_search = RandomizedSearchCV(ridge, params, n_iter=10, cv=10, random_state=42, scoring='neg_mean_squared_error')
ridge_search.fit(X, y)

ridge_alpha = ridge_search.best_params_['alpha']

ridge = Ridge(alpha = ridge_alpha)
ridge.fit(X, y)

ridge_scores = cross_val_score(ridge, X, y, cv=10)
ridge_score = np.mean(ridge_scores)

print(f"The accuracy score for ridge with alpha value of {ridge_alpha}: {ridge_score}")


lasso_pipeline = Pipeline([('scaler', StandardScaler()), ('lasso', Lasso())])


lasso_search = RandomizedSearchCV(
    lasso_pipeline,
    param_distributions={'lasso__alpha': alpha_dist},
    n_iter=10,
    scoring='neg_mean_squared_error',
    cv=10,
    random_state=42
)

lasso_search.fit(X, y)



best_lasso_alpha = lasso_search.best_params_['lasso__alpha']
lasso = Lasso(alpha= best_lasso_alpha)

lasso.fit(X, y)

lasso_scores = cross_val_score(lasso, X, y, cv=10)
lasso_score  = np.mean(lasso_scores)


print(f"The accuracy score for lasso with alpha value of {best_lasso_alpha}: {lasso_score}")


scores = {
    'Linear Regression': mean_lr,
    'Ridge Regression': ridge_score,
    'Lasso Regression': lasso_score
}


best_model = max(scores, key=scores.get)
best_score = scores[best_model]

print(f"The best model is {best_model} with an accuracy score of {best_score}")
