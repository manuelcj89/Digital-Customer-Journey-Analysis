SELECT COUNT(*) AS total_sessions
FROM sessions;

SELECT *
FROM sessions
LIMIT 20;

SELECT DISTINCT VisitorType
FROM sessions;

--Traffic Type, no reference for 1-20 labels
SELECT DISTINCT TrafficType
FROM sessions;

