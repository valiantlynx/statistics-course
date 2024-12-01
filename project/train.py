# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import statsmodels.api as sm
import joblib

# Load the dataset
dataset = pd.read_csv('text_data.csv', on_bad_lines='skip')

# Preprocess the data
def preprocess_data(dataset):
    # Convert text length categories to numerical values
    length_mapping = {'kort': 1, 'middels': 2, 'lang': 3}
    dataset['TextLength'] = dataset['TextLength'].map(length_mapping)
    
    # Convert complexity categories to numerical values
    complexity_mapping = {'lav': 1, 'middels': 2, 'hoy': 3}
    dataset['Complexity'] = dataset['Complexity'].map(complexity_mapping)
    
    # Convert ModelType to numerical values using one-hot encoding
    dataset = pd.get_dummies(dataset, columns=['ModelType'])
    
    # Drop rows with missing values
    dataset = dataset.dropna()
    
    return dataset

dataset = preprocess_data(dataset)

# Split the dataset into features and target
X = dataset.drop(columns=['Accuracy', 'Text'])
y = dataset['Accuracy']

# Ensure all data is numeric
y = y.astype(float)

# Feature scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a linear regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

# Make predictions
y_pred = linear_model.predict(X_test)

# Calculate model performance
mse = metrics.mean_squared_error(y_test, y_pred)
r2 = metrics.r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

# Train and evaluate Naive Bayes classifier on text data
def train_naive_bayes(dataset):
    vectorizer = TfidfVectorizer()
    X_text = vectorizer.fit_transform(dataset['Text'])
    
    # Categorize accuracy into discrete classes
    y_text = pd.cut(dataset['Accuracy'], bins=3, labels=['low', 'medium', 'high'])
    
    X_train_text, X_test_text, y_train_text, y_test_text = train_test_split(X_text, y_text, test_size=0.2, random_state=42)
    
    # Hyperparameter tuning for Naive Bayes
    nb_model = GaussianNB()
    nb_model.fit(X_train_text.toarray(), y_train_text)
    
    y_pred_text = nb_model.predict(X_test_text.toarray())
    accuracy = metrics.accuracy_score(y_test_text, y_pred_text)
    print(f'Naive Bayes Accuracy: {accuracy}')

train_naive_bayes(dataset)

# Plot residuals to check model fit
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color='blue', edgecolor='w', alpha=0.6)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=3)
plt.xlabel('Observed')
plt.ylabel('Predicted')
plt.title('Residual Plot')
plt.show()

# Multiple Linear Regression using statsmodels
X_with_constant = sm.add_constant(X_train)
y_train_array = np.asarray(y_train).astype(float)
ols_model = sm.OLS(y_train_array, X_with_constant).fit()
print(ols_model.summary())

# Save the processed dataset for future use
dataset.to_csv('processed_text_data.csv', index=False)

# Example usage with a Support Vector Machine (SVR) model
# Hyperparameter tuning for SVR
svr_model = SVR()
param_grid_svr = {'kernel': ['linear', 'rbf'], 'C': [0.1, 1, 10], 'gamma': ['scale', 'auto']}
grid_search_svr = GridSearchCV(svr_model, param_grid_svr, cv=5)
grid_search_svr.fit(X_train, y_train)
best_svr_model = grid_search_svr.best_estimator_

y_pred_svr = best_svr_model.predict(X_test)
svm_mse = metrics.mean_squared_error(y_test, y_pred_svr)
print(f'SVM Mean Squared Error: {svm_mse}')

# Train and evaluate Naive Bayes model on features
# Categorize accuracy into discrete classes for classification
y_train_class = pd.cut(y_train, bins=3, labels=['low', 'medium', 'high'])
y_test_class = pd.cut(y_test, bins=3, labels=['low', 'medium', 'high'])

nb_model = GaussianNB()
nb_model.fit(X_train, y_train_class)
y_pred_nb = nb_model.predict(X_test)
nb_accuracy = metrics.accuracy_score(y_test_class, y_pred_nb)
print(f'Naive Bayes Accuracy (features): {nb_accuracy}')

# Train a RandomForestRegressor model
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)
rf_mse = metrics.mean_squared_error(y_test, y_pred_rf)
rf_r2 = metrics.r2_score(y_test, y_pred_rf)
print(f'Random Forest Mean Squared Error: {rf_mse}')
print(f'Random Forest R-squared: {rf_r2}')

# Save the trained models
joblib.dump(linear_model, 'linear_model.pkl')
joblib.dump(nb_model, 'naive_bayes_model.pkl')
joblib.dump(best_svr_model, 'svm_model.pkl')
joblib.dump(rf_model, 'random_forest_model.pkl')
