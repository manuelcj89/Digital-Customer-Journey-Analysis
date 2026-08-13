WITH agg AS (
    SELECT
        VisitorType,
        Weekend,
        COUNT(*) AS sessions,
        SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) AS conversions
    FROM sessions
    GROUP BY VisitorType, Weekend
    --HAVING COUNT(*) >= 50        Comment as only "Other" Weekend traffic has less than 50 sessions, but we want to include it in the analysis
)
SELECT
    VisitorType,
    Weekend,
    sessions,
    conversions,
    ROUND(100.0 * conversions / sessions, 2) AS conversion_rate_percent
FROM agg
ORDER BY VisitorType, conversion_rate_percent DESC;