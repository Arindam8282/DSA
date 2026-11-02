The Schema:
Customers (customer_id, customer_name, signup_date)

Orders (order_id, customer_id, order_date, order_amount)
Write a query to help the marketing team find "High-Value Retained Customers". We want to output:

customer_name

total_spend (sum of all order_amount for that customer)

order_count (total number of orders placed by the customer)

first_order_date (the date of their very first order using MIN() OVER(...))

latest_order_date (the date of their most recent order using MAX() OVER(...))

Filter: Only return customers who have placed at least 3 orders AND have spent over $500 in total.


WITH CustomerOrders As (
    SELECT 
        c.customer_name,
        SUM(o.order_amount) total_spend,
        COUNT(o.order_id) order_count
        MIN(o.order_date)  as first_order_date,
        MAX(o.order_date) OVER(
            PARTITION BY c.customer_id
            ORDER BY o.order_date DESC
        ) as latest_order_date
    FROM
        Customers c JOIN
        Orders o ON
        o.customer_id = c.customer_id
    GROUP BY 
        c.customer_name,
        total_spend,
        order_count
);


SELECT * 
    FROM CustomerOrders 
    WHERE order_count > 3 AND
    total_spend > 500;