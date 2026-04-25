TRUNCATE TABLE numbers;
\copy numbers(number)
FROM 'data/numbers.csv'
CSV HEADER;