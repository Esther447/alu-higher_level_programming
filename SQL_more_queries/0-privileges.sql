-- Check if user_0d_1 exists and display their grants if they do
SELECT 'Checking privileges for user_0d_1@localhost' AS Info;
IF EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost') THEN
    SHOW GRANTS FOR 'user_0d_1'@'localhost';
ELSE
    SELECT 'There is no such grant defined for user user_0d_1 on host localhost' AS Result;
END IF;

-- Check if user_0d_2 exists and display their grants if they do
SELECT 'Checking privileges for user_0d_2@localhost' AS Info;
IF EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost') THEN
    SHOW GRANTS FOR 'user_0d_2'@'localhost';
ELSE
    SELECT 'There is no such grant defined for user user_0d_2 on host localhost' AS Result;
END IF;
