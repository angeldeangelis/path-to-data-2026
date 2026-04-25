SELECT
    n.number,
    b.label AS baseline_label,
    a.label AS adjusted_label
FROM numbers n
JOIN classified_numbers_baseline b USING (number)
JOIN classified_numbers_adjusted a USING (number)
WHERE b.label <> a.label
ORDER BY n.number;
```