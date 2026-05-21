SELECT claim_status, COUNT(*) AS total_claims
FROM INSURANCE_ANALYTICS.SILVER.CLEAN_CLAIMS
GROUP BY claim_status;

SELECT claim_type, SUM(claim_amount) AS total_claim_amount
FROM INSURANCE_ANALYTICS.SILVER.CLEAN_CLAIMS
GROUP BY claim_type;

SELECT claim_type, claim_status, COUNT(*) AS total_claims
FROM INSURANCE_ANALYTICS.SILVER.CLEAN_CLAIMS
GROUP BY claim_type, claim_status;
