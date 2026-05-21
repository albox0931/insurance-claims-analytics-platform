import pandas as pd

claims = pd.read_csv("data/sample_claims.csv")

assert claims["claim_id"].is_unique, "Claim IDs should be unique"
assert claims["claim_amount"].notnull().all(), "Claim amount should not be null"
assert (claims["claim_amount"] > 0).all(), "Claim amount should be positive"
assert claims["claim_status"].isin(["Approved", "Rejected", "Pending"]).all(), "Invalid claim status found"

print("All data quality checks passed.")
