-- a script that creates the database hbtn_02d_2 and
-- the user user_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
