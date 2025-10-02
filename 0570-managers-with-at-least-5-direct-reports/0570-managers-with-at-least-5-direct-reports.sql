-- Write your PostgreSQL query statement below
with manager_ids_with_more_than_5_reports as(
  select managerId as id from Employee group by managerId having count(*) >= 5
)
select e.name from Employee e join manager_ids_with_more_than_5_reports m
on e.id = m.id