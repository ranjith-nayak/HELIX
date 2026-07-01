import mysql.connector

from Framework.config import DB_CONFIG

# ============================================================
# HELIX DATABASE CONNECTION
# ============================================================

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


# ============================================================
# HELIX CURSOR
# ============================================================

def get_cursor():

    connection = get_connection()

    cursor = connection.cursor()

    return connection, cursor