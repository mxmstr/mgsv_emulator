#!/bin/bash
# Start MySQL service
service mysql start && sleep 3

# Set root password and flush privileges
service mysql start && sleep 3; mysql -h localhost -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123'; FLUSH PRIVILEGES;"
# Load initial tables from dbBase.sql
mysql -u root -h localhost -p123 < /dbBase.sql

# Load additional tables from dbMGO3.sql
mysql -u root -h localhost -p123 < /dbMGO3.sql

# Remove temporary SQL files
rm /dbBase.sql
rm /dbMGO3.sql

# Start Apache
apachectl -D FOREGROUND
