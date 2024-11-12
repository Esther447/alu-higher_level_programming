-- Create user_0d_1 if it does not exist and grant privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Create user_0d_2 if it does not exist and grant privileges
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- List privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
