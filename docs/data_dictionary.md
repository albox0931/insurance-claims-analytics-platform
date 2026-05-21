# Data Dictionary

## claims
- claim_id: unique claim identifier
- policy_id: related policy
- customer_id: related customer
- claim_date: date claim was submitted
- claim_amount: requested claim amount
- claim_status: Approved, Rejected, Pending
- claim_type: Auto, Health, Life, Property

## policies
- policy_id: unique policy identifier
- policy_type: type of insurance policy
- start_date: policy start date
- end_date: policy end date
- premium_amount: policy premium

## customers
- customer_id: unique customer identifier
- first_name: customer first name
- last_name: customer last name
- province: Canadian province
- age: customer age
