# Q4. What are the tuning parameters that can be adjusted in Lasso Regression, and how do they affect the
# model's performance?

# The regularization parameter λ (or α) is a non-negative hyperparameter that controls the amount of L1 regularization applied to the model.
# Small Values (λ ≈ 0 or α ≈ 0): When λ is very close to zero, the L1 penalty has little effect, and Lasso Regression behaves similarly to ordinary least squares (OLS) regression. Coefficients may not be shrunk toward zero, and feature selection is less pronounced.
# Intermediate Values (0 < λ < ∞ or 0 < α < 1): As λ increases, the L1 penalty becomes stronger. Coefficients tend to be smaller, and some coefficients may be exactly zero, leading to feature selection. Intermediate values of λ strike a balance between model complexity and model fit.
# Large Values (λ → ∞ or α → 1): When λ is very large, the L1 penalty dominates the loss function, and coefficients are effectively driven to zero. The model becomes simpler, with many coefficients set to zero, resulting in significant feature selection.