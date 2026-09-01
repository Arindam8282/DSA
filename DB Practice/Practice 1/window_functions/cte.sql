An employee is considered a High Performer if their individual total sales exceed the average salesperson total for their specific region.

🗄️ The Schema
Employees Table

emp_id (INT)

emp_name (VARCHAR)

region_id (INT)

Sales Table

sale_id (INT)

emp_id (INT)

sale_amount (NUMERIC)

Regions Table

region_id (INT)

region_name (VARCHAR)

🎯 The Goal
Write a query that outputs:

emp_name

region_name

total_sales (sum of all sales for that employee)

region_avg_sales (the average total_sales per employee within that region)

sales_rank (rank of the employee within their region based on total_sales, highest first, using DENSE_RANK())

Filter: Return ONLY employees whose total_sales is greater than their region_avg_sales.

WITH EmployeTotal AS (
    SELECT
        e.emp_name,
        r.region_id,
        r.region_name,
        SUM(s.sale_amount) AS total_sales
    FROM
        Employees e 
        JOIN
        Sales s ON
        e.emp_id = s.emp_id 
        JOIN 
        Regions r
        ON
        e.region_id = r.region_id
    GROUP BY e.emp_id,e.emp_name,r.region_id,r.region_name
);
WITH RegionMetrics AS (
    SELECT
    *,
    AVG(total_sales) OVER(
        PARTITION BY region_id
    ) AS region_avg_sales,
    DENSE_RANK() OVER(
        PARTITION BY region_id
        ORDER BY total_sales DESC
    ) AS sales_rank
    FROM
    EmployeeTotal;
);

SELECT * FROM RegionMetrics WHERE sales_rank > region_avg_sales;
