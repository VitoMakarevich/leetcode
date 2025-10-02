-- Write your PostgreSQL query statement below

-- select  department_name "Department", employee_name "Employee", salary "Salary"
-- from
-- ( 
  select d.name "Department", employee_name "Employee", salary "Salary" from Department d join
  (
    select departmentId, employee_name, salary from
    (
      select 
      departmentId,
      name employee_name,
      salary,
      dense_rank() over (partition by departmentId order by salary desc) rnk
      from Employee
    ) where rnk <= 3
  ) e on d.id = e.departmentId
-- )