SELECT
    customer_id, 
    COUNT(*) count_no_trans
FROM
    Visits 
WHERE
    visit_id not in (SELECT visit_id FROM Transactions)
GROUP BY customer_id;