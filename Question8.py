# Q8. How do you choose the optimal value of the regularization parameter (lambda) in Lasso Regression?

# Answer - 

# There are several method to do that - 

# k-Fold Cross-Validation: Divide the dataset into k subsets (folds). Train the Ridge Regression model on k-1 subsets and validate it on the remaining subset. 

#  Perform cross-validation for a range of λ values (often on a logarithmic scale). Select the λ that results in the lowest cross-validated MSE or another chosen metric.

# Use Predefined λ Values
