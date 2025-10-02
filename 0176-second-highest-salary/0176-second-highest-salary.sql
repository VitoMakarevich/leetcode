SELECT MAX(salary) AS "SecondHighestSalary"
FROM (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    OFFSET 1 LIMIT 1
) sub;