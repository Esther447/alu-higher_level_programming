-- Step 1: Create users if they don't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'password';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'password';

-- Step 2: Grant specific privileges to each user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';  -- This grants root-level access to user_0d_1
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';  -- Grants only SELECT and INSERT to user_0d_2 on user_2_db

-- Step 3: Ensure changes are applied
FLUSH PRIVILEGES;
