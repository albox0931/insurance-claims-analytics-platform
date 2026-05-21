SELECT
    claim_type,
    claim_status,
    COUNT(*) AS total_claims,
    SUM(claim_amount) AS total_claim_amount,
    AVG(claim_amount) AS avg_claim_amount
FROM {{ ref('silver_claims_cleaned') }}
GROUP BY claim_type, claim_status
