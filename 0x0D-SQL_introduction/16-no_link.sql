-- List records without no values and display score and name
SELECT score, name FROM second_table WHERE name IS NOT NULL AND ORDER BY score DESC;