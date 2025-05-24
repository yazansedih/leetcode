WITH userRated AS (
    SELECT 
        u.name,
        COUNT(*) AS rating_count
    FROM Users u
    JOIN MovieRating mr ON u.user_id = mr.user_id
    GROUP BY u.name
),
avgRating AS (
    SELECT 
        m.title,
        AVG(mr.rating) AS avg_rating
    FROM Movies m
    JOIN MovieRating mr ON m.movie_id = mr.movie_id
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY m.title
)

SELECT results FROM (
    SELECT name AS results
    FROM userRated
    ORDER BY rating_count DESC, name ASC
    LIMIT 1
) AS top_user

UNION ALL

SELECT results FROM (
    SELECT title AS results
    FROM avgRating
    ORDER BY avg_rating DESC, title ASC
    LIMIT 1
) AS top_movie;
