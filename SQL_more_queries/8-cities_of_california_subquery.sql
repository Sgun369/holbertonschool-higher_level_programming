-- a script that lists all the cities of California that can be foud in the database hbtn_0d_usa
SELECT id, 'name'
    FROM cities
    WHERE cities.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id;
