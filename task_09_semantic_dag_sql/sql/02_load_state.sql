TRUNCATE TABLE numbers;
\copy numbers(number)
FROM 'data/numbers_5000.csv'
CSV HEADER;