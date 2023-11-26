-- a script that lists all the cities of California that can be foud in the database hbtn_0d_usa
SELECT cities.id, cities.name
FROM cities
WHERE cities.states_id= (SELECT id FROM states WHEE name = 'California')
ORDER BY cities.id ASC;