# Write your MySQL query statement below
select id, company, salary from
(select id, company, salary, 
ROW_NUMBER() over (partition by company order by salary asc, id asc) position,
count(*) over (partition by company) cnt
from Employee) j
where case when j.cnt % 2 = 0 then j.position = j.cnt / 2 or j.position = j.cnt / 2 + 1 else j.position = ceil(j.cnt / 2) end
order by company asc, salary asc, id asc