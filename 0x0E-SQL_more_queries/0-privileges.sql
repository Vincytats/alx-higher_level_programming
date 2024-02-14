#!/bin/bash

# MySQL credentials
MYSQL_USER="your_mysql_user"
MYSQL_PASSWORD="your_mysql_password"

# MySQL users to check
USERS=("user_0d_1" "user_0d_2")

# Loop through each user and retrieve privileges
for USER in "${USERS[@]}"; do
    echo "Privileges for $USER:"
    mysql -u$MYSQL_USER -p$MYSQL_PASSWORD -e "SHOW GRANTS FOR '$USER'@'localhost';"
    echo "-------------------------------------"
done
