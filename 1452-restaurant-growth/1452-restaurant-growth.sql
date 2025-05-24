SELECT 
    c1.visited_on,
    SUM(c2.daily_amount) AS amount,
    ROUND(AVG(c2.daily_amount), 2) AS average_amount
FROM (
    SELECT visited_on, SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
) c1
JOIN (
    SELECT visited_on, SUM(amount) AS daily_amount
    FROM Customer
    GROUP BY visited_on
) c2
ON DATEDIFF(c1.visited_on, c2.visited_on) BETWEEN 0 AND 6
GROUP BY c1.visited_on
HAVING COUNT(*) = 7
ORDER BY c1.visited_on;
