from database import get_connection

print("=" * 50)

print("HELIX DATABASE CONNECTION TEST")

print("=" * 50)

try:

    connection = get_connection()

    print()

    print("Database Connected Successfully!")

    print()

    print(connection)

    connection.close()

except Exception as e:

    print()

    print("Connection Failed")

    print(e)