select 
TO_CHAR(trans_date, 'YYYY-MM') as month,
country,
count(amount) trans_count,
sum(case when state = 'approved' then 1 else 0 end) approved_count,
sum(amount) trans_total_amount,
sum(case when state = 'approved' then amount else 0 end) approved_total_amount
from Transactions
group by country, TO_CHAR(trans_date, 'YYYY-MM')