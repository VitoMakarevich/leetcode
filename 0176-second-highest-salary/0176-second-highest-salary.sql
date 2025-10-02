with distinct_salaries as (
  select distinct salary from Employee
),
salaries_with_rank as (
  select salary, (dense_rank() over (order by salary desc)) "rank" from distinct_salaries
),
second_salary_with_null as (
  select salary from salaries_with_rank where "rank" = 2
  union
  select null
)
select salary "SecondHighestSalary" from second_salary_with_null order by salary nulls last limit 1
