import pandas as pd

performance = pd.read_csv(
    "../data/processed/clean_performance.csv"
)

def recommend_funds(risk_level):

    filtered = performance[
        performance["risk_grade"] == risk_level
    ]

    return filtered.sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3)

print(
    recommend_funds("Moderate")
)