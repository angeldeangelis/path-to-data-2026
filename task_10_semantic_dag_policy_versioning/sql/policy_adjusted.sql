WITH
base AS (
    SELECT
        number,
        number % 2 = 0  AS is_even,
        number % 3 = 0  AS is_mult_3,
        number % 4 = 0  AS is_mult_4
    FROM numbers
),
intermediate AS (
    SELECT
        *,
        is_even AND is_mult_4       AS is_strong,
        is_mult_3 AND NOT is_even   AS is_weak
    FROM base
),
final AS (
    SELECT
        number,
        CASE
            WHEN (is_strong AND is_mult_3) OR (is_mult_3 AND is_even) THEN 'CRITICAL' 
            WHEN is_weak THEN 'IMPORTANT'
            WHEN is_even AND NOT is_strong THEN 'SECONDARY'
            ELSE 'NORMAL'
        END AS label
    FROM intermediate
)
SELECT *
FROM final
ORDER BY number;