-- Write your PostgreSQL query statement below
WITH all_data AS (
    SELECT
        transaction_id,
        customer_id,
        t.product_id,
        transaction_date,
        amount,
        category,
        price
    FROM
        Transactions t
    JOIN
        Products p ON p.product_id = t.product_id
),
summary AS (
    SELECT
        count(distinct category) unique_categories,
        sum(amount) total_amount,
        COUNT(transaction_id) transaction_count,
        avg(amount) avg_transaction_amount,
        customer_id
    FROM
        all_data
    GROUP BY
        customer_id
),
product_category_count AS (
    SELECT
        count(*) count,
        category,
        customer_id,
        max(transaction_date) as last_transaction
        
    FROM
        all_data
    GROUP BY
        customer_id, category
),
most_frequent_category_inter AS (
    SELECT
        customer_id,
        first_value(category) over (partition by customer_id order by count desc, last_transaction desc) top_category,
        category
    FROM
        product_category_count
),
most_frequent_category as (
  select * from most_frequent_category_inter
  where category = top_category
)
SELECT
    ad.customer_id,
    round(total_amount, 2) total_amount,
    transaction_count,
    unique_categories,
    round(avg_transaction_amount, 2) avg_transaction_amount,
    mfcat.top_category,
    round(transaction_count * 10 +  total_amount / 100, 2) loyalty_score
FROM
    summary ad
JOIN
    most_frequent_category mfcat ON mfcat.customer_id = ad.customer_id
ORDER BY
    loyalty_score desc,
    ad.customer_id asc;
