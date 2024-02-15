-- List records with a name value, displaying score and name in descending order by score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
