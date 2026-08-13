WITH agg AS (
    SELECT
        VisitorType,
        TrafficType,
        COUNT(*) AS sessions,
        SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) AS conversions
    FROM sessions
    GROUP BY VisitorType, TrafficType
    HAVING COUNT(*) >= 50
)
SELECT
    VisitorType,
    TrafficType,
    sessions,
    conversions,
    ROUND(100.0 * conversions / sessions, 2) AS conversion_rate_percent
FROM agg
ORDER BY VisitorType, conversion_rate_percent DESC;