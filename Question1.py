# # Q1. What is Lasso Regression, and how does it differ from other regression techniques?

# # Answer - 
# # 
# Lasso introduces an L1 regularization penalty to the linear regression model. This penalty term adds the absolute values of the coefficients to the loss function being minimized. The L1 regularization term encourages sparsity by forcing some coefficients to be exactly zero, effectively performing feature selection.

# Lasso has a built-in feature selection mechanism. By setting some coefficients to zero, it effectively removes less relevant predictors from the model.

# Lasso can handle multicollinearity (high correlation among predictors) by selecting one of the correlated predictors and setting the coefficients of the others to zero. This can simplify the model and reduce overfitting.