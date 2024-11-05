-- lists scores and groups by score and sorts by score DESC
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
