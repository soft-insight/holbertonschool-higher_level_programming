-- Import in hbtn_0c_0 database, temperatures.sql
-- script that displays the average temperature 
-- (Fahrenheit) by city ordered by temperature (descending).
-- to importe use: source ./<file>
SELECT city, AVG(value) 'avg_temp'
FROM temperatures
GROUP BY city
ORDER BY AVG(value) DESC;
