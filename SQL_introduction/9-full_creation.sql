-- a script that creates a table second_table in the database hbtn_0c_0
CREATE TABLE IF NOT EXISTS second_table (
    id INT, name VARCHAR(256), score INT
);
-- create records
INSERT INTO second_table (id, name, score)(1, 'john', 10);
INSERT INTO second_table (id, name, score)(2, 'Alex', 3);
INSERt INTO second_table (id, name, score)(3, 'Bob', 14);
INSERT INTO second_table (id, name, score)(4, 'George', 8);
