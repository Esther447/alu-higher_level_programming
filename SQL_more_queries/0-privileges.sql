-- a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';

-- Step 2: Grant privileges to the users if necessary
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- Step 3: Show privileges for each user
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
