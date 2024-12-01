# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Load the dataset
dataset = pd.read_csv('text_data.csv')

# Preprocess the data
def preprocess_data(dataset):
    # Convert text length categories to numerical values
    length_mapping = {'kort': 1, 'middels': 2, 'lang': 3}
    dataset['TextLength'] = dataset['TextLength'].map(length_mapping)
    
    # Convert complexity categories to numerical values
    complexity_mapping = {'lav': 1, 'middels': 2, 'hoy': 3}
    dataset['Complexity'] = dataset['Complexity'].map(complexity_mapping)
    
    return dataset

dataset = preprocess_data(dataset)

# Split the dataset into features and target
X = dataset[['TextLength', 'Complexity', 'ModelType']]
y = dataset['Accuracy']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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
    y_text = dataset['Accuracy']
    
    X_train_text, X_test_text, y_train_text, y_test_text = train_test_split(X_text, y_text, test_size=0.2, random_state=42)
    
    nb_model = MultinomialNB()
    nb_model.fit(X_train_text, y_train_text)
    
    y_pred_text = nb_model.predict(X_test_text)
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
ols_model = sm.OLS(y_train, X_with_constant).fit()
print(ols_model.summary())

# Save the processed dataset for future use
dataset.to_csv('processed_text_data.csv', index=False)

# Example usage with a Support Vector Machine (SVM) model
svm_model = SVC(kernel='linear')
svm_model.fit(X_train, y_train)
y_pred_svm = svm_model.predict(X_test)
svm_accuracy = metrics.accuracy_score(y_test, y_pred_svm)
print(f'SVM Accuracy: {svm_accuracy}')

# Save the trained model
import joblib
joblib.dump(linear_model, 'linear_model.pkl')
joblib.dump(nb_model, 'naive_bayes_model.pkl')
joblib.dump(svm_model, 'svm_model.pkl')
