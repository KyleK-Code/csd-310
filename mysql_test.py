import mysql.connector  # to connect to MySQL
from mysql.connector import errorcode

from dotenv import dotenv_values  # to read .env file

# Load secrets from .env file
secrets = dotenv_values(".env")

# Database connection configuration
config = {
    "user": secrets["USER"],
    "password": secrets["PASSWORD"],
    "host": secrets["HOST"],
    "database": secrets["DATABASE"],
    "raise_on_warnings": True
}

try:
    # Connect to MySQL
    db = mysql.connector.connect(**config)
    
    print(f"\n  Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}")
    
    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    # Close the connection
    db.close()