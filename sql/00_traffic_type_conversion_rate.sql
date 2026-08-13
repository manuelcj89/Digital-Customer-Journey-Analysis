/*SELECT
    TrafficType,
    COUNT(*) AS sessions,
    SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) AS conversions,
    ROUND(
        100.0 * SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS conversion_rate_percent
FROM sessions
GROUP BY TrafficType
HAVING COUNT(*) > 1000
ORDER BY sessions DESC;*/

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
    ROUND(100.0 * conversions / sessions, 2) AS conversion_rate_percent
FROM agg
WHERE sessions > 1000
ORDER BY sessions DESC;