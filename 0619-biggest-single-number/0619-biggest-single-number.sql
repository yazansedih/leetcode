# Write your MySQL query statement below
SELECT MAX(nums.num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS nums;