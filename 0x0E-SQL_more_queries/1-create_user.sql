-- Creates the user user_0d_1 with all privileges.
CREATE USER
    IF NOT EXISTS 'chijiuba'@'localhost'
    IDENTIFIED BY 'chijiuba';
GRANT ALL PRIVILEGES
   ON *.*
   TO 'chijiuba'@'localhost';
