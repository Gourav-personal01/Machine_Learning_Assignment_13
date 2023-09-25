# Q7. Can Lasso Regression handle multicollinearity in the input features? If yes, how?

# Yes, Lasso Regression can handle multicollinearity in input feature

# Lasso Regression has a built-in feature selection mechanism due to its L1 regularization penalty. When faced with multicollinearity, Lasso tends to select one of the correlated predictors while setting the coefficients of the others to exactly zero.
# This automatic feature selection simplifies the model by removing less relevant predictors.

# While Lasso Regression helps with multicollinearity by selecting a subset of predictors, it may not completely eliminate multicollinearity in the selected features. The remaining selected predictors may still exhibit some level of correlation, albeit weaker than the original highly correlated set.

# Another approach to address multicollinearity before applying Lasso Regression is to perform Principal Component Analysis (PCA) or other dimensionality reduction techniques.