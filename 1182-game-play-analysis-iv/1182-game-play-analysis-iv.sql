# Write your MySQL query statement below
SELECT 
    ROUND(
        COUNT(DISTINCT a.player_id) / COUNT(DISTINCT f.player_id),
        2
    ) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) f
LEFT JOIN Activity a
    ON a.player_id = f.player_id 
    AND a.event_date = DATE_ADD(f.first_login, INTERVAL 1 DAY);
 