-- list all cities in california from the database htbn_0d_usa
-- sorted in ascending order
-- Uses a subquery to get california's state id

SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
