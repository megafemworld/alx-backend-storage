-- SQL S=script thst  rank by country
-- order by number
SELECT origin, SUM(fans) AS mb_fans
	FROM mental_bands
	GROUP BY origin
	ORDER BY mb_fans DESC;
