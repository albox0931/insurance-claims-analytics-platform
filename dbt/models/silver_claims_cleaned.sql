SELECT
    claim_id,
    policy_id,
    customer_id,
    claim_date,
    claim_amount,
    claim_status,
    claim_type,
    CURRENT_TIMESTAMP AS processed_at
FROM {{ ref('bronze_claims') }}
WHERE claim_amount > 0
