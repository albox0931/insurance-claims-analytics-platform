SELECT
    claim_id,
    policy_id,
    customer_id,
    claim_date,
    claim_amount,
    claim_status,
    claim_type
FROM {{ source('insurance_analytics', 'raw_claims') }}
