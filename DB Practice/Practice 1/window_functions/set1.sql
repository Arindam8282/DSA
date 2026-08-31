Question 1: Ranking (Warm-up)
Schema: Products (product_id, product_name, category_id, price)

Goal: Write a query that selects product_name, category_id, and price, along with a column named price_rank that ranks products from most expensive to least expensive within each category_id (use ROW_NUMBER()).

SELECT 
    product_name,
    category_id,
    price,
    ROW_NUMBER() OVER(
        PARTITION BY category_id 
        ORDER BY price DESC
    ) as price_rank
FROM 
    Products;

Question 2?

Schema: CustomerOrders (customer_id, order_date, order_amount)

Goal: Write a query that shows customer_id, order_date, order_amount, and a column named previous_order_amount showing the amount of the customer's immediately preceding order ordered by order_date.

SELECT
    customer_id,
    order_date.
    order_amount,
    LAG(order_amount,1) OVER(
        PARTITION BY customer_id
        ORDER BY order_date ASC
    ) AS previous_order_amount
FROM
    CustomerOrders;


Question 3 Reminder:

Schema: Employees (emp_id, emp_name, department_id, salary)

Goal: Write a full query using a CTE to get only the Top 3 highest-paid employees in each department using DENSE_RANK().


WITH TemporaryTableName AS (
    -- 1. WRITE YOUR INSIDE QUERY HERE
    SELECT emp_name, salary, department_id,
           DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rank_num
    FROM Employees
)
-- 2. WRITE YOUR OUTSIDE QUERY HERE
SELECT emp_name, salary, department_id
FROM TemporaryTableName
WHERE rank_num <= 3 LIMIT 3;



The Schema:
UserLogins

user_id (INT)

login_date (DATE)

login_id (INT)

🎯 Drill A: Finding Next Login Date (LEAD)
Before finding full streaks, lets trace each users activity from one login to the next.
The Goal:
Write a query using LEAD() to display:

user_id

login_date

next_login_date (the date of the users subsequent login)

    SELECT 
        user_id,
        login_date,
        LEAD(login_date,1) OVER(
            PARTITION BY user_id
            ORDER BY login_date ASC
        ) AS next_login_date
    FROM
        UserLogins

🎯 Drill B: Finding 1-Day Login Streaks (CTE + Filter)
Now lets take your query and wrap it inside a CTE to answer an actual business question.

The Goal:
Using your query as the CTE base, write the full SQL code to find all logins where a user returned the very next day

WITH NextLoginInfo AS (
    SELECT 
        USER_ID,
        LOGIN_DATE,
        LEAD(login_date,1) OVER(
            PARTITION BY user_id
            ORDER BY login_date ASC
        ) AS next_login_date
    FROM UserLogins
);

SELECT user_id, login_date FROM NextLoginInfo WHERE DATEDIFF(next_login_date,login_date)=1;