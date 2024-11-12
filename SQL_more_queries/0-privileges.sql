-- create user_01_1 if it does not exit and grant privileges
CREATE USER 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
