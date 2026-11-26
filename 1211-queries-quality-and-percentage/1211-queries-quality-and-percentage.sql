# Write your MySQL query statement below
SELECT 
    q1.query_name,
    ROUND(
        AVG(q1.rating * 1.0 / q1.position)
    , 2) AS quality,
    ROUND(
        SUM(q1.rating < 3) * 100.0 / COUNT(*)
    , 2) AS poor_query_percentage
FROM Queries q1
GROUP BY q1.query_name
