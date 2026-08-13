WITH agg AS (
    SELECT
        TrafficType,
        COUNT(*) AS sessions,
        SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) AS conversions
    FROM sessions
    GROUP BY TrafficType
)
SELECT
    TrafficType,
    sessions,
    conversions,
    ROUND(100.0 * conversions / sessions, 2) AS conversion_rate_percent,
    CASE
        WHEN sessions > 1000 THEN 'High volume (>1000)'
        WHEN sessions BETWEEN 100 AND 1000 THEN 'Medium volume (100-1000)'
        ELSE 'Low volume (<100)'
    END AS volume_tier
FROM agg
ORDER BY sessions DESC;
--ORDER BY conversion_rate_percent DESC;