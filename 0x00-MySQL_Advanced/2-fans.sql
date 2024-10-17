-- SQL S=script thst  rank by country
-- order by number
SELECT origin, SUM(fans) AS nb_fans
	FROM mental_bands GROUP BY origin
	ORDER BY nb_fans DESC;
