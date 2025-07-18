# Write your MySQL query statement below

select j.user_id user_id, case when j.total = 0 then 0.00 else round(j.confirmed/j.total, 2) end confirmation_rate from
(select s.user_id, COUNT(CASE WHEN c.action = 'confirmed' THEN 1 END) confirmed, count(c.user_id) total from Signups s left join Confirmations c on c.user_id = s.user_id group by s.user_id) j