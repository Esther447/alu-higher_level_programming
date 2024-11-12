-- Check if user_0d_1 exists before showing grants
SELECT IF(EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost'),
           'User user_0d_1 exists, showing grants...',
           'User user_0d_1 does not exist.') AS Result;
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Check if user_0d_2 exists before showing grants
SELECT IF(EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost'),
           'User user_0d_2 exists, showing grants...',
           'User user_0d_2 does not exist.') AS Result;
SHOW GRANTS FOR 'user_0d_2'@'localhost';
