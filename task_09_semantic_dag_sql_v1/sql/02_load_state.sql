TRUNCATE TABLE numbers;

\copy numbers(number)
FROM 'data/numbers_500.csv'
CSV HEADER;