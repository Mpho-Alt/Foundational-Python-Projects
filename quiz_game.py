# this is a python quiz game
question = (
    " In supervised machine learning, what is the primary distinction between regression and classification problems?",
    "Which evaluation metric is generally most appropriate for an imbalanced binary classification problem?",
    "What is the key assumption of the Ordinary Least Squares (OLS) estimator that ensures unbiasedness?",
    "What problem arises when an explanatory variable is correlated with the error term in a regression model?",
    "Which econometric technique is commonly used to address endogeneity?",
    "In quantitative economics, what does a Lagrange multiplier typically represent?",
    "Which concept best describes the idea that rational economic agents maximize utility subject to constraints?"
)

# The following questions are related to economics and econometrics and some data science concepts.
# It might be wise to research the answers before playing the game.

options = (
    "A.Regression uses labeled data, while classification uses unlabeled data ",
    "B.Regression predicts continuous outcomes, while classification predicts discrete classes ",
    "C.Regression is non-parametric, while classification is parametric ",
    "D. Regression cannot overfit, while classification can",

    "A. Accuracy",
    "B. Mean Squared Error (MSE)",
    "C.Precision–Recall or F1-score ",
    "D.R-squared ",

    "A.Homoskedasticity ",
    "B.No multicollinearity ",
    "C. Zero conditional mean of the error term",
    "D.Normality of the error term ",

    "A.Heteroskedasticity ",
    "B.Autocorrelation ",
    "C.Endogeneity ",
    "D. Overfitting",

    "A.Generalized Least Squares (GLS)",
    "B.Instrumental Variables (IV) estimation ",
    "C.Principal Component Analysis (PCA) ",
    "D. Ridge regression ",

    "A. The slope of the objective function",
    "B.The marginal change in the objective function given a relaxation of the constraint ",
    "C.The variance of the estimator",
    "D. The elasticity of demand",

    "A.Nash equilibrium",
    "B.Arbitrage pricing ",
    "C.Constrained optimization ",
    "D. Market clearing  "
)

answers = ("B", "C", "C", "C", "B", "B", "C")

score = 0
question_num = 0
guess = []

for q in question:
    print("------------------------------------------------------------------------------------------------------------------------------------------------------ ")
    print("\n" + q)

    for o in options[question_num * 4 : question_num * 4 + 4]:
        print(o)

    user_answer = input("Enter (A, B, C, or D): ").upper()
    guess.append(user_answer)

    if user_answer == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong! The correct answer is " + answers[question_num])

    question_num += 1

print("------------------------------------------------------------------------------------------------------------------------------------------------------ ")
print(f"You got {score} out of {len(question)} correct.")

score_percentage = int(score / len(question) * 100)
print(f"Your score percentage is: {score_percentage}")
print("------------------------------------------------------------------------------------------------------------------------------------------------------ ")    