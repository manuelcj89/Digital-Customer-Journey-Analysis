
SELECT
    COUNT(*) AS total_sessions,
    SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) AS conversions,
    ROUND(
        100.0 * SUM(CASE WHEN Revenue = 1 THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS conversion_rate_percent
FROM sessions;