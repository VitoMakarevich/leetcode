CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) 
RETURNS TABLE (Salary INT) AS $$
BEGIN
  -- Validate input
  IF N <= 0 THEN
    RETURN QUERY SELECT NULL::INT;  -- return a single row with NULL
    RETURN;
  END IF;

  -- Main query to get N-th highest salary
  RETURN QUERY
    SELECT DISTINCT e.salary
    FROM Employee e
    ORDER BY e.salary DESC
    OFFSET N - 1
    LIMIT 1;
END;
$$ LANGUAGE plpgsql;
